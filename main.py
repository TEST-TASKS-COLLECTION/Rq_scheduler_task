from redis import Redis
from rq import Queue
from rq.job import Job

from rq_scheduler import Scheduler
from datetime import datetime, timedelta
from codes.tasks import task1
# from mero_func import noice

# scheduler = Scheduler(connection=Redis())
# r = Redis(port=7739)
r = Redis() # local
# r = Redis(host="redis") # inside of docker
q = Queue(connection=r)
# q = Queue('test', connection=r)
# scheduler = Scheduler(queue=q, connection=r)
scheduler = Scheduler(queue=q, connection=r)
# scheduler_foo = Scheduler('meow', connection=Redis(port=7739))

# queue = Queue('bar', connection=Redis())


if __name__ == "__main__":
    # f = scheduler.enqueue_at(datetime(2022, 9, 15, 15, 55, 0), func, 1)
    # f = scheduler.enqueue_in(timedelta(seconds=2), sucp )
    # print("THE JOB STATUS IS", f.get_status())
    # print(task1(3))
    print("TIME IS NOW", datetime.now())
    job = q.enqueue(task1, 3)
    # scheduler.schedule(
    #     scheduled_time=datetime.utcnow(), # Time for first execution, in UTC timezone
    #     func=sucp,                     # Function to be queued
    #     args=[2, 3],             # Arguments passed into function when executed
    #     # kwargs={'foo': 'bar'},         # Keyword arguments passed into function when executed
    #     interval=60,                   # Time before the function is called again, in seconds
    #     repeat=10,                     # Repeat this number of times (None means repeat forever)
    #     meta={'foo': 'bar'}            # Arbitrary pickleable data on the job itself
    # )
    # f = scheduler.enqueue_in(timedelta(seconds=2), func , 3)
    # f = scheduler.enqueue_in(timedelta(seconds=2), func , 3)
    # print("THE SCHEDULER IS", f)
    # print("THE SCHEDULER job id", f.id)
    # scheduler_foo.enqueue_in(timedelta(seconds=1), func, 3)
    # for i in scheduler.get_jobs():
    #     print(i)
        # print(i)
    # scheduler_foo.enqueue_at(datetime(2022, 9, 15, 13, 49, 0), func)