import unreal
from unreal import Vector

# import argparse

import os

import math


def spawn_cube(location: Vector = Vector(), cube_scale: Vector = Vector.ONE):

    # basically getting an object that can allow me to interact with one subsystem of
    # editor....in this case the actor subsystem
    editor_actor_subs = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

    # static mesh actors can't be animated - presumably they are basically for object and geometry?
    actor_class = unreal.StaticMeshActor

    # place the actor in the scene on the editor
    static_mesh_actor = editor_actor_subs.spawn_actor_from_class(actor_class, location)

    # give the the cube mesh so it displays a cube
    cube_mesh = unreal.EditorAssetLibrary.load_asset("/Engine/BasicShapes/Cube.Cube")

    # set the assign the cube mesh to the actor
    static_mesh_actor.static_mesh_component.set_static_mesh(cube_mesh)
    static_mesh_actor.static_mesh_component.set_editor_property(
        "relative_scale3d", cube_scale
    )


def generate_grid(size: int, relative_distance: int = 100):
    grid_coords = [
        [(i * relative_distance, j * relative_distance) for i in range(size)]
        for j in range(size)
    ]
    return grid_coords


# def print_input(input):
#     print(input)

def generate_noise(x: float, y: float, z: float):
    pass
    
def main(input):
    
    # # Get the current working directory
    # current_directory = os.getcwd()

    
    # parser = argparse.ArgumentParser(description="Editor inputted args")
    
    # parser.add_argument(
    #     "--input", 
    #     type=str, 
    #     help="The input string", 
    #     required=True
    # )

    # args = parser.parse_args()

    # if args.input:
    #     print(args.input)
        
    print(input)
    
    cube_scale = Vector(0.5, 0.5, 0.5)

    cube_coords = generate_grid(30)
    print(cube_coords)

    for row in cube_coords:
        for x, y in row:
            spawn_cube(Vector(x, y, 0), cube_scale)
            
# if __name__ == "__main__":
    
#     # Get the current working directory
#     current_directory = os.getcwd()

    
#     parser = argparse.ArgumentParser(description="Editor inputted args")
    
#     parser.add_argument(
#         "--input", 
#         type=str, 
#         help="The input string", 
#         required=True
#     )

#     args = parser.parse_args()

#     if args.input:
#         print(args.input)
        
#     cube_scale = Vector(0.5, 0.5, 0.5)

#     cube_coords = generate_grid(8)
#     print(cube_coords)

#     for row in cube_coords:
#         for x, y in row:
#             spawn_cube(Vector(x, y, 0), cube_scale)
