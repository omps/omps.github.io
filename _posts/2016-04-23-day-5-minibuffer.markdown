---
layout: post
title: "Day 5 - Minibuffer"
date: 2015-12-03 20:33:04 +0530
comments: true
categories: emacs
tags: #emacs, #day5, #30daychallenge
---

Emacs have a minibuffer, and called the same because of its small screen space, the minibuffer resides in the same area as echo area so many time when any error or informative message appear in the echo area, it just hides the minibuffer for a few seconds or till the time any new keypress is made. <!--more-->

Minibuffer can be activated using typing text to it, and exited by typing **<RET>** (execute the command) or **C-g** (cancel the command). The minibuffer prompt shows the default arguments suppose the commands that read buffer names usually show buffer name as the default and can be activated using **<RET>**

When finding a file in emacs, for opening or creating one, the minibuffer usually open the default dir, the default directory is stored in buffer-local variable as 'default-directory', now whenever emacs will read a filename using a minibuffer it will insert the directory name of the file being opened.

Emacs interpret '~/' as your home directory. you can specify something like this in case you do not want to type the complete path from where you want your files to be opened / created. 

The minibuffer in emacs is also a buffer and the usual emacs commands are available for editing. **<RET>** in the minibuffer submits the argument and the same cannot be used to insert a new line and can be done with **C-q C-j** and **C-o**. The keys <TAB>, <SPC>, and ? are bound to completion of the commands. 

When the minibuffer is active, the echo area is treated like an ordinary Emacs window. 

Minibuffer uses a feature called as completion these(<TAB>, <RET> and <SPC>) commands attempt to complete the text in the minibuffer, '?' usually provide a list of possible completions. These commands work by narrowing down a large list of to a smaller subsets of matches. Emacs perform completion using one or more of the below *Completion Styles*.

The variable  <span class="underline">completion styles</span> specify the completion style to use.

From the Emacs Manual:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />
</colgroup>
<tbody>
<tr>
<td class="left">basic</td>
<td class="left">A matching completion alternative must have the same beginning as</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">the text in the minibuffer before point.  Furthermore, if there is</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">any text in the minibuffer after point, the rest of the completion</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">alternative must contain that text as a substring.</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
</tr>


<tr>
<td class="left">partial-completions</td>
<td class="left">This aggressive completion style divides the minibuffer text into</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">words separated by hyphens or spaces, and completes each word</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">separately. a \* in the minibuffer is treated as a wildcard and matches</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">any character at the corresponding position.</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
</tr>


<tr>
<td class="left">emacs22</td>
<td class="left">this is similar to basic, except it ignores the text in minibuffer after the</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">point.</td>
</tr>
</tbody>
</table>

Below additional completions are also defined, and can be used in **completion-styles** 

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />
</colgroup>
<tbody>
<tr>
<td class="left">substring</td>
<td class="left">A completion alternative must contain the text in the minibuffer before point., and</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">text after point, as substrings.</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
</tr>


<tr>
<td class="left">initials</td>
<td class="left">the very agressive completions style attempts to complete acronyms and initalisms</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
</tr>


<tr>
<td class="left">emacs21</td>
<td class="left">a very simple completion style, if the text in minibuffer is foobar, only matches</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">starting with foobar is considered.</td>
</tr>
</tbody>
</table>

M-x uses the minibuffer to read the name of a command, so completion works by matching the minibuffer text with available emacs commands.

THe commands for completion works as defined in the minibuffer when the completion is allowed.

**<TAB>**     complete as much as possible; if unable to complete display a list of possible completions (minibuffer-complete) 

**<SPC>**     Completes up to one word. (minibuffer-complete-word)

**<RET>**     Submit the minibuffer text as argument. (minibuffer-complete-and-exit)

**?**         Display list of completions. (minibuffer-complete-help)

**Mouse-1**   Clicking mouse button 1 or 2 on a completion alternative chooses it
**Mouse-2**   (mouse-choose-completion).

**M-v**       Selects the window showing the completion list. (switch-to-completion)
**<PageUp>**  and then we can use the below pageup and prior commands.
**<prior>**

**<Right>**    (next-completion) this moves to point following alternatives.

**<Left>**    (previous-completion) this moves to previous alternatives.

There are many modes in emacs which let you do so many things with the minibuffer, some noted ones are ido-mode and helm-mode.

Ido mode is part of the emacs from version 22.

I will cover these modes in my later learnings, and keep updating.
