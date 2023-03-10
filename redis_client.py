import redis

from config import REDIS_PORT, REDIS_HOST


class RedisClient:
    def __init__(self):
        self.client = self._get_redis_client()

    @staticmethod
    def _get_redis_client():
        '''создаем подключение'''
        try:
            client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
            ping = client.ping()
            if ping:
                return client
        except redis.AuthenticationError:
            print('Ошибка подключения к Redis')
            raise redis.AuthenticationError
        except Exception as e:
            print(e)
            raise Exception

    def cache_user_data(self, user_tg_id, data):
        self.client.hmset(user_tg_id, mapping=data)

    def get_user_date(self, user_tg_id):
        return self.client.hgetall(user_tg_id)

    def del_user_data(self, user_tg_id):
        self.client.delete(user_tg_id)


redis_client = RedisClient()

if __name__ == '__main__':

    redis_client.cache_user_data(123, {'category': 87})
    # data = redis_client.get_user_date(123)
    data = redis_client.del_user_data(123)
    print(data)


