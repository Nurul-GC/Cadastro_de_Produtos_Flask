from Main import app


@app.route('/index/')
@app.route('/')
def index():
    return 'ok'
