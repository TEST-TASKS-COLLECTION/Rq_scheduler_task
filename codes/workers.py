import requests
import time

def task1(i=3):
    print("STARTING TASK")
    
    for t in range(i):
        print(t)
        time.sleep(3)
    with open(f"data/log{i}.txt", "w") as f:
        f.writelines("OK MAN") 
    print("I am running at 1:37", i)
    return "Success"


def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())