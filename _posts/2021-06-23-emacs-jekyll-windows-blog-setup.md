Finally, a long time, i decided to reblog using emacs and jekyll, i tried to maintain an alternate blog on omps.in, the github blog would mainly only be for my quickblogs, after reading an article by one of the perl developers i again felt a tinge of encouragement to start blogging, i do blog but that is very randon, once in a month or like that, most of the time i spend in proffreading and correcting what I had written, But after reading "Flavio Poletti" blog at https://github.polettix.it/ETOOBUSY/2021/06/23/pwc118-binary-palindrome/ I feel encouraged to start my blogging jounrey again. So before i begin this would be my setup for quick blog.

For my Quick blogging setup, I will be using a windows laptop, with emacs installed on it, the guide and tutorial for emace installation can easily be found at the GNU ftp site at https://ftp.gnu.org/gnu/emacs/windows/

The are certain pre-requisites to be added for making Jekyll work on your windows laptop.

- Install Ruby
  Install the latest version of Ruby from (here)[https://rubyinstaller.org/downloads/]

- Install Gems for Jekyll to start blogging
  gem install jekyll bundler jekyll-sitemap pygments.rb

- INstall git for windows
  git fir windows download link https://git-scm.com/download/win

- Setup your emacs
-- Install org-blog in your emacs
-- Install Magit for git control in emacs




** Now we setup our blog, populate it using a Jekyll template structure and push it to Github, at this point we are now live with our blogging


We are still missing on how we are going to write blog post in Org-Mode, and convert them to be parsed by Jekyll and hosted on our Github pages. To achieve this we will be relying a lot on Emacs publishing engine(org-publish) which will convert the org pages into html pages. There are ways on how you want to structure your blog structure, depending on whether one wants to write all pages including front page or about page etc using org or just the posts.

but for the sake of simplicity we will use wrting only the posts page with org-mode and not any other pages. We will setup two things

A sub-directory to store post pages

mkdir _org && cd _org

and a minimal cofiguration for publishing org-mode files in our system by adding the following in our ~/.emacs, so the html exports end up in the right location

#+begin_src emacs
(setq org-publish-project-alist
      '(("omps.github.io" ;; my blog project (just a name)
         ;; Path to org files.
         :base-directory "d:/Users/singho/Projects/omps.github.io/_org"
         :base-extension "org"
         ;; Path to Jekyll Posts
         :publishing-directory "d:/users/singho/projects/omps.github.io/_posts"
         :recursive t
         :publishing-function org-html-publish-to-html
         :headline-levels 4
         :html-extension "html"
         :body-only t
         )))

#+end_src
