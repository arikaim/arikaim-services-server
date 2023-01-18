
from redis import Redis
from rq import Queue as RqQueue
from rq import Worker
from core.db.db import load_model_class
from core.logger import logger
from core.queue.job import Job

class Job:

    def __call__(self):
        logger.info('Job run obj')

test = Job()

class Queue:

    def __init__(self):
        self._redis = Redis()
        self._queue = RqQueue(connection = self._redis)
        self._worker = Worker([self._queue], connection = self._redis, name = 'jobs')
      
    def boot(self):
        logger.info('Init qeueue')
        self.remove_jobs()

        jobs = load_model_class('Jobs','jobs')
        
        self.add_job()

    def run(self):
        logger.info('Run qeueue worker')
        self._worker.work()

    def add_job(self,job = None):
        self._queue.enqueue(test)
        pass

    def get_jobs_count(self):
        return len(self._queue)

    def remove_jobs(self):
        self._queue.empty()

    @property
    def jobs(self):
        return self._queue.jobs







   
    