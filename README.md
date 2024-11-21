# pyglet

This a a project to develop a Python PyPI package with all the features of [figlet](http://www.figlet.org/) (which is already done in [pyfiglet](https://pypi.org/project/pyfiglet/)). **_BUT_** we're gonna add colour customisation!

So instead of having to stick to boring old regular no colour stuff like this:  
![showing plain figlet](./README_IMGS/plain_figlet.png)

You could have something super cool like this:  
![showing colourful figlet](./README_IMGS/colourful_figlet.png)

We will likely end up using colours from the [8bit ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code):  
![ANSI escape codes](./README_IMGS/8bit-colour-ref.png)

# What do?
* Study figlet fonts to learn their secrets [write-up](./Notes/figlet.md)
* Study colour outputting Python libraries to learn their secrets [write-up](./Notes/colour_output.md)
* Study Poetry, because I kinda want to learn how that works and it should ultimately make deploying a PyPI package a little bit easier

# Change of requirements

Right, get this. What if instead of trying to integrate colours into figlet and releasing that as a project. We just create a project that can do fun colour stuff. So I'm thinking you'd have:
* an object you can use to describe a general style and then apply that style to some text [POC](./POCs/ansi_codes.py)
* an interactive app that lets you create a file you can cat out that will have colours in it

...and that would probably be about it

I'll get to creating a bit of a POC for us

# Max prog
\- 21st Nov  
I've started some POCs but it's only in 4bit colour. would be pretty sweet to expand it to 8bit. There's two varieties of working out colours, my [first pass](./POCs/ansi_codes.py) was alright but it's proper verbose. [Second pass](./POCs/bansi_codes.py) just feels right but it doesn't play properly with the way I've set up that compile ansi code function, so I might look at trying to swap that so it just takes a whole tonne of styles and it's up to you to not pass multiple foreground colours or background colours or whatever.

# Angles idea
So, right now there's a way to do gradients that are vertical. If we can figure out a way to represent the colours in a list separate to the text. Then to do angles we just shift the colours in a given direction. To define the angle, we can ask for a number between 0 and 1, then divide 1 by that number to give how many lines we should skip before shifting the colours. 

So, an angle of 0.5 gives 2 lines together, then shift all the next lines by 1, then 2 more lines and shift all the next lines by 1 again.