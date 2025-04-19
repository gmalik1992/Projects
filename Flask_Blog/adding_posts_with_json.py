from flaskblog import db
import json
import os
from flaskblog.models import User, Post

with open('/Users/gobind/Documents/PycharmProjects/Flask_Blog/flaskblog/posts_file.json') as f:
    all_posts = json.load(f)
for post in all_posts:
    title = post.get('title')
    content = post.get('content')
    user_id = post.get('user_id')
    # print(f'{title}\n{content}\n{user_id}')
    # print('*************************************************************************************')
    from_user = User.query.get(int(user_id))
    post = Post(title=title, content=content, author=from_user)
    db.session.add(post)
db.session.commit()
print(os.getcwd())