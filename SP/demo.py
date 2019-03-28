import redis

class Redis:
    def __init__(self):
        '''连接'''
        self.__connect = redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)
        '''订阅频道'''
        self.sub = '456789'
        self.pub = '456789'

    def Publishing(self,info):
        #发布信息到指定的频道
        self.__connect.publish(self.pub,info)
        return True

    def Subscription(self):
        pub = self.__connect.pubsub()
        #订阅一个或者多个频道
        pub.subscribe(self.sub)
        pub.parse_response()
        return pub