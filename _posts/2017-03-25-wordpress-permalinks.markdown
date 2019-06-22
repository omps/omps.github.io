---
layout: post
title: "Wordpress permalinks."
date: 2017-03-25
category: wordpress
tags: wordpress, permalinks, apache
comments: true
---

Everytime I need to setup permalinks, I miss some of the important things to check before hand. This is my document to setup wordpress permalinks.

## Working with wordpress permalinks.
Wordpress Permalinks are important to beautify your wordpress blog links.

### Configuring apache.
Ensure you have mod_rewrite enabled.

I have apache2 setup so its pretty simple to setup mod_rewrite in there.

```# a2enmod rewrite```

```# service apache2 restart```

This enables mod_rewrite for apache.

<em>checked using the phpinfo page</em>

### Configure your site.
Need to configure your apache site to use or enable it to use mod_rewrite feature.

Inside your <Directory></Directory> block enable AllowOverride.

    <Directory>
         AllowOverride All
    </Directory>

### Configure your wordpress.
Go to wordpress and configure your permalinks. The permalinks create the .htaaccess file in your document root.



Well All this is help you setup permalinks for wordpress.
