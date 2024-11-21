# Figlet! What be?

Obviously figlet exists as a stand along CLI app, I've already mentioned that.

So, I've had a brief look over [`pyfiglet`](https://github.com/pwaller/pyfiglet/blob/main/pyfiglet/__init__.py) and my god. The whole fucking thing is just done in one massive `__init__.py` file. **1,036** lines of the thing! No thank you, who the hell couldn't be arsed to split that out?

Anyway, if it's only 1,000 lines _and they've managed to capture the entirety of figlet's options then this stuff can't be too complicated.

I've also looked through some actual figlet fonts. My favourite font (so far) is alligator and looking through the file it basically seems to be the ASCIIbet in order. Take for example this letter 'C':
```
      ::::::::$@
    :+:    :+:$@
   +:+      $  @
  +#+      $   @
 +#+      $    @
#+#    #+#$    @
########$      @@
```

Which Figlet renders as so:
```
      :::::::: 
    :+:    :+: 
   +:+         
  +#+          
 +#+           
#+#    #+#     
######## 
```

It seems as though th '@' symbols are used to demarcate which lines belong to each letter, and the '$' are used to signify kerning boundaries. If we give figlet 'CC' to render, we can see how closely it places the letters meaning there is some fancy kerning going on and I reckon it is the '$' symbol.

```
      ::::::::  :::::::: 
    :+:    :+::+:    :+: 
   +:+       +:+         
  +#+       +#+          
 +#+       +#+           
#+#    #+##+#    #+#     
########  ########  
```

## colours

It also turns out that pyfiglet allows you to do colours, just not on the level that I wanted to do them.

# Conclusion

Implementing a figlet doo-dad from scratch will be a big deal and just slapping colour over the top of pyfiglet is stupid, we should just contribute to pyfiglet instead if we want to get crazy with it to the extent I want to get crazy with it...  
I feel a change of requirements coming on!

