---
layout: post
title: "working with octopress"
date: 2016-04-23 11:58:21 +0530
comments: true
categories: HOWTO
tags: octopress, howto, notes
---

### Good old saturday.

Well it is the good old saturday, when I planned to blog about something after around 2 weeks. 
<!--more-->
#### 2 Weeks earlier
Two weeks earlier I sat up, migrated my blog from pelican to octopress keeping the underlying githubpages intact, hardly did I know after two weeks, I will again face the similar problem like with pelican, In anycase this time I was determined not to rework again on migration to a new platform, and Instead I will fix what was missing and will try to resolve the issue with octopress only.

#### Today
My octopress did worked fine without any error, I made some cosmetic changes to the blog and published some post. The problem happened as the blog and the changes did not published, while I am making changes, the ```rake deploy``` did worked but I was not able to see anychanges happening to my blog page. But yes, the ```rake preview``` did worked fine and I was able to see my changes to localhost. Tried fixing it hard for sometimes but I didn't work. 

To make it work, I deleted my github.io repository from github, ran the command ```rake github_setup_pages``` pushed the content from my local repository back to github again, and well, after this I was able to see the changes on the web. That's a releif.

Finally, I made some cosmetic changes, write this as my notes on to what happened and how I fixed it. I also need to find out why it failed in the first place, I am assuming I changed my Laptop, that could be a reason, but this I am not convinced by this.

