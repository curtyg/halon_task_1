import unreal
from unreal import Vector, ProgressBar
import itertools

from noise import generate

# import argparse

import os

import math


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

    for actor in all_lvl_actors:
        if actor.get_actor_label().startswith("Gen_StaticMeshCube"):
            editor_actor_subs.destroy_actor(actor)


def generate_grid(size: int, relative_distance: int = 100):
    grid_coords = [
        [(i * relative_distance, j * relative_distance) for i in range(size)]
        for j in range(size)
    ]
    return grid_coords


def generate_terrain(
    width: int, z_depth: int = 5, scale: int = 100, cube_scale: float = 1.0
):

    counter = 0
    scale = scale * cube_scale
    text_label = "Generating Cubes!"
    with unreal.ScopedSlowTask(width*width*z_depth, text_label) as slow_task:
        slow_task.make_dialog(True) 
        for x, y in itertools.product(range(width), repeat=2):
            x *= scale
            y *= scale
            for z in range(z_depth):
                
                if slow_task.should_cancel():
                    break
                slow_task.enter_progress_frame(1)
                
                z *= scale
                
                noise = generate(x * 0.01, y * 0.01, z * 0.01)
                noise += 1
                noise /= 2

                if noise > 0:
                    counter += 1
                    cube = spawn_cube(x, y, z)

        unreal.log(f"CUBES CREATED: {counter}")


def main():
    progress_bar = ProgressBar()
    delete_all_cubes()
    generate_terrain(15, 5, 100)



    # # Get the current working directory
    # current_directory = os.getcwd()

    # cube = spawn_cube(0,0,0)

    # origin, extent = cube.get_actor_bounds(False)

    # # Calculate the absolute size of the cube (extent is half the size, so multiply by 2)
    # absolute_size = extent * 2
    # print(absolute_size)


main()
