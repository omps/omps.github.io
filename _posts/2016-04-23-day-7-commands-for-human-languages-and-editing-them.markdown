---
layout: post
title: "Day 7 - Commands for human languages and editing them"
date: 2015-12-20 21:20:12 +0530
comments: true
categories: emacs
tags: #emacs, #30daychallenge, #day7
---

Emacs is wonderful for text editing and related stuff with text. It has many modes which helps in editing and managing text, which help increase the productive overall, here I explored some of the major modes and commands which can quickly help for editing text.
<!--more-->
## Text Editing in Emacs<a id="sec-1-1" name="sec-1-1"></a>

Emacs has several major modes for handelling text, there is text mode for ordinary text which customizes emacs in small ways for syntactic convention of text. Outline mode provides special commands to handle text, Org Mode extends Outline mode and turns emacs into a full fledged organizer: we can manage TODO Lists, store notes and publish them in many formats and I would speak more about this in my coming days learnings. TeX and LaTeX mode contains embedded commands; HTML mode for HTML and SGML Modes; nxml-mode for XML Mode; Nroff Mode for Groff and Nroff Mode.

It is also possible to edit pictures made out of text characters, also referred as \*"ASCII art"\* using Picture mode.

## Words<a id="sec-1-2" name="sec-1-2"></a>

There are several commnads in emacs for operating on words and many of these I have already covered in my Day-1 and Day-4, but let me redo, so I will remeber it for a long time.
Again, the **M** refers the Meta i.e the Alt or Esc key on the keyboard and is followed by the character keys.

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Key bindings</th>
<th scope="col" class="left">commands</th>
<th scope="col" class="left">description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">M-f</td>
<td class="left">forward-word</td>
<td class="left">Self descriptive as it moves forward on word</td>
</tr>


<tr>
<td class="left">M-b</td>
<td class="left">backward-word</td>
<td class="left">it moves one word back.</td>
</tr>


<tr>
<td class="left">M-d</td>
<td class="left">kill-word</td>
<td class="left">kills up to the end of the word</td>
</tr>


<tr>
<td class="left">M-<DEL></td>
<td class="left">backward-kill-word</td>
<td class="left">kill backward to the beginning of the word.</td>
</tr>


<tr>
<td class="left">M-@</td>
<td class="left">mark-word</td>
<td class="left">Mark to the end of the word</td>
</tr>


<tr>
<td class="left">M-t</td>
<td class="left">transpose-words</td>
<td class="left">Transpose the word and drag across others</td>
</tr>


<tr>
<td class="left">M-=</td>
<td class="left">count-words-region</td>
<td class="left">gives the count of the words in the region.</td>
</tr>
</tbody>
</table>

*NOTES:*
*1. These keys parrellel with the character-based movements*
*2. The numeric arguments serves as the repeat count and the negative arguments would make the commands move in the opposite direction.*
*3. M-<DEL> deletes the word to the point where M-b would end, it will kill the comma and space as well, M-b M-d to just kill the word but not the comma.*
*4. If we choose there keybindings in our shell **(set -o emacs)**, these word keybindings can help us in moving around the long commands.*

## Sentences<a id="sec-1-3" name="sec-1-3"></a>

The meta keys are also helpful in moving around the sentences.

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Keybindings</th>
<th scope="col" class="left">commands</th>
<th scope="col" class="left">description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">M-a</td>
<td class="left">backward-sentence</td>
<td class="left">This will move the point to the beginning of the sentence</td>
</tr>


<tr>
<td class="left">M-e</td>
<td class="left">forward-sentence</td>
<td class="left">Will move forward to the end of sentence.</td>
</tr>


<tr>
<td class="left">M-k</td>
<td class="left">kill-sentence</td>
<td class="left">Kill forward to the end of the sentence.</td>
</tr>


<tr>
<td class="left">C-x <DEL></td>
<td class="left">backward-kill-sentence</td>
<td class="left">kill back to the beginning of the sentence.</td>
</tr>
</tbody>
</table>

### Quoting from EMACS Manual<a id="sec-1-3-1" name="sec-1-3-1"></a>

\#+BEGIN<sub>SRC</sub> Quote
 The sentence commands assume that you follow the American typist's
