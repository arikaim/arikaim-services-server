
from redis import Redis
from rq import Queue as RqQueue
from rq_scheduler import Scheduler
from rq import Worker
from core.db.db import load_model_class
from core.logger import logger
from core.queue.job import Job
from core.path import Path
import os, imp
import datetime


class Queue:

    def __init__(self):
        self._redis = Redis()
        self._queue = RqQueue(connection = self._redis)
        self._worker = Worker([self._queue], connection = self._redis, name = 'jobs')
        self._scheduler = Scheduler( connection = self._redis) 

    def boot(self):
        logger.info('Init qeueue')
        self.remove_jobs()

        jobs = load_model_class('Jobs','jobs')
        
    def run(self):
        logger.info('Run qeueue worker')
        self._worker.work()

    def add_job(self, job = None):
        if isinstance(job,Job) == True:        
            if not job.interval:  
                self._queue.enqueue(job)
            else:
                # recurring job job
                self._scheduler.schedule(
                    scheduled_time = datetime.utcnow(), 
                    func = job,                                                  
                    interval = job.interval, # in seconds
                    repeat = None
                )
        pass

    def get_jobs_count(self):
        return len(self._queue)

    def remove_jobs(self):
        self._queue.empty()

    @property
    def jobs(self):
        return self._queue.jobs

    def create_job(self, job_class_name: str, module_name: str, service_name: str):
        path = os.path.join(Path.job_path(service_name),module_name)      
        module = imp.load_source(module_name,path + '.py')

        job_class = getattr(module,job_class_name)
        if not job_class:
            return None
        
        return job_class()