from redis import Redis
from rq import Queue
from rq.job import Job
from rq_scheduler import Scheduler
from datetime import datetime, timedelta
from runner import sucp

# scheduler = Scheduler(connection=Redis())
r = Redis()
# q = Queue('test', connection=r)
# scheduler = Scheduler(queue=q, connection=r)
scheduler = Scheduler(queue_name="after_4", connection=r)
# scheduler_foo = Scheduler('meow', connection=Redis(port=7739))

# queue = Queue('bar', connection=Redis())


if __name__ == "__main__":
    # f = scheduler.enqueue_at(datetime(2022, 9, 15, 15, 55, 0), func, 1)
    f = scheduler.enqueue_in(timedelta(seconds=2), sucp , 3)
    print("THE JOB STATUS IS", f.get_status())
    print("TIME IS NOW", datetime.now())
    # f = scheduler.enqueue_in(timedelta(seconds=2), func , 3)
    # f = scheduler.enqueue_in(timedelta(seconds=2), func , 3)
    # print("THE SCHEDULER IS", f)
    # print("THE SCHEDULER job id", f.id)
    # scheduler_foo.enqueue_in(timedelta(seconds=1), func, 3)
    # for i in scheduler.get_jobs():
    #     print(i)
        # print(i)
    # scheduler_foo.enqueue_at(datetime(2022, 9, 15, 13, 49, 0), func)