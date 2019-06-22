---
layout:     post
title:      "Ansible Quoting"
subtitle:   "Quoting in Ansible"
date:       "2019-02-10"
header-img: "img/"
published: true
tags: ["ansible", "imp"]
---

When quoting is necessary in Ansible. Quoting in Ansible is not as usual quoting works. Its a little complex at times we may need to use quotes under quotes to make things work. 

For example, if refrencing a variable right after specifying the module, the YAML parser will misinterpret the variable refrence as the beginning of an in-line dictonary. As seen in the below example.

{% raw %}
```yaml
    - name: performing a task
	  command: {{ my_command }} -a foo
```
{% endraw %}

Ansible here will read this YAML and try to parse the first part of {% raw %}`"{{ my_command }}" -a foo`{% endraw %} as a dictonary instead of a string, and thus returns an error. For handle this, the arguments must be quoted.
{% raw %}
```yaml
    - name: performing a task
	  command: "{{ my_command }} -a foo"
```
{% endraw %}
A similar problem comes with inline colons. As an example

{% raw %}
```yaml
    - name: debug something
	  debug: 
	    msg: "Debug message: some message "	
```
{% endraw %}

This colon is enough to confuse the YAML parser and give error. To fix this, we need to quote the entire argument string. But quoting the entire string will not also solve this problem and need to be handeled seperately


```yaml
    - name: debug something
	  debug: "msg: Debug message: some message."	
```


now this message will give you an error with an interesting way to fix this.

This one looks easy to fix.  It seems that there is a value started with a quote, and the YAML parser is expecting to see the line ended with the same kind of quote.  For instance:

    when: "ok" in result.stdout

Could be written as:

   when: '"ok" in result.stdout'

Or equivalently:

   when: "'ok' in result.stdout"

We could be wrong, but this one looks like it might be an issue with unbalanced quotes.  If starting a value with a quote, make sure the
line ends with the same set of quotes.  For instance this arbitrary example:

    foo: "bad" "wolf"

Could be written as:

    foo: '"bad" "wolf"'


	TASK [show debug message] *******************************************************************************************************************
	ok: [testserver] => {
		"msg": "Debug message: some message."
	}


and this is how to quote strings in YAML.
