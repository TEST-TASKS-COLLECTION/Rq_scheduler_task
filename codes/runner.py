import time

def sucp(i):
    print("STARTING TASK")
    
    for t in range(i):
        print(t)
        # time.sleep(3)
    with open(f"data/log{i}", "w") as f:
        f.writelines("OK MAN") 
    print("I am running at 1:37", i)
    return "Success"