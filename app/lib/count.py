import time
import queue

def count_num(queue: queue.Queue, max_num: int=5, sleep_time: int=1):
    for i in range(max_num):
        print(f"count: {i}")
        time.sleep(sleep_time)
        progress = i/max_num
        queue.put(progress)

def main():
    q = queue.Queue()
    count_num(queue=q)
    
    while True:
        if q.empty():
            break
        out = q.get()
        print(out)
        print(q.empty())

if __name__ == "__main__":
    main()

        