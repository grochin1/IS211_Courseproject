

# Flask-Blog : Blog Application Details


## Requirements 

The purpose of this web application is to give a user the ability to run their own blog. A blog is just a series of posts made by an author. Each post has a title, a published date, an author, and textual (HTML) content. When first loading the application at the root URL, the user should be presented with a list of available posts listed in reverse chronological order (newest posts first). The application should allow a user to login via the ‘/login’ URL, which gives that user the ability to make changes to the blog.

## Login method


After logging in, the user should be sent to the ‘/dashboard’ page, which presents the user with an interface that:
1. Shows a list of their posts in a table. This list just shows the title of the post, with buttons labeled ‘Edit’ and ‘Delete’. This edit button will take the user to a page that allows them to update the post. The delete button will simply delete that post.

2. Allows the user to add a new post (This can be done either directly on the dashboard page or on a new page).



Simple blog with an administrator area created for Project IS211



## Install


### Python Packages


    $ pip install -r requirements.txt

### Initialize

The following command will create all tables and fill the database with dummy
blog posts. I created a post of a dish I like!

    $ python app.py init


## Run

    $ python app.py runserver

Login with **maritza** as default username and password. (Both username and password is same) Just add /login to the
url or press the login icon at the top of the page.
