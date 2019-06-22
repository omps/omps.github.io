---
layout: post
title: "Day 10 - Search and Replace using regex"
date: 2016-01-20 21:44:31 +0530
comments: true
categories: emacs
tags: #emacs, #30daychallenge, #day10
---

It is important that I am also should be able to search within my text/code when using the editor. Emacs have commands to search for occurrences of a string within the buffer and across the buffers. Emacs has the commands to replace occurrences of a string with a different string. Emacs provides the ability to search multiple files under the control of a tags table or through dired 'A' command , or ask the 'grep' program to do it.
<!--more-->
## Incremental Search
All the searches done in Emacs are "incremental" in nature i.e. it starts searching as soon as we start typing the first character of the search string. As we start typing emacs shows where the string and as we type further, would be found. We can end our search using RETURN.

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
<td class="left">C-s</td>
<td class="left">isearch-forward</td>
<td class="left">Incremental search forward</td>
</tr>

<tr>
<td class="left">C-r</td>
<td class="left">isearch-backward</td>
<td class="left">Incremental search backward</td>
</tr>
</tbody>
</table>
</div>

### Basic incremental search

Incremental search starts a forward incremental search. It reads characters from the keyboard, and moves point just past the end of the next occurrence of those characters in the buffer. When you type ```C-s``` and then F that puts the cursor after the first 'F' that occurs in the buffer after the starting point then if you type O it moves the cursor to just after the FO. At each step emacs highlights, the "current match" – the buffer text which matches the string -- using the 'isearch' face. The current search string is also displayed in the echo area. While we made mistake typing the search string, just press ```<DEL>```. Each ```<DEL>``` cancels the last character of the search string. Once satified, press <RET> Typing ```C-a``` exits the search and moved to the beginning of the line.

As an exception, entering <RET> when the search string is empty launches nonincremental search.

When you exit the search, it add the original value of the point to the mark ring, without activating the mark; use ```C-u C-<SPC>``` to return to where you were before the beginning the search.

Use ```C-r``` to search backwards. A backward search finds matches that end before the starting point.

### Repeating incremental search

Suppose you searched for some word 'FOO' and find a match, but its not the one you expected to find, typing C-s again will jump to the next occurence of the word FOO, repeat this any number of time, till you reach the correct instance. If you overshoot(i.e. added more characters to the search string) your search string cancel the same using the ```<DEL>``` character, which will delete the last visible character in the search string. When you pause a little after typing your search string, Emacs highlights all the possible matches for the search string. This helps in anticipating how many 'C-s' or 'C-r' you may need to type before you end at the right search. The other matches are highlighted differently than the current match, this can be changes by customizing the face lazy-highlight. This feature can be disabled by setting isearch-lazy-highlight to nil.

Once exited from the search the same string can be used to search again using 'C-s C-s' , the first 'C-s' invokes the search, the second 'C-s' means search again. The similar concepts can be applied while searching backward. While searching forward, you realise, that what you are looking for is before the starting point, you can easily switch with 'C-r'.

To reuse a search string, use the "search ring". The commands M-p and 'M-n' move through the ring to pick a search string to reuse. It leaves the selected search ring element in the minibuffer, which can then be edited. If we just need to edit the current search string in the minibuffer without replaying it with items from the search ring, type 'M-e', then type <RET>, 'C-s' or 'C-r' to finish editing and search for the string.

### Erros while incremental search

After typing the search string and if the search string is not found in the buffer, the echo area will say Failing I-Search, and the cursor moves to the place where Emacs found as much of your string as it could. Thus, if you search for 'FOOT' and there is no 'FOOT' in the buffer, then the cursor would be placed after 'FOO' in 'FOOL'. While, in the echo area, the part of the search string that failed to match is highlighted using face isearch-fail. We can correct our string if it was mis-typed, if we liked the place where it is found we can remain there by pressing <RET> or can just remove the character from search string which cannot be found by typing 'C-g', so this will remove the 'T' in 'FOOT' which could not be found and leaving those that are found. i.e will leave the 'FOO' in 'FOOT', repressing 'C-g' cancels the search altogether and return to the point where it was before the search has started.

