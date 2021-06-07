import memory_profiler
import time
# importing libraries
import signal
import resource
import os
# checking time limit exceed
def time_exceeded(signo, frame):
    print("CPU is up for more than specified Time")
    raise SystemExit(1)
    
def set_max_runtime(seconds):
    # setting up the resource limit
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)
    
def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)
def check_even(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num*num)
    return even
    
if __name__ == '__main__':
    set_max_runtime(15)
    limit_memory(5368709120)
    m1 = memory_profiler.memory_usage()
    t1 = time.clock()
    cubes = check_even(range(99999978))
    t2 = time.clock()
    m2 = memory_profiler.memory_usage()
    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]
    print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this method")
