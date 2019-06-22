---
layout: post
title: "opencart on ubuntu"
date: 2017-01-26 13:01:44 +0530
comments: true
categories: e-commerce
tags: #ecommerce, #web-applications, #opencart, #ubuntu, #e-commerce
googleplus_user: +OmPrakashomps
published: true
header-img: "img/opencartplusubuntu.png"
---


Opencart is a opensource store front and eCommerce platform  which provides the flexiblity and control for managing online stores. This document is going to tell you how to setup opencart on an ubuntu based system. I am intentinally avoiding to use any versions in it, but this document is made using Opencart 2.3.0.2 and Ubuntu 16.04. This whole setup(opencart with ubuntu) is running on an linode instance. Before we start I assume you are ready with you LAMP stack and you have already set your hostname pointing to the right server.

## PHP Settings.

Opencart requires certain PHP extensions.

```apt-get install php-mysql php-gd php-zip php-pclzip php-curl php-mcrypt```

## MySQL Credentials.

In case you do not need to use the root credentials, we need to create user credentials to work with mysql. Also, we do not want to use the default database, hence we shall create a seperate database and grant the newly created user some permissions on it.

Login to your mysql instance with root user.

On the MySql Prompt. type the below commands. Please note the (`;`), these are for ending the mysql commands.

Create Database and grant user permissions.

    create database webstore;
    grant all on webstore.* to 'opencart' identified by 'OC@123'; 
    flush privileges;


In the example above, `webstore` is the name of the database for your store, `opencart` is the username, and `OC@123` is the password. You may want to change these as per your requirement.

## Install opencart

Dowload the opencart installation file from [opencart's Download][https://www.opencart.com/index.php?route=cms/download] page.

Issue the following commands to download and unpack OpenCart:

    cd /opt
    wget http://opencart.googlecode.com/files/opencart_v1.5.1.1.zip
    unzip opencart_v1.5.1.1.zip

You will now need to move the files located in the "Upload" directory to your web root. For example, if you wanted your OpenCart installation to be located at `http://www.example.com`, your document root might look something like `/var/www/html/example.com/public_html`.

Next, you will need to make sure that OpenCart has access to write to specific folders and files. Issue the following commands:

    chmod 755 image/
    chmod 755 image/cache/
    chmod 755 image/data/
    chmod 755 cache/
    chmod 755 download/
    chmod 755 config.php
    chmod 755 admin/config.php
    chmod 755 system/cache/
    chmod 755 system/logs/

You may then visit your OpenCart instance via a web browser to continue with the installation process. In our example, this would be `http://www.example.com`.

Read and accept the license agreement, and make sure that the pre-installation checks are passed on the second page. Configure the database connection details by providing OpenCart with the MySQL credentials that you created earlier. Additionally, you will also create your administrator user at this time. Be sure to type your password and email address correctly!

Once you have completed the installation, be sure to delete the `install` directory by issuing the following command:

    rm -rf /srv/www/example.com/public_html/install

Congratulations! You are now ready to manage your own online storefront!