### Special input for incremental search

There are characters which has special effects when typed during incremental search. In default, the incremental search perform lax space matching i.e. each space, or sequence of spaces, matches any sequence of one or more spaces in the text. Hence, 'foo bar' will match 'foo bar', 'foo bar', 'foo bar', and so on but it will not match 'foobar'. Emacs matches each sequence of space characters in the match string to a regular expression specified by the variable search-whitespace-regexp. To toggle lax space matching 'M-s <SPC>' isearch-toggle-lax-whitespace, and to disable this feature entirely set search-whitespace-regexp to nil, and then each single space will be matched to single space only.

By default the searches in emacs are case-insenitive, when there is an uppercase letter is present in search string, the searches become case-sensitive, once the upper case letter it deleted the search string becomes case-insensitive again.

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
<td class="left">M-s i</td>
<td class="left">&#xa0;</td>
<td class="left">isearch-toggle-invisible</td>
</tr>

<tr>
<td class="left">C-s C-j</td>
<td class="left">&#xa0;</td>
<td class="left">search for newline character</td>
</tr>

<tr>
<td class="left">C-s C-\\</td>
<td class="left">isearch-toggle-input-method</td>
<td class="left">Toggle the input method</td>
</tr>

<tr>
<td class="left">C-s C-^</td>
<td class="left">isearch-toggle-specified-input-method</td>
<td class="left">prompts for the name of the input method.</td>
</tr>

<tr>
<td class="left">C-s M-%</td>
<td class="left">query-replace or query-replace-regexp</td>
<td class="left">with current search string used as a string to replace.</td>
</tr>

<tr>
<td class="left">C-s M-&lt;TAB&gt;</td>
<td class="left">isearch-complete</td>
<td class="left">tries to complete the search string using the search ring as a list of completion alternatives.</td>
</tr>

<tr>
<td class="left">C-s C-h C-h</td>
<td class="left">&#xa0;</td>
<td class="left">Interactive help.</td>
</tr>

<tr>
<td class="left">C-s C-y</td>
<td class="left">isearch-yank-kill</td>
<td class="left">Appends the current kill to the search string.</td>
</tr>

<tr>
<td class="left">C-s M-y</td>
<td class="left">isearch-yank-pop</td>
<td class="left">If called after 'C-y', replaces the appended text with an earlier kill, similar to usual 'M-y'.</td>
</tr>

<tr>
<td class="left">C-s C-w</td>
<td class="left">isearch-yank-word-or-char</td>
<td class="left">Appends the next character or word at point to the search string.</td>
</tr>

<tr>
<td class="left">C-s M-s C-e</td>
<td class="left">isearch-yank-line</td>
<td class="left">Appends the rest of the line to the search string. if point is already at the end of a line, it appends the next-line.</td>
</tr>

<tr>
<td class="left">C-s C-M-w</td>
<td class="left">isearch-del-char</td>
<td class="left">Deletes the last character from the search string.</td>
</tr>

<tr>
<td class="left">C-s C-M-y</td>
<td class="left">isearch-yank-char</td>
<td class="left">Appends the character after the point to the search string. Alternately, to add the character after point by entering minibuffer with '<b>M-e</b>' and type '<b>C-f</b>' at the end of the search string in the minibuffer</td>
</tr>

<tr>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
</tr>
</tbody>
</table>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<colgroup>
<col  class="left" />
</colgroup>
<tbody>
<tr>
<td class="left">Search for non-ASCII characters.</td>
</tr>

<tr>
<td class="left">C-q <b>non graphical character</b></td>
</tr>

<tr>
<td class="left">C-x 8 &lt;RET&gt;</td>
</tr>

<tr>
<td class="left">Use an INPUT Method, so if the INPUT method is enabled in the current buffer so when you start the search, you can use it in the seach string also.</td>
</tr>

<tr>
<td class="left">&#xa0;</td>
</tr>
</tbody>
</table>

### Not exiting incremental search

There are two categories of commands which you can type without exiting the current incremental search. They are

- Prefix arguments
With these arguments, by default it will apply either to the next action in the search or to the command that exits the search. When isearch-allow-prefix is set to nil, entering a prefix argument will terminate the search.

