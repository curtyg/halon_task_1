# halon_task_1 - procedural generation

## Approach and Thought Process

I chose to do Task 1 due to having an interest in procedural generation having previously watched some GDC talks on the topic.

I did not, however, have any experience coding an algorithm for procedural generation. Task 2 or 4 might have made more sense seeing as I actually had experience with the algorithms these were displaying (although this experience was brief, only in my university degree 6-7 years ago...) but I knew I would find it fun and interesting to attempt procedural generation so I made the perhaps ill-fated decision of going with it!

I also decided early on I would attempt to do the task mainly utilising python, as its the programming language I have used most to date and I had seen that the Unreal python API was quite extensive so figured I would not be too limited with it, especially considering the scope of the tasks involved. I wasn't sure about any sort of 'animating' and whether I could do that with python but never had to cross that road as I chose task 1.

Initially I knew there would be some things I would need to learn regardless of what task I chose, so I had a series of small tasks to begin with which included but were not limited to:

- Downloading an setting up UE5.3 for the first time
- Understanding the terms used for objects in the engine (e.g. Actors etc.)
- Rendering a single cube to a scene
- Delete a cube from the scene
- Learning how to create a Editor UI component for my python script

## Computer Science principles applied

Having decided on doing Task 1 I knew i would have to decide on an algorithm to use. There seemed to be a number of resources online discussing procedural generation, including a wiki dedicated to it and the different techniques. At some point I decided on using Perlin noise - purely because I could find both Ken Perlin's original version (in Java) and another article breaking down how the algorithm works using a Javascript version

I then went about implementing the algorithm in Python using the Unreal Engine python API for the vector math.

I didn't really have enough time to see if performance could be improved and I'm aware there are some clunky bits of the procedural generation - like 3 nested loops, though I'm not sure this could be avoided. With more time I would have looked into this stuff but I was more concerned with making things work

## Challenges

Having come from a software development background using mostly high level languages like Python, I found the more computer science-y aspects difficult. Implementing an algorithm for procedural generation was very interesting and fun to work on... but ate into a lot of my time as I wanted to make sure I understood how it worked.

Another challenge was just the lack of resource on actually using Python with UE5. The API documentation is extensive but very poor - in that there are little to no examples and often very brief and poor descriptions of what a class or function call does. Due to this, ChatGPT wasn't much help either - from experience it makes up function definitions and class methods with APIs or libraries whenever there is a lack of worked examples on the web. This was very much the case here. The developer forums on unreal engines website also weren't much help in regards to python. 

As a result learning to use the python API through a combination of a few tutorials on the web and some bad chatGPT code was difficult and I did often find myself just searching the API guessing class names or functions that might exist and might do what I want - which was a big time sink

## Experience with Unreal Engine

Prior to this I had no experience with unreal engine. This closest would have been Godot, which i have messed around with for a couple of weeks once, doing 2D sprite-based stuff. I did download unity once and start to do a tutorial but I don't think I got far. It was also 2D.

Layouts of all game engines do seem to hae a little crossover in how they look so on initially opening UE5 it was not as intimidating as it might have otherwise been. I know there'd be some hierarchical view of things in the scene, a scene view, an output for logs and a windows for inputting parameters for different objects in the scene.

It doesn't run too well on my personal laptop so I was immediately looking for things to scrap from the template project it created for me to speed it up. 

I was able to find a tutorial showing how to set up a python script in the editor to run it, and how to connect it to a button in a editor utility widget. I think without this tutorial it would have been very difficult to work out how to even "find" my python script in the editor as there were some obtuse plugin settings that needed to be updated before the scripts would appear.

Again, maybe I was looking in the wrong place, but I thought the general engine documentation was pretty poor. Godot has extremely detailed and good documentation - I'm aware though that the complexity in UE5 scales way higher so aiming fo the same level of detail would be extremely challenging but on a whole it feels kind of unwelcoming to new users.

Having said all that, once I could get a script running it was much easier (and more fun!) to learn how to use the engine just by hacking away at things and trying stuff out - as is always the way!

## How to run the project