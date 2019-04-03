import functools

def user_login_data(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    return wrapper


# @app.route('/news/<int:news_id>')
@user_login_data
def num1():
    print("aaa")


# @app.route('/')
@user_login_data
def num2():
    print("bbbb")

if __name__ == '__main__':
    print(num1.__name__)
    print(num2.__name__)
