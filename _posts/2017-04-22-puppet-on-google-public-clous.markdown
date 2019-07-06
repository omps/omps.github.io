---
layout: post
title: "Puppet on GCP."
subtitle: "Setting up puppet on google cloud platform."
date: 2017-03-26
category: Devops
tags: puppet, googlecloud, automation, orchesteration
comments: true
author: omps
published: true
image: assets/images/puppet-meta.png
---

This is a quick document for my reference not much details in here. Will elaborate later.

File Locations:

Binary Files: /opt/puppetlabs/bin
Symlinks to : /opt/puppetlabs/puppet/bin

Main configuration files: /etc/puppetlabs/puppet main configuration file is puppet.configuration
Display data with puppet command.

    $ puppet agent --version To check the version
    $ puppet config print
    $ puppet config print confdir
    $ puppet conifg print certname
    $ puppet config print {confdir rundir ssldir runinterval(default to 30 mins.)}


Installing puppet master.

2 tasks

    - add puppet repos
    sudo yum install -y http://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm
    - install the server

Setting up directory environment

Checking the defaults for new environment

    sudo puppet config print modulepath --section master --environment test

Fixing the certificate

On the server: Stop Puppet Server.

On the CA server: Revoke and clean the server’s old certificate. (puppet cert clean <NAME>)

On the server: Delete the old certificate (and any old certificate signing requests) from the ssldir.

On the server: Run puppet agent -t --ca_server <CA HOSTNAME> to request a new certificate

On the CA server: Sign the certificate request, explicitly allowing alternate names (puppet cert sign --allow-dns-alt-names <NAME>).

On the server: Run puppet agent -t --ca_server <CA HOSTNAME> to retrieve the cert.

On the server: Start Puppet Server again.

https://docs.puppet.com/puppet/latest/configuration.html#dnsaltnames