convention of putting two spaces at the end of a sentence.  That is, a
sentence ends wherever there is a \`.', \`?' or \`!' followed by the end
of a line or two spaces, with any number of \`)', \`]', \`'', or \`"'
characters allowed in between.  A sentence also begins or ends wherever
a paragraph begins or ends.  It is useful to follow this convention,
because it allows the Emacs sentence commands to distinguish between
periods that end a sentence and periods that indicate abbreviations.
\\#+END<sub>SRC</sub> Quote

*NOTE:*
*1. To use just one space between sentences, set the variable sentence-end-double-space to nil and to make the sentence commands stop for single spaces.*
*2. The variable sentence-end controls how to recognize the end of the sentence; its value is a regular expression, which is used to match the last few characters of the sentence.*
*3. Some languages such as Thai, doesn't end with periods; such cases can be handeld by setting variable sentence-end-without-period to t.*

## Paragraphs<a id="sec-1-4" name="sec-1-4"></a>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Keybindings</th>
<th scope="col" class="left">Commands</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">M-{</td>
<td class="left">backward-paragraph</td>
<td class="left">move to the beginning of paragraph.</td>
</tr>


<tr>
<td class="left">M-}</td>
<td class="left">forward-paragraph</td>
<td class="left">Move to the end of the next paragraph.</td>
</tr>


<tr>
<td class="left">M-h</td>
<td class="left">mark-paragraph</td>
<td class="left">put point and mark around this or next paragraph.</td>
</tr>


<tr>
<td class="left">M-h C-w</td>
<td class="left">&#xa0;</td>
<td class="left">kills the paragraph around or after point.</td>
</tr>
</tbody>
</table>

*Notes:*
*1. The definition of a paragraph boundary is controlled by the variables **paragraph-separate** and  **paragraph-start**. The value of these are regular expression.*
*2. In fundamental mode, Paragraph-start is \*"\f\\\\|[ \t]\*$"\* and matches lines that either start or separate paragraph.* 
*3. Paragraph separate is \*"[ \t\f]\*$"\* and matches lines  that separate paragraph without being part of any paragraph.*

## Pages<a id="sec-1-5" name="sec-1-5"></a>

The files are divided into pages delimited by the "formfeed character" (ASCII code 2, denoted as <contorl-l>) and in emacs is escape sequence .

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Keybindings</th>
<th scope="col" class="left">Commands</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">M-x What-page</td>
<td class="left">&#xa0;</td>
<td class="left">Display the page number and line number within that page</td>
</tr>


<tr>
<td class="left">C-x [</td>
<td class="left">backward-page</td>
<td class="left">Move point to the previous page boundary.</td>
</tr>


<tr>
<td class="left">C-x ]</td>
<td class="left">forward-page</td>
<td class="left">Move point ot next page boundary</td>
</tr>


<tr>
<td class="left">C-x C-p</td>
<td class="left">mark-page</td>
<td class="left">put point and mark around this page.</td>
</tr>


<tr>
<td class="left">C-x C-p C-w</td>
<td class="left">&#xa0;</td>
<td class="left">select and kill the page</td>
</tr>


<tr>
<td class="left">C-x l</td>
<td class="left">count-lines-page</td>
<td class="left">Count the lines in this page.</td>
</tr>
</tbody>
</table>

*Note:*
*page-delimiter control where the page begins. Its a regular expression \*"f"\* which matches a beginning of a line that separate pages.*

## Filling Text<a id="sec-1-6" name="sec-1-6"></a>

Filling text means breaking up the lines that fit a specified width. Emacs does the filling in 2 ways. **Auto Fill Mode** inserts text with self-inserting characters and automatically fills it. **Explicit fill Commands**  can be used for editing texts.

### Auto Fill<a id="sec-1-6-1" name="sec-1-6-1"></a>

This is a minor mode in which the lines are broken automatically when they become too wide, breaking up of lines only happens when you type <SPC> or <RET>.

'M-x auto-fill-mode' : Toggles the Auto Fill mode.

'<SPC>/<RET>' : Break lines when appropriate.

From the command line the auto-fill mode enables or disables the mode for current buffer. From LISP *auto-fill* is enabled when called with omitted or nil argument. for enabling in the major modes, add auto-fill-mode in mode hooks. When the mode it enabled it will show **Fill** in the mode line.

This mode breaks any line which goes longer than the desired width by pressing <SPC> or <RET>, and to insert a SPACE or any newline without breaking the lines tye **C-q <SPC>** or **C-q C-j** and **C-o** for inserting new line.

Auto fill mode does not refill the paragraphs; it break lines but does not merge lines, editing in the middle of the paragraph can result in paragraph which is not correctly filled. To fill them correctly we may need to use explicit Fill Commands.

### Fill Commands<a id="sec-1-6-2" name="sec-1-6-2"></a>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Key bindings</th>
<th scope="col" class="left">Command</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">M-q</td>
<td class="left">fill-paragraph</td>
<td class="left">Fill current paragraph</td>
</tr>


<tr>
<td class="left">C-x f</td>
<td class="left">set-fill-column</td>
<td class="left">Set the fill column</td>
</tr>


<tr>
<td class="left">M-x fill-region</td>
<td class="left">fill-region</td>
<td class="left">Fill each paragraph in the region.</td>
</tr>


<tr>
<td class="left">M-x fill-region-as-paragraph</td>
<td class="left">&#xa0;</td>
<td class="left">Fill the region consider it as paragraph.</td>
</tr>


<tr>
<td class="left">M-o M-s</td>
<td class="left">&#xa0;</td>
<td class="left">Center a line.</td>
</tr>
</tbody>
</table>

*Notes:*
*1. M-q and fill-region uses the usual emacs criteria for finding paragraph boundaries, which refills everything between point and mark as single paragraph.*
*2. Numeric argument to **M-q** justifies the text as well as fill it.*
*3. To Remove extra spaces, use M-q with no argument.*
*4. The default vault for fill column is 70.*
*5. **C-x f** (sets-fill-column) sets the numeric value for fill column. With just C-u as argument it sets fill-column to the current horizantal position of point.*
*6. By default, emacs consider a period followed  by two spaces or by a newline as the end of sentence; a period with just one space will be called as abbrevation and not the end of the sentence.*
*7. Setting 'sentence-end-double-space' to nil the fill commands will break a line after a period followed by a period and a space.*

### The Fill Prefix<a id="sec-1-6-3" name="sec-1-6-3"></a>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Keybindings</th>
<th scope="col" class="left">Command</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">C-x .</td>
<td class="left">set-fill-prefix</td>
<td class="left">Set the fill prefix</td>
</tr>


<tr>
<td class="left">M-q</td>
<td class="left">fill-paragraph</td>
<td class="left">Fill a paragraph using current fill prefix</td>
</tr>


<tr>
<td class="left">M-x fill-individual-paragraphs</td>
<td class="left">&#xa0;</td>
<td class="left">Fill the region, considering each change of indentation as starting a new paragraph.</td>
</tr>


<tr>
<td class="left">M-x fill-nonuniform-paragraphs</td>
<td class="left">&#xa0;</td>
<td class="left">Consider only paragraph separator lines as starting a new paragraph.</td>
</tr>
</tbody>
</table>

*Notes:*
*1. Move to a line which starts with desired prefix, put point at the end of the prefix and type C-x .*
*2. To turn off a prefix, specify an empty prefix: type C-x . with point at the beginning of line.*
*3. The fill prefix is stored in fill-prefix variable. if the value is nil, then there is no fill prefix.*

This feature allows paragraphs to be filled so each line starts with a special string of characters (such a sequence of spaces, giving and indented paragraph). you can specify fill prefix explicitly; otherwise emacs tries to deduce automatically.

### Adaptive Fill.<a id="sec-1-6-4" name="sec-1-6-4"></a>

The fill command deduce the proper fill prefix for a paragraph automatically in some cases; either white spaces or certain precaution characters at the beginning of line are propagated to all lines of the paragraph.

If the paragraph has two or more lines, the fill prefix is taken from the paragraph's second line, but only if it appears on the first line as well.

If a paragraph has just one line, fill commands <span class="underline">may</span> take a prefix from that line.  The decision is complicated because there are three reasonable things to do in such a case: 

-   Use the first line's prefix on all the lines of the paragraph.

-   Indent subsequent lines with whitespace, so that they line up under the text that follows the prefix on the first line, but don't actually copy the      
    prefix from the first line.

-   Don't do anything special with the second and following lines.

All three of these styles of formatting are commonly used.  So the fill commands try to determine what you would like, based on the prefix that appears and on the major mode.  Here is how.

If the prefix found on the first line matches \`adaptive-fill-first-line-regexp', or if it appears to be a comment-starting sequence (this depends on the major mode), then the prefix found is used for filling the paragraph, provided it would not act as a paragraph starter on subsequent lines.

Otherwise, the prefix found is converted to an equivalent number of spaces, and those spaces are used as the fill prefix for the rest of the lines, provided they would not act as a paragraph starter on subsequent lines.

In Text mode, and other modes where only blank lines and page delimiters separate paragraphs, the prefix chosen by adaptive filling never acts as a paragraph starter, so it can always be used for filling.

The variable \`adaptive-fill-regexp' determines what kinds of line beginnings can serve as a fill prefix: any characters at the start of the line that match this regular expression are used.  If you set the variable \`adaptive-fill-mode' to \`nil', the fill prefix is never chosen automatically.

You can specify more complex ways of choosing a fill prefix automatically by setting the variable \`adaptive-fill-function' to a function.  This function is called with point after the left margin of a line, and it should return the appropriate fill prefix based on that line.  If it returns \`nil', \`adaptive-fill-regexp' gets a chance to find a prefix.

## Case<a id="sec-1-7" name="sec-1-7"></a>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Keybindings</th>
<th scope="col" class="left">Commands</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">M-l</td>
<td class="left">downcase-word</td>
<td class="left">Convert the following word to lower case.</td>
</tr>


<tr>
<td class="left">M-u</td>
<td class="left">upcase-word</td>
<td class="left">Convert the following word to upper case.</td>
</tr>


<tr>
<td class="left">M-c</td>
<td class="left">capitalize-word</td>
<td class="left">Capitalize the following word.</td>
</tr>


<tr>
<td class="left">C-x C-l</td>
<td class="left">downcase-region</td>
<td class="left">Convert region to lowercase.</td>
</tr>


<tr>
<td class="left">C-x C-u</td>
<td class="left">upcase-region</td>
<td class="left">Convert region to upper case.</td>
</tr>
</tbody>
</table>

*Note:*
*1. When a negative argument, the case conversion applies to appropriate no. of words before point, but do not move the point, its convinent if I typed something in wrong case and want to correct the case.*
*2. In case the command to change case is given in the middle of the word, the case change would happen from the point to the end of the word.*

## Text Mode<a id="sec-1-8" name="sec-1-8"></a>

This is the major mode for editing the text language, any file ending with .txt will automatically enables this mode; and this mode can also be called by M-x text-mode. Blank lines and page delimiters separate paragraphs, and as a result paragraphs can be indented, and adaptive filling determines what indentation to use when filling a paragraph. The <TAB> usually inserts whitespace up to the next tab stop, instead of indenting the current line.

Text mode turns off comments features except when you explicitly invoke them. It changes so that the single quotes are considered part of the words. But if a word starts with a single quote it is treated as a prefix for the purpose of capitalization. Entering text-mode invokes text-mode-hook.

## Outline Mode<a id="sec-1-9" name="sec-1-9"></a>

This is major mode derived from Text mode, which is specialized for editing outlines; it provides commands to navigate between entries in the outline structure. Type M-x outline-mode to switch to outline mode, entering this mode runs the hook text-mode-hook followed by outline-mode-hook.

When in outline mode use command to make a line invisible it disappears the line and ellipsis(three periods in a row) is displayed at the end of the previous visible line.

Editing command on lines, such as C-n and C-p treat the text of the invisible line as part of the previous visible line.

outline-minor-mode toggle outline minor mode in the current buffer, it is a buffer-local minor mode which provides the same commands as the major mode for the current buffer, this provides special keybindings with C-c prefix, and C-c @ as the prefix in minor-mode.

### Outline Format<a id="sec-1-9-1" name="sec-1-9-1"></a>

Outline mode assumes the the lines in the buffer are of two types:
"heading lines" and "body lines"

Heading line: start with one or more asterisk ('\*'); the number of asterisks determines the depth of the heading in the outline structure. 
Body Line: Any line which is not a heading line is a body line. Body line belong with a preceding heading line.

A heading line and a body line collectively is called as an entry.

### Outline mode commands<a id="sec-1-9-2" name="sec-1-9-2"></a>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Key bindings</th>
<th scope="col" class="left">Commands</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">C-c C-n</td>
<td class="left">outline-next-visible-heading</td>
<td class="left">Move point to the next visible heading</td>
</tr>


<tr>
<td class="left">C-c C-p</td>
<td class="left">outline-previous-visible-heading</td>
<td class="left">Move point to the previous visible heading.</td>
</tr>


<tr>
<td class="left">C-c C-f</td>
<td class="left">outline-forward-same-level</td>
<td class="left">Move point to the next visible heading line at the same level.</td>
</tr>


<tr>
<td class="left">C-c C-b</td>
<td class="left">outline-backward-same-level</td>
<td class="left">Move point to previous heading line at the same level.</td>
</tr>


<tr>
<td class="left">C-c C-u</td>
<td class="left">outline-up-heading</td>
<td class="left">Move point up to a lower-level.</td>
</tr>
</tbody>
</table>

### Outline visibility commands<a id="sec-1-9-3" name="sec-1-9-3"></a>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Keybindings</th>
<th scope="col" class="left">Commands</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">C-c C-c</td>
<td class="left">hide-entry</td>
<td class="left">Make the current heading line's body invisible</td>
</tr>


<tr>
<td class="left">C-c C-e</td>
<td class="left">show-entry</td>
<td class="left">Make the current heading line's body visible</td>
</tr>


<tr>
<td class="left">C-c C-d</td>
<td class="left">hide-subtree</td>
<td class="left">Make everything under the heading invisible excluding the heading</td>
</tr>


<tr>
<td class="left">C-c C-s</td>
<td class="left">show-subtree</td>
<td class="left">Make everything under the current heading visible</td>
</tr>


<tr>
<td class="left">C-c C-l</td>
<td class="left">hide-leaves</td>
<td class="left">Make the body of the current heading line, and all of its subheadings</td>
</tr>


<tr>
<td class="left">C-c C-k</td>
<td class="left">show-branches</td>
<td class="left">Make all subheading of the current heading line, at all levels, visible</td>
</tr>


<tr>
<td class="left">C-c C-i</td>
<td class="left">show-children</td>
<td class="left">Make immediate subheadings of the current heading line visible</td>
</tr>


<tr>
<td class="left">C-c C-t</td>
<td class="left">hide-body</td>
<td class="left">Make all body lines in the buffer invisible</td>
</tr>


<tr>
<td class="left">C-c C-a</td>
<td class="left">show-all</td>
<td class="left">Make all line in the buffer visible</td>
</tr>


<tr>
<td class="left">C-c C-q</td>
<td class="left">hide-sublevels</td>
<td class="left">Hide everything except the top N level of heading lines</td>
</tr>


<tr>
<td class="left">C-c C-o</td>
<td class="left">hide-other</td>
<td class="left">HIde everything except the heading or the body that point is in</td>
</tr>
</tbody>
</table>

And most of these commands may work differently in org-mode, the org-mode is an advance implementation of outline-mode. I will be writing about this mode in my later days. It may confuse me at a later stage as mainly I use org-mode for my purposes of note taking and writing this blog. Let me provide some brief introduction to the org-mode.

## Org Mode<a id="sec-1-10" name="sec-1-10"></a>

Org mode, as in outline mode, each entry has a heading line that starts with one or more asterisk (\*); Any line beginning with a '#' is considered as a comment. and it also provides commands to view and manipulate the outline structure. 

The simplest of these commands is <TAB> (org-cycle). If invoked on heading line, it cycles through different visiblity states of that subtree:
1.  Showing only the heading line.
2.  Show only the heading lines and the heading lines of its direct children.
3.  Show the entire subtree.

The <S-TAB> (org-shifttab) in an org mode cycle visiblity of entire online subtree
1.  Show only top-level heading lines.
2.  Show all heading lines but no body lines.
3.  Show everything.

We can move the entire entry up and down in the buffer, including its body lines and subtree, by typing M-<up> (org-metaup) or M-<down> (org-metadown) on the heading line. Similarly, it can promote or demote the heading line with M-<left> (org-metaleft) and M-<right (org-metaright). For details, The Org Mode Manual.

### Org as an Organizer<a id="sec-1-10-1" name="sec-1-10-1"></a>

You can tag an Org entry as a "TODO" by typing **C-c C-t** (org-todo) anywhere in the entry. This adds *TODO* keyword and typing the keyword **C-c C-t** again switches the keyword to *DONE*; press **C-c C-t** again and it will remove the keyword entirely. They keywords can be customized using the variable 'org-todo-keywords'

With the possiblity of marking an entry as TODO, we can also attach a date to it by typing **C-c C-s** (org-schedule), This prompts for a date by popping a calendar, and then adds the tag 'SCHEDULED', together with the selected date, beneath the heading line. **C-c C-d** (org-deadline) have the same effect except it adds the tag 'DEADLINE'.

Once you have some planned TODO items, you can add that file to the list of "agenda fileS" by typing **C-c [** (org-agenda-file-to-front). It allows us to maintain multiple agenda  files. The list of these agenda files are stored in the variable 'org-agenda-files'.

Typing M-x org-agenda lets view items coming from agenda file, this command prompts for what we want to see: a list of things to do this week, a list of TODO items with specific keywords.

### Org as an authoring system<a id="sec-1-10-2" name="sec-1-10-2"></a>

To format org notes nicely and to prepare them for export and publication, **C-c C-e** (org-export) to export buffer and prompts for a export format; includes HTML, LaTeX, OpenDocument(.odt), and PDF.

To export several files at once to a specified directory, either locally or over the network, we can define a list of projects through the variable 'org-publish-project-alist' 

Org supports a simple markup scheme for applying text formatting to exported documents:

-   This text is *emphasized*
-   This text is **in bold**
-   This text is <span class="underline">underlined</span>
-   This text uses `a teletype font`

> \`\`This is a quote.''

    This is an example.

## TeX Mode<a id="sec-1-11" name="sec-1-11"></a>

Emacs provides special major modes for editing files written in TeX and its related formats. TeX is a powerful text formatter written by Donald Knuth; like GNU Emacs. Latex is a simplified input format for TeX implemented using TeX macros. DocTeX is a special file format in which the LateX sources are written, combining sources with documentation. 

TeX mode has four variants:
1.  Plain TeX mode
2.  LateX mode.
3.  DocTeX mode.
4.  SliTeX mode.

These distinc major modes differ only slightly, and are designed for editing the four different format. Emacs selects the appropriate mode by looking at the contents of the buffer. Emacs chooses the mode specified by the variable 'tex-default-mode'; its default value is latex-mode. If Emacs doesn't get it right you can select the correct variant of TeX using the command 'M-x plain-tex-mode', 'M-x latex-mode', 'M-x slitex-mode', or 'M-x doctex-mode'.

## SGML and HTML Modes<a id="sec-1-12" name="sec-1-12"></a>

HTML mode is slightly customizable variant of SGML mode.

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Keybindings</th>
<th scope="col" class="left">Command</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">C-C C-n</td>
<td class="left">sgml-name-char</td>
<td class="left">Interactively specify a special character and insert the SGML '&' command for that character</td>
</tr>


<tr>
<td class="left">C-c C-t</td>
<td class="left">sgml-tag</td>
<td class="left">Specify a tag and its attribute.</td>
</tr>


<tr>
<td class="left">C-c C-a</td>
<td class="left">sgml-attributes</td>
<td class="left">insert attribute value for the current tag</td>
</tr>


<tr>
<td class="left">C-c C-f</td>
<td class="left">sgml-skip-tag-forward</td>
<td class="left">skip across a balanced tag group.</td>
</tr>


<tr>
<td class="left">C-c C-b</td>
<td class="left">sgml-skip-tag-backward</td>
<td class="left">skip backward across a balanced tag group.</td>
</tr>


<tr>
<td class="left">C-c C-d</td>
<td class="left">sgml-delete-tag</td>
<td class="left">Delete the tag</td>
</tr>


<tr>
<td class="left">C-c ? TAG <RET></td>
<td class="left">sgml-tag-help</td>
<td class="left">display the description and the meaning of the tag</td>
</tr>


<tr>
<td class="left">C-c /</td>
<td class="left">sgml-close-tag</td>
<td class="left">insert a close tag for the innermost undetermind tag</td>
</tr>


<tr>
<td class="left">C-c 8</td>
<td class="left">sgml-name-8bit-mode</td>
<td class="left">Toggle a minor mode in which Latin-1 characters insert the corresponding SGML commands.</td>
</tr>


<tr>
<td class="left">C-c C-v</td>
<td class="left">sgml-validate</td>
<td class="left">run a shell commands to validate the current buffer as SGML.</td>
</tr>


<tr>
<td class="left">C-c <TAB></td>
<td class="left">sgml-tags-invisible</td>
<td class="left">Toggle the visiblity of existing tags in the buffer.</td>
</tr>
</tbody>
</table>

There is a major mode for editing XML documents called as nXML mode. This is a mode which can recognize any XML schema and use them to provide completion on XML elements via 'M-<TAB>, as well as on the fly XML validation with error highlighting. To enable nXML mode for existing buffer type **M-x nxml-mode** or **M-x xml-mode**

For files with extension .xml nxml-mode is used by default; and for files with xhtml html-mode is used.

## Nroff mode<a id="sec-1-13" name="sec-1-13"></a>

This is a major mode derived from Text mode and is specialized for editing nroff files e.g. UNIX man pages. **M-x nroff-mode** enters into this mode, and runs the hook 'text-mode-hook', then 'nroff-mode-hook'; nroff command lines are treated as paragraph separators, pages are separated by '.bp' commands, and comments start with backslash-doublequote (\\")

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Keybindings</th>
<th scope="col" class="left">Commands</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">M-n</td>
<td class="left">forward-next-line</td>
<td class="left">move to the beginning of next line, which is not a nroff command</td>
</tr>


<tr>
<td class="left">M-p</td>
<td class="left">backward-next-line</td>
<td class="left">same but moves up</td>
</tr>


<tr>
<td class="left">M-?</td>
<td class="left">count-text-lines</td>
<td class="left">display in the echo area the number of text lines.</td>
</tr>
</tbody>
</table>

**M-x electric-nroff-mode** toggles the Electric Nroff mode and is a minor-mode and can be used with Nroff mode. 

## Enriched Text<a id="sec-1-14" name="sec-1-14"></a>

This is a minor mode for editing formatted text files in a WYSIWYG ("what you see is what you get") fashion. When Enriched mode is enabled we can apply various formatting properties to the text in the buffer. This mode is typically used by Text mode and is not compatible with Font Lock Mode which is used by many major modes, for syntax highlighting. When you save a buffer with enriched mode enabled, it is saved using the 'text/enriched' format, including the formatting indentation.

To create a new file of formatted text, visit file and type **M-x enriched-mode** 

## Editing Text Based Tables<a id="sec-1-15" name="sec-1-15"></a>

The table package provides commands to easily edit the text-based tables. A "table" consist of t a rectangular text area which is divided into "cells". Each cell must be one character wide and one character high, not counting its border lines. A cell can be subdivided into more cells, but they cannot overlap.

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Commands</th>
<th scope="col" class="left">Default</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">table-cell-vertical-char</td>
<td class="left">Pipe</td>
<td class="left">The character used for vertical lines.</td>
</tr>


<tr>
<td class="left">table-cell-horizontal-chars</td>
<td class="left">- =</td>
<td class="left">character used for horizontal lines.</td>
</tr>


<tr>
<td class="left">table-cell-intersection-char</td>
<td class="left">+</td>
<td class="left">character used for intersection of horizontal and vertical lines</td>
</tr>
</tbody>
</table>

The following are examples of <span class="underline">invalid</span> tables:

<!-- This HTML table template is generated by emacs 24.5.1 -->
<table border="1">
  <tr>
    <td align="left" valign="top">
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br />
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br />
      --+&nbsp;&nbsp;<br />
      &nbsp;&nbsp;|&nbsp;&nbsp;<br />
      &nbsp;&nbsp;|&nbsp;&nbsp;
    </td>
  </tr>
</table>

a          b          c

From left to right:

1.  Overlapped cells or non-rectangular cells are not allowed.

2.  The border must be rectangular.

3.  Cells must have a minimum width/height of one character.

## Two column editing<a id="sec-1-16" name="sec-1-16"></a>

Two columns lets you convinently edit two side-by-side columns of text. It uses two side-by-side windows, each showing its own buffer. There are three ways to enter two column mode:

1.  <F2> 2 or C-x 6 2 - Enter two columns mode with the current buffer on the left and on the right, a buffer whose name is based on the current buffer's name.

2.  <F2> s  or C-x 6 s - Split the current buffer, which contains two column text, into two buffers and display them side by side.

3.  <F2> b BUFFER <RET> or C-x 6 b BUFFER <RET> - Enter two columns mode using the current buffer as the left-hand buffer, and using buffer BUFFER as the right-hand buffer.
