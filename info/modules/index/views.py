from flask import current_app
from info import redis_store
from . import index_blu
from flask import  render_template

@index_blu.route('/')
def index():
    # 向redis中保存一个值 name itcast
    return render_template('news/index.html')

@index_blu.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/favicon.ico')