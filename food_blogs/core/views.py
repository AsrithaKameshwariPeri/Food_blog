from flask import render_template,request,Blueprint,jsonify
from food_blogs.models import BlogPost

core = Blueprint('core',__name__)

@core.route('/')

def index():
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    if blog_posts:

        return render_template('index.html', blog_posts=blog_posts)
    return jsonify({"status":"No data found"})
@core.route('/info')
def info():
    return render_template('info.html')