from redis import Redis
from rq import Queue
from rq.job import Job
from rq_scheduler import Scheduler
from datetime import datetime, timedelta
from codes.tasks import func

# scheduler = Scheduler(connection=Redis())
# r = Redis.from_url('redis://localhost:7739')
# q = Queue('test', connection=r)
# scheduler = Scheduler(queue=q, connection=r)
# scheduler = Scheduler(queue_name="naya", connection=Redis())
scheduler = Scheduler(queue_name="naya", connection=Redis())
# scheduler_foo = Scheduler('meow', connection=Redis(port=7739))

# queue = Queue('bar', connection=Redis())


if __name__ == "__main__":
    print(Job())
    l = [i for i in scheduler.get_jobs()]
    print([scheduler.get_jobs_to_queue()])
    print("jobs are: ", l)
    print("jobs are: ", l)
    print(len(l))
    
    # print(Job("c8243d3e-a647-4660-9cb8-72416f18c19d", Redis()))