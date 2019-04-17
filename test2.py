from werkzeug.utils import escape
from werkzeug.wrappers import Request, Response
@Request.application
def hello_world(request):
    result = ['<title>Greeter</title>']
    if request.method == 'POST':
        result.append('<h1>Hello %s!</h1>' % escape(request.form['name']))
    result.append('''
        <form action="" method="post">
            <p>Name: <input type="text" name="name" size="20">
            <input type="submit" value="Greet me">
        </form>
    ''')
    return Response(''.join(result), mimetype='text/html')
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8080, hello_world)