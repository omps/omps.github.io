---
layout:     post
title:      "BASH CLI Tips."
subtitle:   "CLI TIPS to get things done faster."
date:       2017-01-27
author:     "Om Prakash Singh"
alias:      ['cli/bash/tips']
header-img: "img/ansible.png"
published: false
---


http://stackoverflow.com/questions/6109225/bash-echoing-the-last-command-run



Bash has built in features to access the last command executed. But that's the last whole command (e.g. the whole case command), not individual simple commands like you originally requested.
'''
!:0 = the name of command executed.

!:1 = the first parameter of the previous command

!:* = all of the parameters of the previous command

!:-1 = the final parameter of the previous command

!! = the previous command line
'''
etc.

So, the simplest answer to the question is, in fact:
'''
echo !!
'''
...alternatively:

echo "Last command run was ["!:0"] with arguments ["!:*"]"
Try it yourself!

echo this is a test
echo !!
In a script, history expansion is turned off by default, you need to enable it with
'''
set -o history -o histexpand
'''
