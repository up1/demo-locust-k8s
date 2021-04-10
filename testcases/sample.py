from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def index(self):
        self.client.get("/")

    @task
    def list_all_users(self):
        self.client.get("/users")
