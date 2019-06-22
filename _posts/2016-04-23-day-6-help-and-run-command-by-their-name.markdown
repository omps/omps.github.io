---
layout: post
title: "Day 6 - Help and Run command by their name"
date: 2015-12-13 21:09:38 +0530
comments: true
categories: emacs
tags: #emacs, #day6, #30daychallenge
---

Sixth day of writing my content, I had never thought i would be even writing for this many posts continuously(I am kind of a lazy writer) and I realize this experience of writing blogs and sharing my learnings or acquired knowledge is actually encouraging. I started to think that if I am able to put some extra time and effort, I may also complete a lot of things by taking similar challenegs. <!--more-->My priority ones are loosing weight(I am still finding myself in tough situation on to get myself motivated) and learning the python programming language, which as I had been told is pretty easy to learning. I may get inconsistent at times due to other priorities coming up, but writing my learnings and posting everyday keeps me motivated and keep reminiding me I have pending stuff to do.

Every emacs command has a name which can be used against the convenient key bindings. Most emacs commands doesn't have key bindings so the only way to learn them is to use them as commands, by emacs convention all the command will consist one or more words separated  by '-'. For eg. auto-fill-mode or manual-entry. So to enter a command, type M-x enter the command name RET (to execute), C-g (to cancel). Its something similar to what we discussed in our Day 5, to enter the mini-buffer run the command and execute it and it does work similar for completion as it is to be done in mini-buffer.

well there are many things which we need immediately and overlook to take the effort to read the manual, or say for LISP errors which we might not be aware of, the freenode.org IRC network's #emacs channel is the best place after failed attempt of finding any help on google and emacswiki.org. but again at the same time emacs itself has a very awesome online documentation for reference. Online means it is accessible within emacs all the time. The help commands are easily accessible with 'C-h' help character, after this we usually put the character for which we are seeking help and can be canceled the same way as all the mini-buffers. 'C-h' itself a help option, so typing 'C-h C-h' will print the available help characters. Apart from C-h, F1 can also  be used. I have put some simple stuff about how to ask help in Emacs at <<a id="put-the-link-here" name="put-the-link-here"></a>. A more detailed list s below.

Similarly apropos are the commands which may answer certain questions as "what are the commands for working with files?". specifying a apropos pattern such as a word, a list of words, or regular expressions, each apropos command display a list of item that matches the pattern in a separate window.

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
<td class="left">C-h a *TOPICS*</td>
<td class="left">Searched for the command whose name matches the arguments</td>
</tr>


<tr>
<td class="left">C-h i d m *emacs* RET i *TOPIC* RET</td>
<td class="left">This searches for the topic in the indices of online emacs manual, and prints the first match</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">',' to jump to the subsequent matches, we can also use regexes here.</td>
</tr>


<tr>
<td class="left">C-h i d m *emacs* RET s *TOPIC* RET</td>
<td class="left">Same as above, but instead of just searching the indices, it searches the manual too.</td>
</tr>


<tr>
<td class="left">C-h C-f</td>
<td class="left">Displays the FAQ.</td>
</tr>


<tr>
<td class="left">C-h p</td>
<td class="left">Display all the emacs package based on the keywords.</td>
</tr>


<tr>
<td class="left">C-h b</td>
<td class="left">Display all active key bindings</td>
</tr>


<tr>
<td class="left">C-h c *key*</td>
<td class="left">show the name of the command it runs. (describe-key-briefly)</td>
</tr>


<tr>
<td class="left">C-h d *TOPICS* RET</td>
<td class="left">Display command and variables whose documentation matches topic. (aprops-documentation)</td>
</tr>


<tr>
<td class="left">C-h e</td>
<td class="left">Display **Message** Buffer</td>
</tr>


<tr>
<td class="left">C-h f *function* RET</td>
<td class="left">Display documentation on the LISP function (describe-function)</td>
</tr>


<tr>
<td class="left">C-h h</td>
<td class="left">Display the 'HELLO' file</td>
</tr>


<tr>
<td class="left">C-h i</td>
<td class="left">Run info, the GNU documentation browser, the complete emacs document is available online in info</td>
</tr>


<tr>
<td class="left">C-h key</td>
<td class="left">Display the name and the documentation of the command that the key runs. (describe-key)</td>
</tr>


