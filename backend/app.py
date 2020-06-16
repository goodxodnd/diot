from flask import Flask
from backend.controller.api import api_page
from backend.controller.views import view_page
from backend.models.database import ZenMongo


app = Flask(__name__)

app.register_blueprint(view_page, url_prefix='/')
app.register_blueprint(api_page, url_prefix='/api')


@app.route('/')
def hello_world():
    return 'Hello World!'


# DB connect
zen_mongo = ZenMongo()
api_page.resource['mongo'] = zen_mongo
view_page.resource['mongo'] = zen_mongo


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