- Scrolling commands
Scrolling commands exit search. changing variable ```isearch-allow-scroll``` to non-nil value, this enables the use of the scroll-bar as well as keyboard scrolling commands. The isearch-allow-scroll also afects some other commands, such as ```C-x 2``` and ```C-x ^``` which don't actually scroll but do affect where the text appears on the screen.

### Searching the minibuffer

If you start search while the minibuffer is active, Emacs searches the content of the minibuffer. If the search fails in the minibuffer, it tries searching the minibuffer history. The minibuffer can be visualized in series of pages. A forward search searches forward to later pages and similarly a reverse search does the backward search. If the current search is a history element, that history element is pulled in the minibuffer. Even you exit the incremental search by press RET, the point remains in the minibuffer unless it is specifically cancelled using C-g.

## Non Incremental search

So we have visited how the incremental search works, i.e while you type the characters the emacs already begun it searching process and as every word gets added it moves you closer to what you are looking for, and if this is too annoying, emacs does have a conventional non-ncremental search, which require the complete string to present before it start searching.


<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<colgroup>
<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Keybinding</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td class="left">C-s &lt;RET&gt; STRING &lt;RET&gt;</td>
<td class="left">search for string</td>
</tr>

<tr>
<td class="left">C-r &lt;RET&gt; STRING &lt;RET&gt;</td>
<td class="left">Search backward for string</td>
</tr>

<tr>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
</tr>
</tbody>
</table>
</div>
</div>

### Search for word.

A "word search" finds a sequence of words without regard to the type of punctuation between them. For instance, if you enter a search string that consists of two words seperated by a single space, the search matched any sequence of those two words separated by one or more spaces, newlines, or other punctiation characters. Useful for searching text documents where you do not have to worry about the words you are looking for and wether they are sperated by newlines of spaces.
</p>
<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Keybinding</th>
<th scope="col" class="left">Commands</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td class="left">M-s-w</td>
<td class="left">isearch-toggle-word</td>
<td class="left">if incremental search is active toggle to word search mode.</td>
</tr>

<tr>
<td class="left">&#xa0;</td>
<td class="left">isearch-forward-searching</td>
<td class="left">begin and incremental forward word search.</td>
</tr>

<tr>
<td class="left">M-s-w &lt;RET&gt; WORDS &lt;RET&gt;</td>
<td class="left">&#xa0;</td>
<td class="left">similar to the non-incremenatal forward search.</td>
</tr>

<tr>
<td class="left">M-s w C-r &lt;RET&gt; WORDS &lt;RET&gt;</td>
<td class="left">&#xa0;</td>
<td class="left">similar to non-incremental backward search.</td>
</tr>
</tbody>
</table>
</div>
</div>

### search for symbols.

<p>
It is just like normal search, except the boundaries of the search must match the boundaries of the symbol. This feature is mainly useful for searching the source code. 
</p>
<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Keybinding</th>
<th scope="col" class="left">Command</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td class="left">M-s</td>
<td class="left">isearch-toggle-symbol</td>
<td class="left">If active incremental search is, toggle symbol search mode.</td>
</tr>

<tr>
<td class="left">&#xa0;</td>
<td class="left">isearch-forward-symbol</td>
<td class="left">else, begin an incremental forward search.</td>
</tr>

<tr>
<td class="left">M-s .</td>
<td class="left">&#xa0;</td>
<td class="left">Start incremental symbol searching forward with the symbol found at the point is added to the initial search.</td>
</tr>

<tr>
<td class="left">M-s \_ &lt;RET&gt; SYMBOL &lt;RET&gt;</td>
<td class="left">&#xa0;</td>
<td class="left">Searches forward for symbol non-incrementally.</td>
</tr>

<tr>
<td class="left">M-s \_ C-r &lt;RET&gt; SYMBOL &lt;RET&gt;</td>
<td class="left">&#xa0;</td>
<td class="left">Search backward for symbol non-incrementally.</td>
</tr>
</tbody>
</table>
</div>
</div>

### search using regular expressions.

