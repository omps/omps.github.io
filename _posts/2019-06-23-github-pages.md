---
layout:     post
title:      "Personal blog on Github Pages"
subtitle:   "Setting up GitHub pages for your blog."
date:       "2019-06-23"
image: "assets/images/gh-pages/gh_pages.jpg"
published: true
categories: HOW-TO
tags: ["Github", "Blog", "github-pages"]
featured: true
---

# What is Github
Github is a code hosting platform for collaboration and version control using git which is quite similar to SVN and Mercurial. Github allows us to work with other developers together on the projects. You can sign up for github at https://github.com

![Github_account](https://www.w3schools.com/whatis/img_github_account.jpg)

Essential components of Github are:
1. Repositories
2. Branches
3. Commits
4. Pull Request
5. [Git] (The version control software Github is built on.)

To learn more about git do visit the [git-scm] page.

## What is Github pages.

> GitHub Pages is a static site hosting service designed to host your personal, organization, or project pages directly from a GitHub repository.

Basically with Github pages you can host your static HTML site, like your portfolio, your blog on an information site, which do not require a lot of content-changes very frequently.

GitHub Pages is a static site hosting service and doesn't support server-side code such as, PHP, Ruby, or Python.

Ruby and Python can be used to generate static site though which can then be pushed into your repositories.

They are also not intended for or allowed to be used as a free web hosting service
GitHub Pages sites are subject to the following usage limits:

GitHub Pages source repositories have a recommended limit of 1GB .

Published GitHub Pages sites may be no larger than 1 GB.

GitHub Pages sites have a soft bandwidth limit of 100GB per month.

GitHub Pages sites have a soft limit of to run our online businesses, e-commerce sites, or any other website that is primarily directed at either facilitating commercial transactions or providing commercial software as a service (SaaS).

### Limitations

GH Pages sites are subject to the following usage limits:

* The source repositories hosting your blog have a recommended limit of 1GB .
* Published sites cannot be no larger than 1 GB.
* The sites will have a soft bandwidth limit of 100GB per month.
* And your site will only be build for 10 times in an hour, if you are using Jekyll or pelican as static site generator.

While you have hosted your content on the GitHub pages. Please also make sure you follow these guidelines and must refrain from:
* Content or activity that is illegal or otherwise prohibited by our Terms of Service or Community Guidelines
* Violent or threatening content or activity
* Excessive automated bulk activity (for example, spamming)
* Activity that compromises GitHub users or GitHub services
* Get-rich-quick schemes
* Sexually obscene content
* Content that misrepresents your identity or site purpose

## Why Github Pages
GitHub pages uses static sites technically, a static website is only HTML and CSS and doesn't involve scripting. To change the content which appears source code needs to be edited directly. In simple words, the content of the website will remain same for every visit whereas for dynamic sites the content will keep on changing. For e.g. the news feed of facebook is a dynamic site, but book review site can be a static site, since the content remains constant for somtime.  There are many reasons which makes a static site desirable than a dynamic site as follows:

### 1. Security
Static websites are a safe bet compared to dynamic ones when it comes to security as they don't rely on CMS plugins. APIs and JavaScript are used to handle the dynamic functions of static websites, eliminating the risk of getting hacked. On the other hand, active websites are highly prone to get hacked due to multiple content sources and plugins.

A report by WP WhiteSecurity states that about 70% of WordPress sites are at risk of getting hacked by malicious hackers because of lack of maintenance and upgrading. Ugh, scary.

### 2. Reliability
You must have occasionally come across an error message saying that, "The connection could not be established.â This primarily occurs because of the database errors. Serving just basic HTML files makes it easier to host them anywhere with ease like on a CDN.
Hence, whenever there'd be an attack on the server, the static website is just redirected to other closest node, unlike its dynamic alternative where the website might go down for few hours.

### 3. Speed
The absence of middleman/database makes the static site much more speedy and easy to load.
A static site is ten times faster than a dynamic site that is built with a CMS. Another reason for a static website to run faster is that it can be served from the node closest to the browser.

[According to research by Kissmetrics], about 47% of people expect the website to load within 2 seconds, and a whopping 40% of people will not wait for the website to load for longer than 3 seconds. Hence, getting a static website also helps in getting more traffic by reducing abandonment rate caused due to slow loading.
![Page Load Time](/assets/images/gh-pages/loading-time-sml.jpg)

### Hosting and Price
Static websites have basic HTML files which require less space making the hosting of these websites cheaper to that of dynamic websites. Organizations with static website save up on the costs and channel those resources to integrate Git or automated builds to incorporate the latest changes in the system.

### Scalablity
What to do when your website is finally up and running? Handling massive traffic on a dynamic website might be a cumbersome process as it requires complex code playing on the server. Basic static websites with HTML files can be easily scaled up by just increasing the bandwidth.

### Technological advancements.

There was a time when online store websites would have to rely on dynamic websites for their organization and integrate those complex coding and deal with tedious scripting.

With tools like Magento, it is possible to have a static website for shop-centric businesses. A Java-script based shopping cart, called Snipcart, integrates e-commerce site’s functionalities to a static website, eliminating the need for dynamic websites. Snipcart dashboard can manage sales and product inventories, and its API can be integrated with shipping service providers and inventory management software systems as well.

With some static generators and static website hosting platforms that allow Github integration, global CDN, SSL certificates along with free custom domains. Hosting providers such Netlify, go up the notch and even deal with redirects such as 404 errors, proxies, and even password protection.

Therefore, it is safe to say that static websites have made a terrific comeback and they are here to stay with more advantages than drawbacks. As a website is a digital face of the business, organizations must take into consideration all the factors and necessities of their business website and must assess all the new tools and platforms before making a website.

![online stores](/assets/images/gh-pages/website-1624028-1280.png)

## What are the requirements for hosting on github pages
- You need to have a github account, register [here].
- enable gh-pages for your repository.
- you can access the repository as <reponame>.github.io

## How to Do GitHub hosting.

### Create a repository
Head over to GitHub and create a new repository named username.github.io, where username is your username (or organization name) on GitHub.
![Create repository](/assets/images/gh-pages/user-repo@2x.png)
If the first part of the repository doesn’t exactly match your username, it won’t work, so make sure to get it right.


### Clone the repository
Go to the folder where you want to store your project, and clone the new repository:

    ~ $ git clone https://github.com/username/username.github.io    

### Hello World
Enter the project folder and add an index.html file:

    ~ $ cd username.github.io
    ~ $ echo "Hello World" > index.html

### Push it
Add, commit, and push your changes:

    ~ $ git add --all
    ~ $ git commit -m "Initial commit"
    ~ $ git push -u origin master

…and you're done!


Fire up a browser and go to https://username.github.io.

Once this is done learn to [set your custom domain].





[Git]:https://git-scm.com
[git-scm]:https://git-scm.com/doc
[According to research by Kissmetrics]: https://neilpatel.com/blog/loading-time/
[Page Load Time]:https://blog.kissmetrics.com/loading-time/
[here]:https://github.com
[set your custom domain]:https://www.omps.in/2019-06-22-https-github-cloudflare.html
