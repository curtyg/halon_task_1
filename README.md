# halon_task_1 - procedural generation

## Approach and Thought Process

I chose to do Task 1 due to having an interest in procedural generation having previously watched some GDC talks on the topic and played games that make use of the technique etc.

I did not, however, have any experience coding an algorithm for procedural generation. Task 2 or 4 might have made more sense seeing as I actually had experience with the algorithms these were displaying (although this experience was brief, only in my university degree 6-7 years ago...) but I knew I would find it fun and interesting to attempt procedural generation so I made the perhaps ill-fated decision of going with it!

I also decided early on I would attempt to do the task mainly utilising python, as its the programming language I have used most to date and I had seen that the Unreal python API was quite extensive so figured I would not be too limited with it, especially considering the scope of the tasks involved. I wasn't sure about any sort of 'animating' and whether I could do that with python but never had to cross that road as I chose task 1.

Initially I knew there would be some things I would need to learn regardless of what task I chose, so my initial thought process was to get and end-to-end flow of a editor widget on which I could click a button and generate a single cube. On top of this I wanted to work out if I could pass input from the widget to my script and whether I could also delete the cube programmatically. I broke this down into a series of smaller tasks before worrying about the algorithm or other main deliverables of the task

## Computer Science principles applied

Having decided on doing Task 1 I knew i would have to decide on an algorithm to use. There seemed to be a number of resources online discussing procedural generation, including a wiki dedicated to it and the different techniques. At some point I decided on using Perlin noise - purely because I could find both Ken Perlin's original (improved) version (in Java) and another article breaking down how the algorithm works.

I then went about implementing the algorithm in Python using the Unreal Engine python API for the vector math.

I didn't really have enough time to see if performance could be improved and I'm aware there are some clunky bits of the procedural generation - like 3 nested loops, though I'm not sure this could be avoided. With more time I would have looked into this stuff but I was more concerned with making things work

## Challenges

Having come from a software development background using mostly high level languages like Python, I found the more computer science-y aspects difficult. Implementing an algorithm for procedural generation was very interesting and fun to work on... but ate into a lot of my time as I wanted to make sure I understood how it worked.

Another challenge was just the lack of resource on actually using Python with UE5. The API documentation is extensive but very poor - in that there are little to no examples and often very brief and poor descriptions of what a class or function call does. Due to this, ChatGPT wasn't much help either - from experience it makes up function definitions and class methods with APIs or libraries whenever there is a lack of worked examples on the web. This was very much the case here. The developer forums on unreal engines website also weren't much help in regards to python. 

As a result learning to use the python API through a combination of a few tutorials on the web and some bad chatGPT code was difficult and I did often find myself just searching the API guessing class names or functions that might exist and might do what I want - which was a big time sink.

The engine does not run well on so I was immediately looking for things to scrap from the template project it created for me to speed it up. Even with this I think there was something going on with deleted cubes not being fully deleted as the more work i did, the slower the program got to use. By the end this significantly slowed me down....

## Experience with Unreal Engine

Prior to this I had no experience with unreal engine. This closest would have been Godot, which i have messed around with for a couple of weeks once, doing 2D sprite-based stuff. I did download unity once and start to do a tutorial but I don't think I got far. It was also 2D.

Layouts of all game engines do seem to hae a little crossover in how they look so on initially opening UE5 it was not as intimidating as it might have otherwise been. I know there'd be some hierarchical view of things in the scene, a scene view, an output for logs and a windows for inputting parameters for different objects in the scene.

I was able to find a tutorial showing how to set up a python script in the editor to run it, and how to connect it to a button in a editor utility widget. I think without this tutorial it would have been very difficult to work ou simple stuff like how to "find" my python script in the editor as there were some obtuse plugin settings that needed to be updated before the scripts would appear.

Again, maybe I was looking in the wrong place, but I thought the general engine documentation was pretty poor. Godot has extremely detailed and good documentation - I'm aware though that the complexity in UE5 scales way higher so aiming fo the same level of detail would be extremely challenging but on a whole it feels kind of unwelcoming to new users.

Having said all that, once I could get a script running it was much easier (and more fun!) to learn how to use the engine just by hacking away at things and trying stuff out - as is always the way!

## Limitations

My algorithm doesn't really work as I'd hoped. The ideal outcome would have been to generate some simple voxelised terrain. With more time I probably could have tweaked the code and got there but I just didn't have the time to experiment. With more time I also would have...

- Adding function docstrings
- Added more type checking, error handling and logging
- Maybe refactored the code though there isn't much and I certainly don't think there would be any need to use OOP for this amount of code
- Improved the look of the ui widget
- Had more variables that code be passed in to affect the algorithm/procedural generation

## How to run the project

1. Clone the project and open the project in Unreal Engine 5.3
2. Navigate to File -> Open Level... and select 'test_level'
3. Go to Content Browser -> All/Content/Python -> right click on 'CubeGen' and select 'Run Editor Uility Widget'
4. Once the widget appears, enter some integers for the values (0 < width < 100, 0 < z_depth < 10) and click on 'Generate Cubes'
5. Entering new or the same values and clicking on 'Generate Cubes' will delete the existing cubes and regenerate new cubes


