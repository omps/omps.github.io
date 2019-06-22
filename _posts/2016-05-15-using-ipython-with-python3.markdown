---
layout: post
title: "Using Ipython with Python3"
date: 2016-05-15 13:25:37 +0530
comments: true
categories: python
# publish: false
---

I started to move along with using python 3, and for the sake of using it, wanted my python shell for to be working properly, now you must have been aware, I use ipython for most of my python work, so while I downloaded and installed python3. I was unable to use ipython. The ```pip3 install ipython3``` didn't came of much help. Technicall, I am having two versions of python running on to my system, one is the native python version ```2.7.11``` which by default came with my OS, other python version ```3.5.1``` which I had explicity downloaded for using python3.

Googling around did helped me, and the solution was pretty simple for implementation.

    $ which ipython
    /usr/local/bin/ipython
    $ which python3
    /usr/local/bin/python3
    
    cp /usr/local/bin/ipython /usr/local/bin/ipython3
    
edit the ipython3 file.

```python
#!/usr/local/bin/python

# -*- coding: utf-8 -*-
import re
import sys

from IPython import start_ipython

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(start_ipython())
```


Change the shebang which is ```#!/usr/local/bin/python```  to ```#!/usr/local/bin/python3```

Save the file.

run ipython3, I am assuming ```/usr/local/bin``` is in the system path.

```sh
$ ipython
Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
Type "copyright", "credits" or "license" for more information.

IPython 4.2.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: 
```


What we basically did, was copied the original ipython file which was being used by python version 2 and ensured that to work with python3 by changing its shebang line, which tells ipython to use the desired python version. In case, if you do not already have ipython installed then ```pip install ipython``` will just work, post your python 3 installation.
