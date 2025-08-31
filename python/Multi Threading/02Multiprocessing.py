import multiprocessing
import time

def square_num():
    for i in range(5):
        time.sleep(2)
        print(f"Square : {i * i}")

def cube_num():
    for i in range(5):
        time.sleep(2)
        print(f"Cube : {i * i * i}")
        
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square_num)
    p2 = multiprocessing.Process(target=cube_num)
    
    t = time.time()
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
        
    print("Start time:", t)
    finished_time = time.time() - t
    print("Finished time:", finished_time)
    

