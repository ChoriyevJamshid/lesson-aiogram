# import time
#
#
# def decorator(function):
#
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         result = function(*args, **kwargs)
#         end_time = time.perf_counter()
#         print(f'Work time: {round(end_time - start_time, 3)}')
#         return result
#
#     return wrapper


# @decorator
# def simple_func():
#     i = 0
#     while i < 100000:
#         i += 1
#
#
# simple_func()

lst = [1, 2]
a, b = lst
print(a)
print(b)


