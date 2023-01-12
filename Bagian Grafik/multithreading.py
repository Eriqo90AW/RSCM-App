import threading
import time

def worker(n):
    print(f'Worker in thread: {threading.get_ident()}\nReceived argument: {n}')
    time.sleep(n)

start = time.perf_counter()

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i+1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.perf_counter()

print(f'Finished in {round(end - start, 2)} second(s)')