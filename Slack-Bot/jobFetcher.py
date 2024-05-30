import requests

class JobFetcher:
    def __init__(self, api_key, host) -> None:
        self.api_key = api_key
        self.host = host
        self.base_url = "https://linkedin-jobs-scraper-api.p.rapidapi.com/jobs"
        self.job_ids = []
    
    def get_jobs(self, title = 'Software Engineer', location = 'Toronto', companyName = [], publishedAt = 'PastMonth') -> list:
        payload = {
        "title": title,
        "location": location,
        "companyName": companyName,
        "rows": 100,
        "contractType": "FullTime",
        "experienceLevel": "Internship",
        "publishedAt": publishedAt
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.host
        }

        response = requests.post(self.base_url, json=payload, headers=headers)
        response.raise_for_status()
        postings = JobFetcher.format_postings(response.json())
        
        return postings
    
    def get_job_ids(self)->list:
        return self.job_ids
    
    def set_job_ids(self, id: str)->None:
        self.job_ids.append(id)
    
    #Format the job postings by dropping  unnecessary columns(Variable "trash_keys") and store IDs of every job posting
    @staticmethod
    def format_postings(posting:list) -> list:
        trash_keys = {"applicationsCount","workType", "contractType", "companyUrl", 'posterProfileUrl', 'posterFullName', 'companyId'}
        for i in range(len(posting)):
            JobFetcher.set_job_ids(posting[i]['id'])
            posting[i] = {key: val for key,val in posting[i].items() if key not in trash_keys}
            return posting