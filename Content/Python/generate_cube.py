import unreal
from unreal import Vector, ProgressBar
import itertools
import sys
import noise
from importlib import *

reload(noise)

DEFAULT_CUBE_SIZE = 100


def spawn_cube(x, y, z, cube_scale: Vector = Vector.ONE) -> unreal.StaticMeshActor:
    location = Vector(x, y, z)
    # basically getting an object that can allow me to interact with one subsystem of
    # editor....in this case the actor subsystem
    editor_actor_subs = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

    # static mesh actors can't be animated - presumably they are basically for object and geometry?
    actor_class = unreal.StaticMeshActor

    # place the actor in the scene on the editor
    static_mesh_actor = editor_actor_subs.spawn_actor_from_class(actor_class, location)
    static_mesh_actor.set_actor_label(f"Gen_StaticMeshCube_{x}{y}{z}")

    # give the the cube mesh so it displays a cube
    cube_mesh = unreal.EditorAssetLibrary.load_asset("/Engine/BasicShapes/Cube.Cube")

    # set the assign the cube mesh to the actor
    static_mesh_actor.static_mesh_component.set_static_mesh(cube_mesh)

    # print(f"DEFAULT SCALE: {static_mesh_actor.get_actor_scale3d()}")
    # print(f"DEFAULT RELATIVE SCALE: {static_mesh_actor.get_actor_relative_scale3d()}")

    return static_mesh_actor


def delete_all_cubes():
    editor_actor_subs = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

    all_lvl_actors = editor_actor_subs.get_all_level_actors()
    with unreal.ScopedSlowTask(
        len(all_lvl_actors), "Deleting old cubes..."
    ) as slow_task:
        slow_task.make_dialog(True)
        for actor in all_lvl_actors:
            if slow_task.should_cancel():
                break
            slow_task.enter_progress_frame(1)
            if actor.get_actor_label().startswith("Gen_StaticMeshCube"):
                editor_actor_subs.destroy_actor(actor)


def generate_grid(size: int, relative_distance: int = 100):
    grid_coords = [
        [(i * relative_distance, j * relative_distance) for i in range(size)]
        for j in range(size)
    ]
    return grid_coords


def generate_terrain(
    width: int,
    z_depth: int = 5,
    cube_scale: float = 1.0,
    seed: int = 42,
):

    counter = 0
    scale = DEFAULT_CUBE_SIZE * cube_scale
    text_label = "Generating Cubes!"
    
    with unreal.ScopedSlowTask(width * width * z_depth, text_label) as slow_task:
        slow_task.make_dialog(True)
        for x, y in itertools.product(range(width), repeat=2):
            for z in range(z_depth):
                if slow_task.should_cancel():
                    break
                slow_task.enter_progress_frame(1)

                n = noise.generate(x * 0.1, y * 0.1, z * 0.1, seed)
                n += 1.0
                n /= 2.0

                print(f"X: {x}, Y: {y}, Z : {z}")
                print(n)

                if n > 0.5:
                    counter += 1
                    cube = spawn_cube(x * scale, y * scale, z * scale)

        unreal.log(f"CUBES CREATED: {counter}")


def main(width, z_depth, seed):

    if width > 50:
        unreal.log_warning("Please select a width less than 100")
        sys.exit()
    if z_depth > 10:
        unreal.log_warning("Please select a z_depth less than 10")
        sys.exit()

    if any(v == 0 for v in [width, z_depth, seed]):
        unreal.log_warning(
            "Please select non-zero integer values for width, z_depth and seed"
        )
        sys.exit()

    unreal.log(f"Generating with WIDTH: {width}, Z_DEPTH: {z_depth}, SEED: {seed}")

    delete_all_cubes()
    generate_terrain(width, z_depth, 1.0, seed=seed)
