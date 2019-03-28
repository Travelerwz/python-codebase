from demo import Redis

obj = Redis()
sub = obj.Subscription()

while(True):
    msg = sub.parse_response()
    print(msg)
    print(type(msg))