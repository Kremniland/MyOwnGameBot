import redis

from config import REDIS_PORT, REDIS_HOST


class RedisClient:
    def __init__(self):
        self.client = self._get_redis_client()

    @staticmethod
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


redis_client = RedisClient()

if __name__ == '__main__':
    print(redis_client)
