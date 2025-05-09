from flask import Blueprint
main = Blueprint('main', __name__)

from flask import render_template, request
from flaskblog.models import Post

@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page',1, type = int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page = 5, page = page)
    return render_template('home.html', posts = posts)

@main.route('/about')
def about():
    return render_template('about.html', title = "About")