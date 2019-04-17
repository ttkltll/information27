# 该模块是用于保存当前项目所有的业务逻辑模块，比如：首页、新闻详情页、个人中心、后台管理
# 登录注册的相关业务逻辑都放在当前模块

from flask import Blueprint

# 创建蓝图对象
profile_blu = Blueprint("profile", __name__, url_prefix="/user")


from . import views
