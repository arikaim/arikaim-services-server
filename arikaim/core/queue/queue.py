
import os
from datetime import datetime, timedelta, timezone
from redis import Redis
from rq import Queue as RqQueue
from rq import Worker

from arikaim.core.utils import load_source
from arikaim.core.logger import logger
from arikaim.core.queue.job import Job
from arikaim.core.path import Path

class Queue:

    def __init__(self):
        self._redis = Redis()
        self._queue = RqQueue(connection = self._redis)
        self._worker = None
       
    def boot(self):
        logger.info('Init qeueue')
     
    def run(self):
        logger.info('Run qeueue worker')
        self._worker = Worker(
            [self._queue], 
            connection = self._redis, 
            name = 'jobs'
        )
        self._worker.work()

    def add_job(self, job, *args, **kwargs):
        if isinstance(job,Job) == False: 
            raise Exception('Not valid job instance')
        
        if job.interval:
            return self._queue.enqueue_in(
                job.execute, 

                *args, 
                **kwargs
            )
        return self._queue.enqueue(job.execute, *args, **kwargs)
    
    def get_jobs_count(self):
        return len(self._queue)

    def remove_jobs(self):
        self._queue.empty()

    @property
    def jobs(self):
        return self._queue.jobs

    def create_job(self, job_class_name: str, module_name: str, service_name: str):
        path = os.path.join(Path.job(service_name),module_name)      
        module = load_source(module_name,path + '.py')

        job_class = getattr(module,job_class_name)
        if not job_class:
            return None
        
        return job_class()
    

queue = Queue()
