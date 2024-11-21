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