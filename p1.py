from rq import Queue
import requests
from redis import Redis
from codes.tasks import count_words_at_url
import time


# Tell RQ what Redis connection to use
redis_conn = Redis()
# redis_conn = Redis(host="redis")
q = Queue(connection=redis_conn)  # no args implies the default queue

# print(count_words_at_url("http://nvie.com"))

# Delay execution of count_words_at_url('http://nvie.com')
job = q.enqueue(count_words_at_url, 'http://nvie.com')
print(job)
print(job.id)
print(job._status)
print(job.result)   # => None

# Now, wait a while, until the worker is finished
time.sleep(2)
print(job.result)   # => 889