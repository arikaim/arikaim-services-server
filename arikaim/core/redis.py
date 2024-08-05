import redis as r

redis = None

def redis_connect(config = None):
    global redis
    if config == False:
        redis = None
        return None
    
    if not config:
        redis = r.Redis()
    else:
        redis = r.Redis(config)
     
    return redis
