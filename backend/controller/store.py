import redis
import json
from backend.controller.config import CONFIG
from backend.models.database import ZenMongo
import time


class Que(object):
    # def __init__(self, que_name, host=CONFIG['REDIS_IP'], port=CONFIG['REDIS_PORT'], db=0):
    def __init__(self, que_name, host='210.114.89.53', port='15900', db=0):
        # redis_server 생성
        self.rq = redis.StrictRedis(host, port, db)
        self.que_name = que_name

    def size(self):
        return self.rq.llen(self.que_name)

    def isEmpty(self):
        return self.size() == 0

    def put(self, element):
        self.rq.lpush(self.que_name, element)

    def get(self):
        element = self.rq.rpop(self.que_name)
        return element

    def get_without_pop(self):
        if self.isEmpty():
            return None
        element = self.rq.lindex(self.que_name, -1)
        return element

    def put_dict(self, dict):
        json_str = json.dumps(dict)
        self.put(json_str)

    def get_dict(self):
        element = self.get()
        if element is None:
            return None
        return json.loads(element)


# todo check
if __name__ == '__main__':
    zen_mongo = ZenMongo()
    que = Que('DIOT_EVENT_QUE')
    while True:
        dict = que.get_dict()
        if dict is not None:

            if dict['event'] == 'OwnerChangeRequest':
                # add event to db
                mongoResult = zen_mongo.add_event_Request(dict)
            else:
                mongoResult = zen_mongo.add_event_Accept(dict)
            print(dict)
        else:
            print("I'm waiting")
        time.sleep(1)

