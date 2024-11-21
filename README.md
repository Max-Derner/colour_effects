# pyglet

This a a project to develop a Python PyPI package with all the features of [figlet](http://www.figlet.org/) (which is already done in [pyfiglet](https://pypi.org/project/pyfiglet/)). **_BUT_** we're gonna add colour customisation!

So instead of having to stick to boring old regular no colour stuff like this:  
![showing plain figlet](./README_IMGS/plain_figlet.png)

You could have something super cool like this:  
![showing colourful figlet](./README_IMGS/colourful_figlet.png)

We will likely end up using colours from the 8bits ANSI escape codes:  
![ANSI escape codes](./README_IMGS/8bit-colour-ref.png)

# What do?
* Study figlet fonts to learn their secrets 
* Study colour outputting Python libraries to learn their secrets [write-up](./Notes/colour_output.md)
* Study Poetry, because I kinda want to learn how that works and it should ultimately make deploying a PyPI package a little bit easier