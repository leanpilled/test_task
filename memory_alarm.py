import psutil
import requests

MEMORY_THRESHOLD_PERCENT = 90

while True:
    memory_percent = psutil.virtual_memory().percent

    if memory_percent >= MEMORY_THRESHOLD_PERCENT:
        data = {"message": f"High memory usage: {memory_percent}%"}

        response = requests.post("https://example.com/api/alarm", json=data)
        if response.status_code != 200:
            print(f"Ошибка {response.status_code}")