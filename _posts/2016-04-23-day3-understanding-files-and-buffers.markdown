---
layout: post
title: "Day 3 - Understanding Files and Buffers"
date: 2015-11-23 20:06:40 +0530
comments: true
categories: emacs
tags: #emacs, #30daychallenge, #day3
---
# The windows and the buffer.<a id="sec-1" name="sec-1"></a>

I will touch upon one new topic and what I learned today. While writing my [Day 2](http://www.omps.in/blog/2015/11/14/day-2-the-real-estate/) article I learnt intersting usage of windows and frames (well, the one where we do our editing and writing stuff. It would be good to understand how opening emacs creates the frame and window within.) 
<!--more-->
We start emacs the same way we start our other application. (on Linux, by typing on the terminal window; on Windows and Mac, clicking on to the application icon.) When emacs starts up it usually display a special buffer name **GNU Emacs**. This contains information about emacs and links to common good stuff for begineers(in later days we will figure out how we can skip this)

It is good not to start multiple emacs session, instead just start once and do all the editing in the same sessions. In this way the emacs context accumlates valuable context, such as kill ring, registers, undo history, which helps a lot at advanced stages.

## Buffer<a id="sec-1-1" name="sec-1-1"></a>

The text we are going to edit in emacs is called as buffers and is used to hold the files text. So everytime we visit a file, run dired, send message with 'C-x m' or ask for help, a buffer is used for holding the text of the message.

### Creating and selecting buffers<a id="sec-1-1-1" name="sec-1-1-1"></a>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Command Keybinding</th>
<th scope="col" class="left">Command</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">C-x b BUFFER</td>
<td class="left">switch-to-buffer</td>
<td class="left">select of create a buffer</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">named BUFFER.</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">C-x 4 b BUFFER</td>
<td class="left">switch-to-buffer-other-window</td>
<td class="left">slect BUFFER in other</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">window.</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">C-x 5 b BUFFER</td>
<td class="left">switch-to-buffer-other-frame</td>
<td class="left">select BUFFER in other</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">frame.</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">C-x <LEFT></td>
<td class="left">previous-buffer</td>
<td class="left">select the previous buffer</td>
</tr>


<tr>
<td class="left">C-x <RIGHT></td>
<td class="left">next-buffer</td>
<td class="left">select the next buffer</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">C-u M-g M-g</td>
<td class="left">&#xa0;</td>
<td class="left">read num N and move to line N</td>
</tr>


<tr>
<td class="left">C-u M-g g</td>
<td class="left">&#xa0;</td>
<td class="left">in the most recent buffer</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">other than current</td>
</tr>
</tbody>
</table>

### Listing Buffers<a id="sec-1-1-2" name="sec-1-1-2"></a>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Command Keybinding</th>
<th scope="col" class="left">Command</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">C-x C-b</td>
<td class="left">list-buffer</td>
<td class="left">List the exisitng buffers</td>
</tr>
</tbody>
</table>

Here is an example of a buffer list:

CRM Buffer                Size  Mode              File
. \* .emacs                3294  Emacs-Lisp        ~/.emacs
 %  **Help**                 101  Help
    search.c             86055  C                 ~/cvs/emacs/src/search.c
 %  src                  20959  Dired by name     ~/cvs/emacs/src/
-   **mail**                  42  Mail

%  HELLO                 1607  Fundamental       ~/cvs/emacs/etc/HELLO
%  NEWS                481184  Outline           ~/cvs/emacs/etc/NEWS
   **scratch**              191  Lisp Interaction
-   **Messages**            1554  Fundamental

\`.' in the first field indicates that this is the current buffer.  
\`%' indicates a read-only buffer.  
\`\*' indicates that the buffer is "modified". 

The buffer \`\*Help\*' was made by a help request (\*note Help::); it is not visiting any file. 
The buffer \`src' was made by Dired on the directory \`~/cvs/emacs/src/'. 

### Killing<a id="sec-1-1-3" name="sec-1-1-3"></a>

The buffers can simply be done by just pressing C-x k BUFFER or in the C-x C-b we can select the buffer by pressing k and then exectue it.

## Windows<a id="sec-1-2" name="sec-1-2"></a>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Key Bindings</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">'C-x 2'</td>
<td class="left">To split the windows into 2 one above the another.</td>
</tr>


<tr>
<td class="left">'C-x 3'</td>
<td class="left">Split the windows side by side.</td>
</tr>


<tr>
<td class="left">'C-x o'</td>
<td class="left">to move around windows, or click in the window with the mouse click to have the focus on that window.</td>
</tr>


<tr>
<td class="left">'C-M-v'</td>
<td class="left">Scroll the next window.</td>
</tr>


<tr>
<td class="left">'C-x 0'</td>
<td class="left">Delete the selected window</td>
</tr>


<tr>
<td class="left">'C-x 1'</td>
<td class="left">Delete all windows except the select one.</td>
</tr>


<tr>
<td class="left">'C-x 4 0'</td>
<td class="left">Delete the selected window and kill the buffer showing in that window.</td>
</tr>


<tr>
<td class="left">'C-x ^'</td>
<td class="left">Make selected window taller.</td>
</tr>


<tr>
<td class="left">'C-x }'</td>
<td class="left">Make selected window wider</td>
</tr>


<tr>
<td class="left">'C-x {'</td>
<td class="left">Make selected window narrower</td>
</tr>


<tr>
<td class="left">'C-x -'</td>
<td class="left">Shrink window if buffer dont need so many lines.</td>
</tr>


<tr>
<td class="left">'C-x +'</td>
<td class="left">Make all window same height.</td>
</tr>
</tbody>
</table>