<tr>
<td class="left">C-h l</td>
<td class="left">Description of last 300 keystrokes. (view-lossage)</td>
</tr>


<tr>
<td class="left">C-h f</td>
<td class="left">Display docuemntation of the current major mode. (describe-mode)</td>
</tr>


<tr>
<td class="left">C-h n</td>
<td class="left">Display news of recent changes. (view-emacs-news)</td>
</tr>


<tr>
<td class="left">C-h p</td>
<td class="left">find packages by topic keyword. ((finder-by-keyword)</td>
</tr>


<tr>
<td class="left">C-h r</td>
<td class="left">Display the emacs manual. (info-emacs-manual)</td>
</tr>


<tr>
<td class="left">C-h s</td>
<td class="left">Display the current contents of the syntax table, with explanation of what they mean</td>
</tr>


<tr>
<td class="left">&#xa0;</td>
<td class="left">(describe-syntax)</td>
</tr>


<tr>
<td class="left">C-h t</td>
<td class="left">enter the emacs interactive tutorial. (help-with-tutorial)</td>
</tr>


<tr>
<td class="left">C-h v *var* RET</td>
<td class="left">Display the doc for the LISP variable var. (describe-variable).</td>
</tr>


<tr>
<td class="left">C-h w *command* RET</td>
<td class="left">Show which keys run the command named command. (where-is)</td>
</tr>


<tr>
<td class="left">C-h C *coding* RET</td>
<td class="left">Describe the coding system. (describe-coding-system)</td>
</tr>


<tr>
<td class="left">C-h C RET</td>
<td class="left">Describe the coding system current in use.</td>
</tr>


<tr>
<td class="left">C-h F *COMMAND* RET</td>
<td class="left">Enter Info and go to node that documents emacs command *command*. (info-goto-emacs-command-node)</td>
</tr>


<tr>
<td class="left">C-h I *method* RET</td>
<td class="left">Describe the input *method*. (describe-input-method)</td>
</tr>


<tr>
<td class="left">C-h K *key*</td>
<td class="left">go to the key-sequence document in Info. (Infp-goto-emacs-key-command-node)</td>
</tr>


<tr>
<td class="left">C-h L *Language-env* RET</td>
<td class="left">Display info on the character set, coding system and input methods. (describe-language-environment)</td>
</tr>


<tr>
<td class="left">C-h S *Symbol* RET</td>
<td class="left">Display the info on the symbol *symbol* based on the programming mode you are using (info-lookup-symbol)</td>
</tr>


<tr>
<td class="left">C-h .</td>
<td class="left">Display message for the special text area. (display-local-help)</td>
</tr>


<tr>
<td class="left">**Apropos**</td>
<td class="left">&#xa0;</td>
</tr>


<tr>
<td class="left">C-h a *pattern* RET</td>
<td class="left">Search for command whose names matches the pattern.</td>
</tr>


<tr>
<td class="left">M-x apropos RET *pattern* RET</td>
<td class="left">Search for functions(both interactive and non-interactive) and variables whose name matches the *pattern*</td>
</tr>


<tr>
<td class="left">M-x apropos-variable RET *pattern* RET</td>
<td class="left">Search for a user-option variables matching the *pattern*.</td>
</tr>


<tr>
<td class="left">M-x apropos-value RET *pattern* RET</td>
<td class="left">search for function whose definition match *pattern* and variable whose value matches *pattern*</td>
</tr>


<tr>
<td class="left">C-h d *pattern* RET</td>
<td class="left">search for function and variable whose documentation string matches *pattern*</td>
</tr>


<tr>
<td class="left">**Emacs help files**</td>
<td class="left">&#xa0;</td>
</tr>


<tr>
<td class="left">C-h C-c</td>
<td class="left">Describe the emacs copying condition. rules for copying and redistributing emacs. (describe-copying)</td>
</tr>


<tr>
<td class="left">C-h C-d</td>
<td class="left">Debugging in emacs. (view-emacs-debugging)</td>
</tr>


<tr>
<td class="left">C-h g</td>
<td class="left">Display general information about GNU Project. (describe-gnu-project)</td>
</tr>


<tr>
<td class="left">C-h C-m</td>
<td class="left">How to order printed copies. (view-order-manual)</td>
</tr>


<tr>
<td class="left">C-h C-n</td>
<td class="left">To see the emacs news and listing of new features. (view-emacs-news)</td>
</tr>


<tr>
<td class="left">C-h C-o</td>
<td class="left">How to get new version. (describe-distribution)</td>
</tr>


<tr>
<td class="left">C-h C-p</td>
<td class="left">Tells us about the known emacs problems. (view-emacs-problems)</td>
</tr>


<tr>
<td class="left">C-h C-t</td>
<td class="left">Display the emacs TODO list, or things that needs to be done. (view-emacs-todo)</td>
</tr>


<tr>
<td class="left">C-h C-w</td>
<td class="left">Describe warranty. (describe-no-warranty)</td>
</tr>


<tr>
<td class="left">**Commands work in Help mode**</td>
<td class="left">&#xa0;</td>
</tr>


<tr>
<td class="left">SPC</td>
<td class="left">Scroll forward</td>
</tr>


<tr>
<td class="left">DEL</td>
<td class="left">Scroll backard</td>
</tr>


<tr>
<td class="left">TAB</td>
<td class="left">Move point forward to next cross refrence</td>
</tr>


<tr>
<td class="left">S-TAB</td>
<td class="left">Move point backward to previous reference</td>
</tr>


<tr>
<td class="left">RET</td>
<td class="left">Follow a cross refrence point.</td>
</tr>


<tr>
<td class="left">C-c C-c</td>
<td class="left">Show all documents of symbol at the point.</td>
</tr>
</tbody>
</table>

I just completed through the help documentation in emacs manual, and I am convinced the emacs has got the most extensive documentation an editor could ever have, the above table tries to cover as many things as possible but I am pretty sure, I would have definitely missed things, like this that once on IRC I had been suggested some lisp code to quickly take me to the help page and I missed it. Well, on many modern keyboards F1 as well works to call the help function.

While doing the typing I do make a lot of mistakes and undo is the most fundamental command for correcting the mistakes. C-/ does the same trick as C-x u and C-\_ all meant to undo my work. If you see the buffers have been modified accidentaly, the easiest way is to press **C-/** repetadely unless the stars disappears from the mod line. Just press **C-/** to see the last change, so that we can understand if the change was intentional, if yes then we can leave it like this, if no then we can undo by pressing **C-/** repeatedly.

Its much easier to transpose characters in emacs using \*C-t\*(transpose-chars)  and transpose words using \*M-t\*(transpose-words) and moves the word containing or preceding point forward as tell, though it does not move any punctutation mark, for eg, FOO, BAR will become BAR, FOO. \*C-M-t\*(transpose-sexps) is similar to transposing two expressions and \*C-x C-t\*(transpose-lines) for transposing lines. The numeric command works here, it tell the transpose command to move forward the character before or containing point across several other characters. 

**M&#x2013; M-l** Convert last word to lower-case, it is Meta-Minus. **M&#x2013; M-u** Convert last word to uppercase. **M&#x2013; M-c** convert last word to lowercase with capital letters.

The spell checking ability of any editor should be good for the writer to help check spells on the fly, and emacs does have some nifty commands to do that as well. We need aspell, ispell, hunspell installed on the system for these commands to work. Once started the programs continue to run so that subsequent spell check commands complete more quickly and can be killed using **M-x ispell-kill-ispell** but is not required as it does not uses much memory and only active when spelling correcting is done, these programs using two dictionaries one is the standard dictionary and the other is our defined dictionary. The local dictionary can be defined by "ispell-local-dictionary\* or if nil by "ispell-dictionary" or if both is nil then the default dictinary is selected. The variable "ispell-complete-word-dict" specifies the file name for its dictionary and is used for word completion. Flyspell mode is fully automatic mode of checking the words in the buffer as we insert them or edit them, when it finds the words it doesn't recognize it highlights that word. Right now I am seeing my buffer so colorful, thanks to flyspell mode, and my typing :). **M-x flyspell-mode** toggles the flyspell mode, to turn on flyspell mode for all text buffer **turn-on-flyspell-mode** to **text-mode-hook**.

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<tbody>
<tr>
<td class="left">Key binding</td>
<td class="left">command</td>
<td class="left">Description</td>
</tr>


<tr>
<td class="left">M-$</td>
<td class="left">ispell-word</td>
<td class="left">check and correct spelling of active region or word at point.</td>
</tr>


<tr>
<td class="left">M-x ipsell</td>
<td class="left">&#xa0;</td>
<td class="left">check or correct spelling in active region or entire buffer.</td>
</tr>


<tr>
<td class="left">M-x ispell-buffer</td>
<td class="left">&#xa0;</td>
<td class="left">check and correct spelling in the buffer.</td>
</tr>


<tr>
<td class="left">M-x ispell-region</td>
<td class="left">&#xa0;</td>
<td class="left">check and correct spelling in the region.</td>
</tr>


<tr>
<td class="left">M-x ispell-message</td>
<td class="left">&#xa0;</td>
<td class="left">check and correct spelling in the draft message, excluding citied content</td>
</tr>


<tr>
<td class="left">M-x ispell-change-dictionary RET *Dictionary* RET</td>
<td class="left">&#xa0;</td>
<td class="left">restart ispell/aspell/hunspell using dict as dictionary.</td>
</tr>


<tr>
<td class="left">M-x ispell-kill-ispell</td>
<td class="left">&#xa0;</td>
<td class="left">kill the dictionary process</td>
</tr>


<tr>
<td class="left">M-TAB / ESC-TAB</td>
<td class="left">ispell-complete-word</td>
<td class="left">complete the word based on the dictinary</td>
</tr>


<tr>
<td class="left">M-x flyspell-mode</td>
<td class="left">&#xa0;</td>
<td class="left">enable flyspell mode which highlights misspelled words</td>
</tr>


<tr>
<td class="left">M-x flyspell-prog-mode</td>
<td class="left">&#xa0;</td>
<td class="left">enable flyspell mode for comments and strings only</td>
</tr>
</tbody>
</table>

When the commands encounter the errors in case of misspelled words, it usually display the numbered "near-misses" close to the incorrect word, then we have to choose the valid response from the below list.

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />
</colgroup>
<tbody>
<tr>
<td class="left">digit</td>
<td class="left">replace the word, just this time, with one of the near misses, the near misses are displayed by no. and the no. can be used to select it.</td>
</tr>


<tr>
<td class="left">SPC</td>
<td class="left">skip this word, continue to consider incorrect and don't change.</td>
</tr>


<tr>
<td class="left">r *NEW* RET</td>
<td class="left">replace the word just this time, with the new word.</td>
</tr>


<tr>
<td class="left">R *NEW* RET</td>
<td class="left">replace the word and do query-replace so it can be replaced everywhere.</td>
</tr>


<tr>
<td class="left">a</td>
<td class="left">accept the incorrect word, treat it as correct one, but only in this editing session</td>
</tr>


<tr>
<td class="left">A</td>
<td class="left">same as above but include the buffer too.</td>
</tr>


<tr>
<td class="left">i</td>
<td class="left">insert this word in my private dictionary, so it can be treated as a correct word by my spell check applications</td>
</tr>


<tr>
<td class="left">m</td>
<td class="left">like i</td>
</tr>


<tr>
<td class="left">u</td>
<td class="left">save the lowercase version of this word to my private dictionary</td>
</tr>


<tr>
<td class="left">l *word* RET</td>
<td class="left">Look in the dictinary for the word that match *word*. these words become new list for near-misses.</td>
</tr>


<tr>
<td class="left">C-g X</td>
<td class="left">quit interactive spell checking</td>
</tr>


<tr>
<td class="left">C-g x</td>
<td class="left">quit interactive spell checking and move point back to where it was when you started spell checking.</td>
</tr>


<tr>
<td class="left">C-g q</td>
<td class="left">quit spell checking and kill the sub process as well.</td>
</tr>


<tr>
<td class="left">?</td>
<td class="left">show the list of options.</td>
</tr>
</tbody>
</table>

Well. I am done for the Day 6, being emacs is such a vast entity as an editor, i spend most of my time going through the help document and manual pages only and enable myself to write quality content, which should help me or any one else who might want to use my content for his/her reference. I am still at a very primitive level of doing things with emacs, but I am aware I am still to young here. I will put these text on git hub as well, for anyone to help me correcting the content or if adding anything more.

