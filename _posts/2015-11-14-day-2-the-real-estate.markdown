---
layout: post
title: Day 2 - The Emacs Real estate
date: 2015-11-14 00:31
category: emacs
tags: #emacs, #day2, #30daychallenge
---
#### The Emacs Real estate.

This is about the screen organization of emacs, how the text is placed and how the screen is drawn for the editor, this is about telling you how the things in #emacs as they are, and why they are important this way. Though, i should have started understanding it and writng it down on Day 1, but understanding the key contol is equally important to me, if I did not had learned about it, I surely would have faced difficulty closing my emacs <!--more-->and moving around. Now let me just try to see how much I  am understanding about the screen here and how well I can put it in my words. :) ofcourse it is not a tech doc, but this my 30 Days challenege to learn more about emacs and understand emacs for good.

I would be mainly using a lot of images compared to lot of writing that, understanding the screen can better be understood by rightly poining to the correct area.

##### The Screen

Double clicking on the emacs icon does open up a GUI window and similarly typing it on command prompt from withing an X Windows system, I get the emacs as an editor with full flesh and bones, i actually means as an GUI application, like we see for other editors. And when  I do same while I am  on the command prompt with no X support, or with -nw or -t (with emacsclient, will write more about this in coming days.) i get the emacs taking up my entire terminal screen. We will call these frames and emace behaves almost similar in both these frames. It normally starts with just one frame, but many frames can be created. 

Each frame consist of several distinct regions. as shown in the picture below.

The emacs frame consist of these important segments

###### Point: Where editing takes place

The place where the cusrsor is present is called as the point in a multiple windows emacs in GUI, the point can be moved by clicking the mouse in the respective region, the active window will have the curson as solid block and will appear to be on the cursor. While working with several buffers each buffer has its own valur for point.

###### Echo area: Where the commands and messages appear at bottom of the frame.

if you pause for more than a second in the middle of the command, you can see your commands being echoed in the echo area. it also shows you the error message when the command fails. The messages displayed in the echo area are generally saved in the special buffer calles as **Messages**

###### Mode Line: Understanding the mode line.

At the bottom of every window there is a mode line. 
The text displayed on the mode line has the following format
cs:ch-fr buf        pos line (major minor)

o cs  display the character set. 

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />
</colgroup>
<tbody>
<tr>
<td class="left">'-'</td>
<td class="left">implicate no special character set.  see [Coding System](http://www.gnu.org/software/emacs/manual/html_mono/emacs.html#Coding-Systems)</td>
</tr>


<tr>
<td class="left">'='</td>
<td class="left">means no coversion, and used for files with no textual data</td>
</tr>


<tr>
<td class="left">'1'</td>
<td class="left">ISO Latin-1, other characters represent various coding system</td>
</tr>
</tbody>
</table>

o ch   this usually show 2 dashes 

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />
</colgroup>
<tbody>
<tr>
<td class="left">(&#x2013;)</td>
<td class="left">if the buffer is unmodified.</td>
</tr>


<tr>
<td class="left">(\*\*)</td>
<td class="left">if the buffer is modified.</td>
</tr>


<tr>
<td class="left">'%\*'</td>
<td class="left">for read only buffer if modified.</td>
</tr>


<tr>
<td class="left">'%%'</td>
<td class="left">otherwise, i.e read only buffer and not modified.</td>
</tr>


<tr>
<td class="left">'-'</td>
<td class="left">displayed after ch, if the directory is local.</td>
</tr>


<tr>
<td class="left">'@'</td>
<td class="left">if the directory if buffer is on remote macine is shows @.</td>
</tr>
</tbody>
</table>

o fr   is the selected frame name, default is F1

o buf   usually the name of the file or the buffer.

o pos   where there is additional text above the top of the window or below the bottom.

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />
</colgroup>
<tbody>
<tr>
<td class="left">All</td>
<td class="left">In case of small buffer and everything visible on screen</td>
</tr>


<tr>
<td class="left">Top</td>
<td class="left">If you are at the beginning of the buffer</td>
</tr>


<tr>
<td class="left">Bot</td>
<td class="left">If you are at the bottom of the buffer</td>
</tr>


<tr>
<td class="left">nn%</td>
<td class="left">nn is the percentage of buffer above the window</td>
</tr>
</tbody>
</table>

o line   'L' Followed by the line no. at point.

o major   Name of the major mode used in buffer, for eg. Text mode, Lisp Mode, Org Mode and so on. 

o minor   minor mode are the list of enabled minor modes on top of major mode, for eg visual-line-mode, flyspell-mode

###### The Menu Bar - How to use.

On the graphical display you can just use the mouse to open the menu bar, an arrow to the right of the menu denotes the menu having a sub menu. Many commands in menu bar have ordinary key bindings as well. 

On a text terminal menu bar can be opened using 'M-\`' or <F10>, or run the command tmm-menubar. Move around the menu bar using up and down arrow key, <RET> i.e enter key, to select the item or C-g to come out of the menu bar mode.

I know its been a little late today, but I was quite able to give time one weekends than as on weekdays, I just don't want to loose focus so am trying to keep up with my posts daily, hope these should be helpful, and I am seriously looking forward for your comments and suggestion, so do please keep posting, tomorrow I think I will go more about buffers and frames.

All in all I am enjoying and learning so many things while posting and writing.
