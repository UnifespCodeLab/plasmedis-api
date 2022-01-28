import os
from flask_cors import cross_origin
from api import app
from api.controller import ( 
    users, 
    auth, 
    forms, 
    notifications, 
    comments, 
    posts, 
    privileges, 
    neighborhoods,
    categories
)

app.register_blueprint(comments.app)

# TODO: Mover para controller
@app.route('/status')
def hello():
    return f'This API Works! [{os.environ.get("ENV", "DEV")}]'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
