#Introduction to Web Scraping

#An important first note:

The following lesson has a bunch of code in it, to get the most out of this lesson you should actually try all of this code.  That means typing it in, as shown in the lesson.  Just because I wrote something down, it doesn't mean you'll be able to make it run too.  There are dependency issues, files maybe missing, your computer may have an issue.  You need to ensure everything I am doing is reproducible on your system.  And the only way to do that, is to actually try it out!

##Definition: Web Scraping

Web scraping is the process of taking content which is hosted somewhere on the internet and downloading it locally to your computer

##Example:

Have you ever openned a browser and right-clicked and then selected "save as"?  Then you already understand the concept!  

##Exercise One:

open a browser (preferrably google chrome) and go to https://www.google.com
Then right click any where on the page and selected save as.  Save the file as google.html to a folder you will remember (the easiest place is your desktop).  Then open the google.html file by double clicking on it.  It should open in your browser, but it shouldn't look exactly right.

The reason for this is actually pretty simple.  Some of the content displayed on google's home page is dynamic(this word should be italized), however since you are accessing the html "locally" you only see the static(this word should be italized) part of the webpage.

##Larger point:

Web pages are broken down into two pieces: the static content and the dynamic content.  The techniques we will learn in this first tutorial will only be helpful for downloading static content.

##Definition: Static content

Static content is any content that does not require an internet connection to view.  

##Examples:

Text, hyper links, text markup are all static elements of an html page

##Definition: Dynamic content

Dynamic content will always require a connection to the internet to view or "consume" however this content can still be downloaded, just by very different means.

##Examples:

images, javascript functions, interactive maps, advanced markup, videos and other more "interactive" pieces of content on webpages will all be considered dynamic content.

#Getting Started

##The requests library

Python comes with a number of libraries for downloading content locally.  My personal favorite library is the requests library.  It doesn't come built into python, but can be installed very easily.

##Installation:

open a terminal and type the following:

sudo pip install requests

Note:  This will only work if you have installed pip 

###Installing pip

###On Windows:

Windows does not natively support pip however you can get it with cygwin.  Head over to (cygwin's url) here and download it.  This will give you access to a linux terminal in windows.

###On Mac:

You should be able to download and install pip normally.  Just head over to (url for getting pip).  Next you'll need to hit command A (which should select all the text on the page) and then command C (which shoudl copy all the text on the page).  Next open a text editor (I personally love emacs) and paste in the code.  Next all you need to do is save the file as get-pip.py and save it to someplace you can remember.  Now open a terminal and navigate to the file.  (if you don't know how to do this yet, I highly recommend some of the introductory material).  Then run the following:

sudo python get-pip.py

###On Linux:

I will only cover Ubuntu here.  If you are using another version of linux I am sure you can figure it out ;)

You should be able to download and install pip normally.  Just head over to (url for getting pip). Next you'll need to hit command A (which should select all the text on the page) and then command C (which shoudl copy all the text on the page).  Next open a text editor (I personally love emacs) and paste in the code.  Next all you need to do is save the file as get-pip.py and save it to someplace you can remember.  Now open a terminal and navigate to the file.  (if you don't know how to do this yet, I highly recommend some of the introductory material).  Then run the following:

sudo python get-pip.py

##Testing things out

At this point you should have pip and requests installed.  If this hasn't happened you may want to seek help from your mentor.  

Now, open a terminal and type python

This should load an interactive python shell called a REPL (Read Evaluate Print Loop).  

Now type in the following line:

import requests

If you didn't get any errors that means you successfully installed requests.  Good job!

#Sub-project 1

##Downloading content from the net

Now that you have requests, let's do(italize this) something with it.  For these shorter exercises you might be better off with Ipython notebook or just using the REPL.  However you can certainly write programs in a text editor.  As your programs become longer (anything over 20 lines) you should absolutely write and then "compile" your code.  (By this I mean saving things to files and then running them from the command line or your IDE).

So, I'm just going to do this one from the command line:

Open a terminal and type:

python

From REPL.

import requests
response = requests.get("https://www.google.com")
print response #the object - how to add python comments to markdown?!?!
print response.text #the html result of the object - HOW?!

If the above did not work for you then you may not have an internet connection OR you didn't install requests properly.  Please install you do so before proceeding.

##Saving to a file

Python comes with a number of ways to save to a file.  Here we'll look at the simplest one.  

a_file = open("thing.txt","w") #open a file for writing
a_file.write("Hello, World") #write to the file
a_file.close() #close the file

