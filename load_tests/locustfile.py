import random

from locust import HttpUser, between, task

SAMPLE_QUERIES = [
    "What is the refund policy for enterprise customers?",
    "How do I reset my password?",
    "What are the SLA guarantees for the Pro plan?",
    "How does the billing cycle work?",
    "What integrations are supported?",
    "Can I export my data at any time?",
    "What happens if I exceed my monthly quota?",
    "Is there a free trial available?",
]


class RAGUser(HttpUser):
    wait_time = between(1, 3)

    @task(8)
    def query(self):
        payload = {
            "query": random.choice(SAMPLE_QUERIES),
            "session_id": f"load-test-{random.randint(1, 100)}",
            "user_id": f"user-{random.randint(1, 20)}",
        }
        with self.client.post("/api/v1/query", json=payload, catch_response=True, name="/query") as response:
            if response.status_code == 200:
                data = response.json()
                latency = data.get("latency_ms", 0)
                if latency > 15000:
                    response.failure(f"Latency too high: {latency}ms")
                else:
                    response.success()
            else:
                response.failure(f"HTTP {response.status_code}")

    @task(2)
    def health_check(self):
        self.client.get("/health", name="/health")
