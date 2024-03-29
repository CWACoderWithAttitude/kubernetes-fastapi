from locust import HttpUser, task


class LoadTesting(HttpUser):
    @task
    def hello_world(self):
        self.client.post("/api/v1/hello", json={})
    @task
    def hello_ping(self):
        self.client.get("/ping")
