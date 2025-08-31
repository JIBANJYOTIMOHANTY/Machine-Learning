import threading
import time
def print_numbers():
    for i in range(5):
        print(f"Number : {i}")
        time.sleep(2)
        
def print_letters():
    for letter in "abcde":
        print(f"Letter : {letter}")
        time.sleep(2)
        
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters) 
        
t = time.time()
t1.start()
t2.start()

t1.join()
t2.join()

print("Start time:", t)
# print_numbers()
print()
# print_letters()
finished_time = time.time() - t;
print("Finished time:", finished_time)