<p>
A regexp denotes a class of alternative strings to match. Emacs provides both incremental and non-incremental ways to search for a match for a regexp. Below is the syntax for regluar expressions.
</p>

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
<td class="left">C-M-s</td>
<td class="left">isearch-forward-regexp</td>
<td class="left">Begin incrmental search.</td>
</tr>

<tr>
<td class="left">C-M-r</td>
<td class="left">isearch-backward-regexp</td>
<td class="left">Begin reverse incremental search.</td>
</tr>

<tr>
<td class="left">C-M-s &lt;RET&gt;</td>
<td class="left">re-search-forward</td>
<td class="left">non incremental forward search</td>
</tr>

<tr>
<td class="left">C-M-r &lt;RET&gt;</td>
<td class="left">re-search-backward</td>
<td class="left">non incremental backward search</td>
</tr>
</tbody>
</table>
</div>

## Understanding Regular expressions (regex)

[The Emacs Regular Expression](https://www.gnu.org/software/emacs/manual/html_node/emacs/Regexps.html) have syntax in which a few characters are special constructs and the rest are ordinary. I will just go through the special constructs below, this would be similar to what the emacs tutorial says about regex, except I am putting it in the tabular format.

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<colgroup>
<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Regex</th>
<th scope="col" class="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td class="left">'.' (period)</td>
<td class="left">Matches any single character except a new line.</td>
</tr>

<tr>
<td class="left">'\*'</td>
<td class="left">Means to match preceding regular expression any no. of time as possible.</td>
</tr>

<tr>
<td class="left">'+'</td>
<td class="left">Matches the preceding expression atleast once.</td>
</tr>

<tr>
<td class="left">'?'</td>
<td class="left">Matches the expression either once or none.</td>
</tr>

<tr>
<td class="left">'\*?', '+?', '??'</td>
<td class="left">Non-greedy variants of above operators.</td>
</tr>

<tr>
<td class="left">'\\{N\\}'</td>
<td class="left">That the preceding regular expression matches exactly N times in a row.</td>
</tr>

<tr>
<td class="left">'\\{N,M\\}'</td>
<td class="left">Match N times but not more than M times.</td>
</tr>

<tr>
<td class="left">'[ &#x2026; ]'</td>
<td class="left">Set of character within the bracket.</td>
</tr>

<tr>
<td class="left">'[:char classes:]'</td>
<td class="left">Encloses character classes. [[</td>
</tr>

<tr>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
</tr>
</tbody>
</table>

## Searching and cases

While searching within emacs, emacs usually ignores the case of the text which is being searched through, when the search is specified in lower case, for example, searching for word 'nutrients' so while typing the word in incremental search will match 'nutrients' begining with either 'Nutri' and 'nutri'. Likewise, '[ab]' matches 'a', 'A', 'B', 'b'. Any appearance of the uppercase letter within the search makes the searches case-sensisive, thus, searching for 'Nutri' doesn't matches 'nutri' and 'NUTRI'. Typing *'M-c'* within an incremental search toggles the case sensetivity of that search.

When we set **case-fold-search** to nil then all the letters must match exactly incuding the case. This is per-buffer variable, setting this variable to a particular buffer will only affect that buffer and will have no effects on the other buffers. The effect of this variable applies to non-incremental searches and to the replace commands as well.

## Replaement commands

There is a simple replace command as **M-x replace-string** which replaces the occurunces in the buffer. **M-% command** is for query replace, which presents each occurence of the pattern and asks wether to replace it.

The replace command usually work from the point place where your cursor is to the end of the buffer. In an active region replace commands will work in that region only. The basic replace commands replaces one search string with one replacement string. **expand-region-abbrevs** makes emacs possible to perform several replacements in parellel. Replacement commands do not use lax space matching1 by default and can be enabled by changing the variable **replace-lax-withespaces** to **t**.

### Unconditional replacements
 
| Unconditional Replacements |
| --- | --- |
| M-x replace-string RET string RET newstring RET | Replace all string with new string |

This replace every occurence of the string with the new string _from the point to the end of the buffer_. For doing this in the whole buffer, you must begin with the beginning2 of the buffer. In an active region the replacement is limited to the region.

### Regexp replacement
Similarly,

| Regexp replcatement commands. |
|---------------------------------------------|-----------------------------------------------------|
| M-x replace-regexp RET regexp RET newstring |	Replace every match for regexp with the new string. |

Here the newstring need not required to be constant: it can refer to all or part of the string as matched by the regex. \& in newstring stands for the entire match being replaced. \d in newstring where d = digit, stands for whatever matched the d/th/ parenthesized grouping in regexp, also called as backrefrence. \# refers to the count of replacements already made in this command. \? will asks for the replacement string each time.

**Examples**: M-x replace-regexp RET c[ad]+r RET \&-safe RET : replaces cadr with cadr-safe and cddr with cddr-safe M-x replace-regexp RET c[ad]+r-safe RET \1 RET: performs the inverse of above.


### Command and case
Cases in emacs replace the similar way as it is in incremental search i.e. if the first argument of the replace command is all in lower case it ignores the cases. However, if the case-fold-search is set to nil, case would be significant in the searches.

### Query Replace

| Keybinding | Description |
|------------|-------------|
| M-% string RET newstring RET | Replaces some occurrences of string with newstring. |
| C-M-% regexp RET newstring RET | Replace some matches for regexp with new string. |

if you want to change only few occurrences and not all of them in the buffer the **M-% (query-replace)** will replace the words one by one and ask for your permission before doing it. Similarly, **C-M-%** performs performs regexp search and replace (query-replace-regexp). It works like replace-regexp except it queries like query-replace .

Character which are used when a match is shown in query-replace or **query-replace-regexp**

| Characters | Their actions while in query-replace |
|------------|--------------------------------------|
| SPC, y | Replace |
| DEL, n | Skip to next occurrence |
| , (comma) |	Replace and display result.|
| C-r |	To undo the replaced text. C-x u can also be used. |
| RET, q |	Exit without doing any more replacements. |
| . (period) | Replace this one and exit, do not replace any more. |
| ! (exclamation) | Replace everything do not ask me again. |
| Y (UPPERCASE) | Replace all remaining occurrences in all remaining buffer in multi-buffer replacements |
| N (UPPERCASE)	| Skip to the next buffer in the multi-buffer replacement without replacing remaining occurrences in the current buffer. |
| ^ (caret)	| Go back to the position of the previous occurrences. |
| C-w | to delete the occurrences and enter into recursive editing level. |
| e	| Edit the replacement string in the mini-buffer. This also becomes new replacement string for any further occurrences. |
| C-l | Re-display the screen. |
| C-h | Display message summarizing these options.|

### Some more commands for searching and looping

| Keybindings | Description |
|-------------|-------------|
| M-x multi-search-buffers | Prompt for one or more buffer name ending with RET. Do an incremental search in all the buffers. |
| M-x multi-isearch-buffers-regexp | same as multi-isearch-buffer, except it performs incremental regexp search. |
| M-x occur	| Prompt for a regexp and display a list showing each line in buffer that contains a match for it. To limit the search to part of the buffer, narrow to that part. In the occur buffer you can click on each entry or move point there and type RET, to visit the corresponding position in the buffer that was searched. o and C-o display the match in another window. Typing e in the occur buffer switches to occur edit mode, in which edits made to the entries are also applied to the text in originating buffer. Type C-c C-c to return to the occur mode. Command M-x list-matching-lines is synonymous to Occur mode. |
| M-s o	| Run occur using the last used search string. Running M-s o when the search is active used the current search string. |
| M-x multi-occur | This command is like occur, except it is able to search through buffers. It asks for the buffer names one-by-one. |
| M-x multi-occur-in-matching-buffers | Same as multi-occur, except the buffers to search are specified by regular expression which matches visited file names. |
| M-x how-many | Prompt for regexp and print for the number of matches for it in the buffer for point. |
| M-x flush-lines | Prompt for regexp and delete the line which contains the match for it, operating on the text after point. This deletes the current line if it contains the match starting after point. |
| M-x keep-lines | Prompt for regexp and deletes the line which doesn't contain the match regexp. This command always keeps the current line where the match is found. |

