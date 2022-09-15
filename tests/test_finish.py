import pytest
from rq_scheduler import Scheduler
from redis import Redis

r = Redis()
scheduler = Scheduler(queue_name="naya", connection=r)

def test_finish():
    for i in scheduler.get_jobs():
        print(i)
        assert i.is_finished