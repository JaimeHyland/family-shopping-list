from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def index(self):
        self.client.get("/")

    @task
    def login(self):
        self.client.post("/accounts/login/", {"username":"user", "password":"password"})

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(5, 15)