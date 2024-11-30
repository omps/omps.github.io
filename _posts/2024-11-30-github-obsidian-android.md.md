---
layout: post
title: Blogging from Android with github and obsidian
author: Om Prakash Singh
categories:
  - Blogging
image: 
rating: 3
published: true
date: "2024-11-30"
---

This is my obsidian blog pipeline.

Requirements
1. obsidian to blog
2. Jekyll to publish
3. github to version control and source control
4. github to publish static pages

I am using android to write my blog on obsidian. Using memory card for storing blog data.

I installed termux and using termux has configured and compiled all the tools.

In Termux I have installed
- Git
- Jekyll

Installed hugo site using 
$ hugo new site <site name for my blog> --format yaml

I am using YAML instead of TOML as YAML is easier to read.

I am using paper mod theme. Inside your new project folder download using github submodule method

```
git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
git submodule update --init --recursive # needed when you reclone your repo (submodules may not get cloned automatically)
git submodule update --remote --merge
```


I am using nano for any kind of configuration I am doing for my hugo site.

- 