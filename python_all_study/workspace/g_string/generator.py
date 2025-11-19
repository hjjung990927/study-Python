import os
import psutil

process_object = psutil.Process(os.getpid())

##################################################################################
memory_before = process_object.memory_info().rss / 1024 / 1024

data_list = [i**2 for i in range(100000)]

memory_after = process_object.memory_info().rss / 1024 / 1024

print(f'memory: {memory_before} -> {memory_after}')
##################################################################################
memory_before = process_object.memory_info().rss / 1024 / 1024

data_generator = (i**2 for i in range(100000))

memory_after = process_object.memory_info().rss / 1024 / 1024

print(f'memory: {memory_before} -> {memory_after}')
##################################################################################
