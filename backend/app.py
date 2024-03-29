from flask import Flask
from backend.controller.api import api_page
from backend.controller.views import view_page
from backend.models.database import ZenMongo
from backend.models.database import ZenMongo_resolve
from backend.controller.core import EthCore2
from backend.controller.config import CONFIG, Mode, ResCode
from backend.controller.core import OwnershipManager,KeyManager
from backend.controller.que import Que


core = EthCore2(url=CONFIG['RPC-URL'], mode=Mode.PRODUCT)
ownership_manager = OwnershipManager(core)
key_manager = KeyManager(passphrase='abcd')

app = Flask(__name__)

app.register_blueprint(view_page, url_prefix='/')
app.register_blueprint(api_page, url_prefix='/api')

# Redis connect
que = Que('DIOT_EVENT_QUE')
api_page.resource['redis'] = que
view_page.resource['redis'] = que


# DB connect
zen_mongo = ZenMongo()
api_page.resource['mongo'] = zen_mongo
view_page.resource['mongo'] = zen_mongo

# DB connect2
zen_mongo_resolve = ZenMongo_resolve()
api_page.resource['mongo_resolve'] = zen_mongo_resolve

api_page.resource['ownership_manager'] = ownership_manager
view_page.resource['ownership_manager'] = ownership_manager

api_page.resource['key_manager'] = key_manager
view_page.resource['key_manager'] = key_manager

api_page.resource['core'] = core
view_page.resource['core'] = core

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
