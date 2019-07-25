import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import datetime
import re, string

blog_path = "/Users/omps/projects/omps.in/omps.github.io/_drafts/"


# Finding what month we are in.
d = datetime.date.today()
month = d.strftime('%m')

def gen_blog_title():
    month_name = d.strftime('%B')
    year = d.strftime('%Y')
    title = "What's new at AWS in the Month of %s %s" % (month_name, year)
    return title

def create_file():
        a = re.sub('[%s]' % re.escape(string.punctuation), '', gen_blog_title())
        filename = "-".join(a.split())
        return blog_path + d.strftime('%Y-%m-%d') + "-" + filename.lower() + ".markdown"

filename = create_file()


# Function for generating url
def generate_url(link):
    url = 'https:%s' % (link)
    return url

# html parser
def html_parser(url):
    response = requests.get(url)
    parsedhtml = BeautifulSoup(response.text, "html.parser")
    return parsedhtml

# # Collec the title of the page
# def get_title(data):
#     return data.title

def get_content(data):
    aws_text_box = data.find_all('div', class_='aws-text-box')
    return aws_text_box



# Adding the month to the URL, we are looking for the content of this month only.
url = "https://aws.amazon.com/about-aws/whats-new/2019/%s/" % (month)
response = requests.get(url)

# Handling over the date to BeautifulSoup for parsing
soup = html_parser(url) # BeautifulSoup(response.text, "html.parser")

# Collecting links
aws_stories = soup.find_all("a", string="Read More »")

# collect all the link in the list.
links = []
for i in aws_stories:
    links.append("https:%s" % (i['href']))

# Now go to each link and read its content.
blog = open(filename, "w")
blog.flush()
for url in links:
    content = html_parser(url)
    blog.write(md(content.h1))
    blog.write(md(get_content(content)))
    time.sleep(5)

blog.close()
