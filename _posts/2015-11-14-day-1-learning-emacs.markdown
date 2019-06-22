---
layout: post
title: "Day 1 - Learn Emacs in 30 days challenge"
date: 2015-11-14 00:02 +0530
category: emacs
author: omps
tags: emacs, 30daychallenge, #day1
comments: true
---

Thank you for your support and encouragement. So here I am writing about my beginning of Day 1: part and working with EMACS.

The below is the content I am planning to touch upon during my 30 Days challenge. The checklist is not in any particular order, but just to remind me of the topics what I need to cover.
<!--more-->
-   [ ] Modes.
-   [ ] IDO Mode
-   [ ] org-mode
    -   [ ] Todo items
    -   [ ] Hyperlinks
    -   [ ] tags, tables
    -   [ ] propertis and columns
    -   [ ] Date and time.
    -   [ ] AGenda views
    -   [ ] Exporting
-   [ ] tramp
-   [X] Running command by the name/ help/ commands for fixing typos. - Day 6
-   [X] Commands for human languages.
-   [ ] Mark and the region / Killing and moving text / Registers
-   [ ] Contrlling the display / Multiple buffers / Multiple windows / frames and graphical display
-   [ ] Search and replacement.
-   [ ] File handelling.
-   [ ] Editing compling, testing and mantaining programs.
-   [ ] Sending mail, reading mail with rmail.
-   [ ] Dired mode.
-   [ ] The calendar and the diary.
-   [ ] Miscellaneous commands
-   [ ] Customization.

Quoting from Emacs Manual
" Emacs is the extensible, customizable, self-documenting real-time display editor."

Emacs is an advanced editor because of its ability to perform complex operations related to OS, by controlling subprocesses, indenting programs automatically, showing multiple files at once and ofcourse we can use it as text editor.
It is also a self-documenting means any time special command for help can be used for finding out what the particular command does.
Emacs can be eaisly altered to behave in certain prefrence and is highly customizable.
Emacs can go beyond simple customisation and can create entirely new commands. These new commands are simple program written in LISP.

#### Downloading<a id="sec-1" name="sec-1"></a>

-   Downloaded Emacs: I downloaded for MAC OS X from <http://emacsformacosx.com/>. I had been suggested by many sites and also from the people on IRC #emacs channel, while you are learning to use emacs, do not start with a customised emacs. I believe it could be mainly because a lot of customisations are already done for you, hence limiting you learning curve. Well, downloading and installing with OS X is pretty simple and straight, I got "Emacs Version 24.3 Universal Binary Released 2013-03-11". Double click on the installer and voilla the installation is completed on the fly.