If the above the code looks weird, just think about the steps you would actually take when openning a file and writing some content.  The open function does exactly what you think it does, it opens the file.  The program needs to know the file name to open and what you want to do once the file is openned.  The second parameter, w, stands for writing and allows you to send content to the file.  On the next line, we actually tell the program what content we want to write to the file.  In this case, "Hello, World".  Finally, we close the file, just like you would when you are finished writing an essay or a term paper.  

Don't worry about why you need to do things in this way for now, that's a question you get into a lot in an operating systems class. 

##Putting it all together

Now that we know how to download content from the internet and we know how to save our work to a file, we are ready to replicate the "save as" operation we did eariler, manually.  But now we can do it programmatically!

##Exercise

Try to combine the above steps to create a program that downloads the content from https://www.google.com and saves it locally.  If you get stuck don't worry!  The answer is below, however you want have the answers to all future exercises, just this one.  



--Space left intentionally blank --














Okay, so did you do it or get stuck?  Time to check your answer:

import requests
response = requests.get("https://www.google.com")
a_file = open("google.html","w")
a_file.write(response.text)
a_file.close()


##Parsing Web Pages

Now that we can successfully download content from the web, the next step is to get meaningful information from those web pages.  In order to do that we'll need to parse(itialize) the web page.  

###Definition: Parse

In this context, parsing means breaking down some larger content into it's component pieces.  So when you are parsing a web page you are creating an organizational structure that allows you to easily access specific pieces for easier analysis.

### Enter lxml

The lxml library happens to be a personal favorite and is totally worth learning.  It isn't as simple as some other parsing libraries, however it is far faster (in terms of performance).  I've never found a web page that couldn't be easily parsed with lxml, although I've been told they exist.  

So, how does it work?  The lxml library takes advantage of something called xpath, which is a tiny language used to traverse documents.  If that sounds scray, don't worry!  We're about to explain.  But first, I want to show you an example of how you can use lxml.

### Example

import requests
import lxml.html

response = requests.get("https://www.google.com")
html = lxml.html.fromstring(response.text)
links = html.xpath("//a/@href")
print links

The above example goes to google.com and then downloads the page.  Then in memory (which means while the program is running) lxml parsing the program and gives you back all the hyper links on the page!  A hyper link is just a way of going from one web page to another by clicking on the highlighted text.  But this actually gives you the addresses of those different pages.

## Document traversal

Before we can understand what xpath is, or how it really works, we need to understand what an "html document" really is.  

### The html standard

HTML stands for hyper text markup language.  An HTML page is organized as a series of tags.  Go to any web page and right click and then select view source.  What you'll see is a whole bunch of things that look like this: <p>Some content </p>.  The <p> called the p-tag stands for paragraph.  There a whole host of these tags.  Some of them include, <a>, <p>, <html>, <img>, and <script>.

HTML tags have a hierarchical structure, meaning that tags wrap other tags.  Each tag does something different to the content inside of it, so if you want a piece of text to have multiple behaviors, you'll usually wrap it in multiple tags.  Here's an example:

<strong><a href="https://www.google.com">Google's homepage</a></strong>

The strong-tag wraps around the a-tag, thus allowing the text to look different.  If we removed the strong-tag then an html page with this would look differently.  

So! Generalizing we get the following:

All tags on an HTML page are actually wrapped by the <html> tag, and in turn the <head> and <body> tags wrap everything else.  The body is the content actually displayed to the user and the head is used to help make those pages look pretty or do some stuff behind the scenes.  

Now, let's talk about xpath.

The xpath language can be used to easily get to specific content by taking advantage of the hierarchical structure of html documents.  This structure imposes an ordering on the content in any html page, meaning we can always find what we are looking for, assuming we know what that is.

So how is this traversal?

Well, when a program is actually looking through the html document it does this:

Read in the first tag (always <html>), then look at the tags this tag contains.  In this case, that will be the head and body tags.  Then look in each of the tags that head and body contain and so on and so forth.  Eventually the entire document will be mapped out and we'll know where everything is.

In the simple example above:

import requests
import lxml.html

response = requests.get("https://www.google.com")
html = lxml.html.fromstring(response.text)
links = html.xpath("//a/@href")
print links

We were looking for all of the a tags, as specified by html.xpath("//a/@href").  So we are now really to break this statement down further.

// - this precedes any tags and tells the program to look for any a-tags anywhere in the document.  This is done by traversing the document and looking for any a-tag.
@ - The @ symbol must preface an attribute of an tag.  The href attribute is used to tell the a tag where to send the browser when a link is clicked on.  So if we want the link address we simply ask for the href attribute.

/ - looks only one level deeper into the html document or can be used, as above to find the attribute of a given tag.

So //a/@href says - find me all the tags and then save all of their hyperlinks to a python list.

Exercises: