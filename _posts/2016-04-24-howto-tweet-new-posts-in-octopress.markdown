---
layout: post
title: "Tweet Posts with Octopress"
date: 2016-04-24 08:19:20 +0530
comments: true
categories: howto
tags: #twitter,#octopress, #howto 
---

Thanks to the [blog post](http://fusion94.org/blog/2013/01/13/howto-tweet-new-posts-in-octopress/) by [Tony Guntharp](http://fusion94.org) who got inspired from another blog post by [Adnan Abdulhussein](http://blog.prydoni.us) on how to integrate twitter posting with [Octopress](http://octopress.org). His post was some 3 Years old and the [twitter gem](https://github.com/sferik/twitter) for [Octopress](http://octopress.org) version `5.16.0` has gone through a lot of changes, So technically I did some rewrite into the ruby configuration code and fixed it so I can post the tweets with the latest twitter gem.
<!--more-->
The basic idea remains the same taken from the predecessors blogs, you create a post and print the tweet message you want to give and it create a link to the post in the tweet_queue file. When the ```rake deploy``` task is called, it reads from the **tweet_queue** file and tweets what's in their line by line. This way you can create multiple posts at a time, and they all will be tweeted when you run your ```rake deploy``` task for your blog.

### Create a twitter application.
A twitter application is must to post to [twitter](http://www.twitter.com). Head over to https://apps.twitter.com/app/new, sign in and create a new application for your blog. 

In *settings*: ensure *read* and *write* is **enabled**.

In *Keys and access tokens*: take note of the following details.

* Consumer Keys
* Consumer Secret
* Access Token
* Access Token Secret

### Install the gem
We'll be using the [twitter gem](https://github.com/sferik/twitter) to update the status. Put the below line in your development ```Gemfile``` 

    gem twitter

from the terminal run ```bundle install```

### Configure Octopress to use twitter gem

Open the ```Rakefile``` in your favorite editor and add the below near the top with other required in the ```Rakefile```.

    require twitter

Add the following lines after the ```server_port``` line

```ruby Twitter Configuration
    # Twitter config (for tweeting posts)
    client = Twitter::REST::Client.new do |config|
      config.consumer_key = "YOUR_CONSUMER_KEY"
      config.consumer_secret = "YOUR_CONSUMER_SECRET"
      config.access_token = "YOUR_ACCESS_TOKEN""
      config.access_token_secret = "YOUR_ACCESS_TOKEN_SECRET
    end

    # MAKE SURE THERE IS A TRAILING SLASH, otherwise the linking won't work
    blog_url = "YOUR_BLOG_URL/"
```

ensure the trailing slash(/), It is required to append the date-name combination of the posts to form the url of the post.

### Modify the new_post rake task

Search for ```:new_post``` rake task in the ```Rakefile``` and replace the task with the following.

```ruby Modifying new_post task
# usage rake new_post[my-new-post] or rake new_post['my new post'] or rake new_post (defaults to "new-post")
desc "Begin a new post in #{source_dir}/#{posts_dir}"
task :new_post, :title, :tweet do |t, args|
  raise "### You haven't set anything up yet. First run `rake install` to set up an Octopress theme." unless File.directory?(source_dir)
  mkdir_p "#{source_dir}/#{posts_dir}"
  args.with_defaults(:title => 'new-post', :tweet => '')
  title = args.title
  filename = "#{source_dir}/#{posts_dir}/#{Time.now.strftime('%Y-%m-%d')}-#{title.to_url}.#{new_post_ext}"
  if File.exist?(filename)
    abort("rake aborted!") if ask("#{filename} already exists. Do you want to overwrite?", ['y', 'n']) == 'n'
  end
  puts "Creating new post: #{filename}"
  open(filename, 'w') do |post|
    post.puts "---"
    post.puts "layout: post"
    post.puts "title: \"#{title.gsub(/&/,'&amp;')}\""
    post.puts "date: #{Time.now.strftime('%Y-%m-%d %H:%M')}"
    post.puts "comments: true"
    post.puts "categories: "
    post.puts "---"
  end
  tweet = args.tweet
  if not tweet == ''
    # add to twitter status queue
    puts 'Adding post to tweet queue, it will be tweeted after deploying.'
    open('tweet_queue', 'a') do |file|
      file.puts "#{tweet} - #{blog_url}#{Time.now.strftime('%Y/%m/%d')}/#{title.to_url}/"
    end
  end
end
```

If you already have a modified task, the only changes are the task declaration ```(task :new_post, :title, :tweet do |t, args|)``` and the last few lines starting with ```tweet = args.tweet```.

### Setup to post tweets on deploy

Look for the `deplpoy_task` in the `Rakefile` and change or replace the files accordingly.

```ruby Deploy task
desc "Default deploy task"
task :deploy do
  # Check if preview posts exist, which should not be published
  if File.exists?(".preview-mode")
    puts "## Found posts in preview mode, regenerating files ..."
    File.delete(".preview-mode")
    Rake::Task[:generate].execute
  end

  Rake::Task[:copydot].invoke(source_dir, public_dir)
  Rake::Task["#{deploy_default}"].execute

  # Tweet
  next if not File.exists? 'tweet_queue'
  puts "Tweeting..."
  open('tweet_queue', 'r') do |file|
    while (line = file.gets)
      puts "Tweeting '#{line.gsub("\n", "")}' for @#{client.current_user.screen_name}..."
      client.update(line)
    end
  end
  puts "Deleting queue..."
  rm 'tweet_queue'
end
```

or just add the `#Tweet` task in deploy task.

### Usage

Now while creating your `new_post` you need to specify a separate message for the tweet when you create a post. This is the best way to give you the option of choosing whether you want to tweet the post or not. It also allows you to add @’s and #’s to the tweet message separately from the post title.

For Example:

The first part is the URL, and the second part is your tweet message.

    rake new_post["HowTo Tweet New Posts in Octopress","HowTo Tweet New Posts in Octopress @twitter"]

You should be able to see your new post generated by the rake task.

Once, this is done. Go Ahead and write into your post and `rake gen_deploy` should do the rest of it.
