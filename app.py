from datetime import datetime

from flask.ext.script import Manager

from app import app, db
from app.models import User, Post

manager = Manager(app)


@manager.command
def init():
    dropdb()
    initdb()
    filldb()


@manager.command
def initdb():
    print('Initializing database...'),
    db.create_all()
    print('done!')


@manager.command
def filldb():
    print('Filling database...'),

    admin = User(u'maritza', u'maritza')
    db.session.add(admin)
    db.session.commit()

    post = Post(
        title=u'Hello, Veg Lovers!',
        markup=POST_1,
        author_id=admin.id,
        visible=True,
    )
    db.session.add(post)
    post.created = datetime(2011, 06, 13)
    post.update(post.title, post.markup, True)
    post = Post(
        title=u'Random Words 1',
        markup=POST_4,
        author_id=admin.id,
        visible=True,
    )
    db.session.add(post)
    post.created = datetime(2012, 8, 15)
    post.update(post.title, post.markup, True)
    post = Post(
        title=u'Random Words 2',
        markup=POST_2,
        author_id=admin.id,
        visible=True,
    )
    db.session.add(post)
    post.created = datetime(2012, 12, 24)
    post.update(post.title, post.markup, True)
    post = Post(
        title=u'My vegan dish!',
        markup=POST_3,
        author_id=admin.id,
        visible=True,
    )
    db.session.add(post)
    post = Post(
        title=u'Random Words 3',
        markup=POST_4,
        author_id=admin.id,
        visible=True,
    )
    db.session.add(post)
    post = Post(
        title=u'My project for IS211 is a Vegan Blog',
        markup=POST_5,
        author_id=admin.id,
        visible=True,
    )
    db.session.add(post)
    db.session.commit()
    print('done!')


@manager.command
def dropdb():
    print('Dropping database...'),
    db.drop_all()
    print('done!')


POST_1 = u"""
Learn vegan recipes and tips.

Nam quis urna est. Duis vel tincidunt quam. Vivamus odio tortor, suscipit vel
pretium quis, imperdiet quis dolor. Integer molestie enim nec risus malesuada
imperdiet. Donec pellentesque justo id sem tempor varius. Etiam ut tincidunt
lorem. Nullam a tellus sem.

### How to make coconut yogurt by the Minimalist Baker
<iframe width="560" height="315" src="https://www.youtube.com/embed/1O-0_fyVzjs" 
frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

Vestibulum a neque sed quam pharetra interdum. Quisque euismod dictum ipsum.
Vivamus tincidunt mi at tellus pharetra placerat. Sed sed sem nisi, sit amet
ultrices neque. Quisque eget turpis et sapien luctus auctor in ac magna.
"""


POST_2 = u"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vel ipsum
lectus. Pellentesque tempus enim sed leo imperdiet non lobortis nulla
sollicitudin. Maecenas arcu orci, interdum eu rhoncus ut, blandit id felis.
Mauris consectetur dui at felis ultricies tempus. Quisque molestie convallis
lectus vitae viverra. Duis lobortis ultrices turpis, nec eleifend est
venenatis nec. Sed sed lorem quis metus eleifend ullamcorper. Ut semper
nulla a arcu ornare **condimentum**.

Aliquam neque metus, posuere vitae condimentum ut, fermentum quis diam.
*Nulla facilisi*. Proin sapien felis, tristique eu venenatis at,
**accumsan** non dui. Vestibulum ante ipsum primis in faucibus orci luctus et
ultrices posuere cubilia.
"""


POST_3 = u"""
Maecenas ut gravida nisi. Aenean feugiat orci non quam vehicula accumsan.
Nullam scelerisque elementum sollicitudin. Sed vel tellus nisi, non tincidunt
augue. Aliquam at nulla ut sem mollis tincidunt.

![Vegan dish](https://images.pexels.com/photos/248509/pexels-photo-248509.jpeg)

Nam quis urna est. Duis vel tt quam. Vivamus odio tortor, suscipit vel
pretium quis, imperdiet quis dolor. Integer molestie enim nec risus malesuada
imperdiet. Donec pellentesque justo id sem tempor varius. Etiam ut tincidunt
lorem. Nullam a tellus sem.

Vestibulum a neque sed quam pharetra interdum. Quisque euismod dictum ipsum.
Vivamus tincidunt mi at tellus pharetra placerat. Sed sed sem nisi, sit amet
ultrices neque. Quisque eget turpis et sapien luctus auctor in ac magna.
Etiam rhoncus commodo molestie.
"""


POST_4 = u"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vel ipsum
lectus. Pellentesque tempus enim sed leo imperdiet non lobortis nulla
sollicitudin. Maecenas arcu orci, interdum eu rhoncus ut, blandit id felis.
Mauris consectetur dui at felis ultricies tempus. Quisque molestie convallis
lectus vitae viverra. Duis lobortis ultrices turpis, nec eleifend est
venenatis nec.

+ Quisque
+ Venenatis

Sed sed lorem quis metus eleifend ullamcorper. Ut semper nulla a arcu ornare
condimentum. Ut et lacus ac lacus pulvinar accumsan quis eget lacus. Integer
id nibh non eros tincidunt bibendum. Aenean diam lectus, tempus sed consequat
consectetur, posuere non ipsum. Donec vitae eleifend est. Donec at elit mi.
Maecenas tempor nulla gravida quam volutpat varius.

Vivamus malesuada viverra mauris sed dapibus. Aliquam erat volutpat. Aliquam
neque metus, posuere vitae condimentum ut, fermentum quis diam. Nulla
facilisi. Proin sapien felis, tristique eu venenatis at, accumsan non dui.
Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere
cubilia.
"""


POST_5 = u"""
To run *IS211 Course Project*, download the code from my [github](https://github.com/grochin1/IS211_Courseproject).

```python
python app.py init
python app.py runserver
```
"""


if __name__ == '__main__':
    manager.run()
