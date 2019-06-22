---
layout: post
title: "Day 4 - Editing"
date: 2015-11-28 20:15:36 +0530
comments: true
categories: emacs
tags: #emacs, #30daychallenge, #day4
---

I am  becoming such an inconsistent learner and writer and have been not being able to post any new learnings a from last 4 days for emacs, but sometimes the work just take over us and do not allow any bandwidth, this really could be a lame excuse, but my sincerely I should be keeping my posts regular.
<!--more-->
Again, it's more the like learning from your (in this case my) mistakes and going through your work again and again it's a way of reorganising your work and fixing it wherever necessary, I would also need help to understanding the mistakes we should avoid overlooking while technical writing or a posting on a blog.

## What new there could be there inserting text, believe me, emacs is pandora box for writers and enthusiasts.

There is so much written in the #emacs manual ```C-h r```, and this time it was the keys ```C-q``` or ```C-x 8``` this is used to print literals or Unicode characters by specifying their Hex or octal code. For eg, we have a key on keyboard as 'Del' which is used to delete the character  on the point and move backward(from right to left, when the text displays from left to right or otherwise in case text being displayed the other way). The C-q combination when pressed will make the delete key type type the literal 'DEL' instead of acting as text eraser, and the same goes for RET, when you press RET(RETURN or ENTER on some keyboard) we get RET as the literal. But really I want to insert a blank line could it be C-\n (new line character), well that is going to be a cryptic I am sure emacs doesn't treat it's commands this way and I can simply press **C-o** and similarly **C-x C-o** delete all but the last blank line, good gracious I was too fed up with doing C-k to delete my empty lines :) and similarly **C-j** is for entering a new line. 

I want to count the no of words in my selected region or in the buffer, M-= and C-u M-= comes to the rescue. The latter would count the no. of words in the buffer. The command C-x = would do the display the information for my cursor position. Quoting from the emacs manual.

We can also move around the buffer with providing the numeric argument, the most simpler is to use the 'Meta' command with the no. The keys M-1, M-2 as well as M&#x2013; are bound to commands (digit-argument and negative-argument) and set up argument for the next command.

For example I want to go down by 5 lines

M-5 C-n


I was just wondering now what if I want to write 5 o's in line, well thats another question to worry why I would like to do, but how to do in Emacs, and well M-5 0 C-n is not going to do this(i.e. insert 5 0 and go to next line). So, to achieve this  press **M-5 C-u 0** does the trick. We now know there is another way of inserting a *Numeric Argument* and that is using **C-u**, but when type alone it does have its own special meaning of 4 characters. 'C-u C-u C-f' will move you 16 characters, 'C-u C-u C-o' will make a lot of blank lines, and C-u C-k will kill 4 lines. :)

It would be good to know that emacs is powerful to repeat commands as well, the way it worked in Shell, but I think its pretty ahead of its time, and in one command itself you can ensure you can repeat the command as many times as you want. The trick is to use **C-x z**, if I have used a command 'C-u 2 0 C-d' to delete 20 characters, we can repeat this same command using 'C-x z' and insert 'z' as many times you want to run the previous command. cool. For deleting 100 chars I may need to write like 'C-x z z z z z' should remove 100 characters. *Note: this command will not change the arguments in the previous command*

So we checked out the below in commands today.

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Commands</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">C-h r</td>
<td class="left">emacs manual</td>
</tr>


<tr>
<td class="left">C-q</td>
<td class="left">insert literals</td>
</tr>


<tr>
<td class="left">C-x 8</td>
<td class="left">same as above</td>
</tr>


<tr>
<td class="left">C-o</td>
<td class="left">insert blank line</td>
</tr>


<tr>
<td class="left">C-j</td>
<td class="left">insert new line</td>
</tr>


<tr>
<td class="left">C-x C-o</td>
<td class="left">Kill all but the last blank line</td>
</tr>


<tr>
<td class="left">M-=</td>
<td class="left">Count the no. of lines and characters and wordsin buffer</td>
</tr>


<tr>
<td class="left">C-u M-=</td>
<td class="left">same as above except no. of words</td>
</tr>


<tr>
<td class="left">C-x =</td>
<td class="left">cursor postion.</td>
</tr>


<tr>
<td class="left">M--</td>
<td class="left">Bound to digit argumenst such as M-1, M-2</td>
</tr>


<tr>
<td class="left">C-x z</td>
<td class="left">Repeat the previous command. no. of z will repeat the no. of times</td>
</tr>
</tbody>
</table>
