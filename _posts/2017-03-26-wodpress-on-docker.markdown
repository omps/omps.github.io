---
layout: post
title: "Wordpress on Docker"
date: 2017-03-26
category: docker
tags: wordpress, docker
comments: true
---

## Install Docker
Install docker on to your system. Docker is only workable for 64 bit system. Install a 64 bit linux system, and further install docker on the same.

The installation document for different OSes can be found at. [Installation guide](https://docs.docker.com/engine/installation/)

## Install Mysql

Install mysql using docker.

     docker run --name wordpressdb -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=wordpress -d mysql:5.7
     
     
## Install wordpress

Install wordpress on docker

     docker run -e WORDPRESS_DB_PASSWORD=password -d --name wordpress --link wordpressdb:mysql -p 127.0.0.2:8080:80 -v "$PWD/":/var/www/html  wordpress


The $PWD is the local dir which is mapped to /var/www/html/
