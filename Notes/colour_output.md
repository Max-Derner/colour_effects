# Colour output! How do?

So, a cursory web search shows a _LOT_ of people talking about the ANSI escape sequences. 

There's mention in [this stack overflow thread](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal) that bloody windows is all problematic and you need to run `os.system('color')` before any colours will work. 

Someone is mentioning using **_TWO_** separate 3rd party libraries for a basic bit of colour!
```python
from colorama import init
from termcolor import colored

init()

print(colored('Hello, World!', 'green', 'on_red'))
```

I seem to be coming across colorama and termcolor again and again and again... (along with ANSI escapes of course).  
Now, I don't really want to be taking on subdependencies for such a simple jobs, so I'm just going see how complicated their secrets are.

* [`colorama`](https://pypi.org/project/colorama/)
* [`termcolour`](https://pypi.org/project/termcolor/)
* [`colored`](https://pypi.org/project/colored/) (an extra one I found that is weirdly on GitLab)

## `termcolor`

Is mindbogglingly simple, there is absolutely nothing to it and the testing is a mix of overcomplicated and questionable albeit comprehensive.  
[termcolor on GitHub](https://github.com/termcolor/termcolor/tree/main/src/termcolor)

Also, `termcolor` just uses ANSI escapes and that's it.

## `colorama`

Seems as though it's only goal is making colours work on Windows. Which honestly just goes to show what a bloated, half backwards, flaming pile of desperate-for-the-bin rubbish Windows is. Nevertheless I guess kids use Windows when they don't know any better and this project is a bit of fun and kids like fun, so I suppose we should learn the secrets...

No thanks, that is wildly complicated. `termcolor` was nothing, this crap genuinely looks like some ancient curse written in runes. Windows is a bit too much for right out the gate. Let's get something working for sensible OSes, we can even throw in a "if Windows `os.system('color')` and just hope for the best. But there is no way in hell I would want to be trying to support Windows like this. To illustrate, try following this function [`just_fix_windows_console()`](https://github.com/tartley/colorama/blob/master/colorama/initialise.py#L72) it looks all cute and dainty and simple, and then it just explodes into a ginormous class that looks to have it's hand up the metaphorical arse of Windows in order to puppeteer it and very clearly knows exactly what parts to touch and not touch.

[colorama on GitHub](https://github.com/tartley/colorama/tree/master/colorama)

## `coloured`

Not a bad package at all, it's got some complexity to it but nowhere near the same scale as `colorama`.

[colored on GitLab](https://gitlab.com/dslackw/colored/-/tree/master/colored?ref_type=heads)

# Conclusion

Everyone uses ANSI, it's just that some systems need a hell of a lot of hand-holding.

Now in terms of subdependencies, I would much rather have none if possible and spaffing out a bunch of ANSI codes is in no way what-so-ever a complicated task. **_But_** I am quite happy to concede that if we want to do cross-platform support for everyone and their Grandmas then we will want to leverage someone elses hard work.