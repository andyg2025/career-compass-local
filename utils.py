from models import Job

def get_jobs() -> List[Job]:
    jobs = []
    job = Job()
    job.location = "Ireland"
    job.name = "backend"
    job.postdate = "1d"
    job.type = "intern"
    job.url = "www.google.com"
    
    jobs.append(job)

    return jobs