For windows and Linux you can download GNU Emacs releases from a [nearby GNU mirror](http://ftpmirror.gnu.org/emacs/); or if automatic redirection does not work see the list of [GNU mirrors](http://www.gnu.org/order/ftp.html), or use the main [GNU ftp server](http://ftp.gnu.org/gnu/emacs).

GNU Emacs development is hosted on [savannah.gnu.org](http://savannah.gnu.org/projects/emacs/).

#### Working with emacs<a id="sec-2" name="sec-2"></a>

-   Starting the editor: once downloaded and installed. From the Launchpad -> emacs, clicking on which took me to the editor in its full glory, with a nice welcome message with link to the manual and the beginner emacs tutorials to get a start working with emacs and to quickly get help in emacs "C-h (Hold down Ctrl and Press h)

##### Few things to note and which is global to emacs.<a id="sec-2-1" name="sec-2-1"></a>

Control Key in emacs is denoted as 'C'.
All or Esc Key in emacs is denoted as 'M' or referred in document as meta key.
Shift will be denoted as 'S'.

##### Moving around<a id="sec-2-2" name="sec-2-2"></a>

Most movements in emacs can be controlled using the arrow keys but some still say it is not advisable and use of key sequences controled by Ctrl and Meta keys are advisable. below table helps in understanding the movements with these keys.

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />
</colgroup>
<tbody>
<tr>
<td class="left">Keys</td>
<td class="left">Movement</td>
</tr>


<tr>
<td class="left">C-v</td>
<td class="left">View next screen also as Page Up.</td>
</tr>


<tr>
<td class="left">M-v</td>
<td class="left">Move Backward one screen or Page Down.</td>
</tr>


<tr>
<td class="left">C-l</td>
<td class="left">redisplay the text with cursor at the center of the screen.</td>
</tr>


<tr>
<td class="left">C-p</td>
<td class="left">Previous line or up arrow key.</td>
</tr>


<tr>
<td class="left">C-b</td>
<td class="left">back one character or left arrow key.</td>
</tr>


<tr>
<td class="left">C-f</td>
<td class="left">forward one character or right arrow key.</td>
</tr>


<tr>
<td class="left">C-n</td>
<td class="left">Next line or down arrow key.</td>
</tr>


<tr>
<td class="left">M-f</td>
<td class="left">Move one forward one word.</td>
</tr>


<tr>
<td class="left">M-b</td>
<td class="left">Move back one word.</td>
</tr>


<tr>
<td class="left">C-a</td>
<td class="left">Move to the beginning of the line.</td>
</tr>


<tr>
<td class="left">C-e</td>
<td class="left">Move to the end of the line.</td>
</tr>


<tr>
<td class="left">M-a</td>
<td class="left">Move to the beginning of the sentence.</td>
</tr>


<tr>
<td class="left">M-e</td>
<td class="left">Move to the end of the sentence.</td>
</tr>


<tr>
<td class="left">C-u</td>
<td class="left">to specify a repeat count.</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">C-v and M-v are exceptions as they won't move pages but</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">instead will scroll to that many lines forward/backward</td>
</tr>


<tr>
<td class="left">C-g</td>
<td class="left">Kill the running command in minibffer, or in case emacs</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">stop responding.</td>
</tr>


<tr>
<td class="left">C-d</td>
<td class="left">Delete the next character after the cursor cursor.</td>
</tr>


<tr>
<td class="left">DEL</td>
<td class="left">delete the character just before the cursor.</td>
</tr>


<tr>
<td class="left">Insert</td>
<td class="left">text insertion is as simple as typing it.</td>
</tr>


<tr>
<td class="left">text</td>
<td class="left">you can use the C-u to insert text as well. for eg.</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">C-u 10 - will insert -&#x2014;&#x2014;&#x2014;.</td>
</tr>


<tr>
<td class="left">M-<DEL></td>
<td class="left">Kill the word before the cursor.</td>
</tr>


<tr>
<td class="left">M-d</td>
<td class="left">Kill the word after the cursor</td>
</tr>


<tr>
<td class="left">C-k</td>
<td class="left">Kill from the cursor position to end of line.</td>
</tr>


<tr>
<td class="left">M-k</td>
<td class="left">Kill to the end of current sentence.</td>
</tr>


<tr>
<td class="left">C-<SPC></td>
<td class="left">Set the mark, move aroung with the above keys to highlight</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">the text.</td>
</tr>


<tr>
<td class="left">C-y</td>
<td class="left">Yank the file back.</td>
</tr>


<tr>
<td class="left">C-x C-f</td>
<td class="left">Find file, can be used for creating a file or opening an</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">exitisitng file.</td>
</tr>


<tr>
<td class="left">C-x C-s</td>
<td class="left">Save the file, when you made some changes to the file and</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">want to write the same to disk or save it.</td>
</tr>


<tr>
<td class="left">C-x s</td>
<td class="left">Save some buffers.</td>
</tr>


<tr>
<td class="left">C-x C-b</td>
<td class="left">List all the opened Buffers.</td>
</tr>


<tr>
<td class="left">C-x b</td>
<td class="left">Switch buffer around.</td>
</tr>


<tr>
<td class="left">C-x C-c</td>
<td class="left">Quit Emacs.</td>
</tr>
</tbody>
</table>

These are some of the common keys for moving around while in emacs. It seems its really hard for getting used to it, but as I am working with emacs for sometime, I started to feel it is most obvious to be like that.

I think most of the time as a beginner we could get along with using the arrow keys and we should highly discourage it and use the emacs specific keybindings to move around within emacs. Apart from bringing the emacs on and starting it up, the very important thing we should remeber is how to close it. During my initial days as emacs user I was not aware of quitting emacs, and have of the time ended in killing emacs from the process tree, now I feel so stupid. C-g and C-x C-c are the commands, which can help you all the time, while we are learning. I have heard more advanced user of emacs seldom close their emacs sessions and I may try to forget using C-x C-C again. It may take some time till I get there and stop closing my emacs and I am sure it would be more than 30 days.
