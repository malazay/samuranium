import functools
import time

def get_current_time():
  return time.perf_counter()

def timer(func):
  """Print the runtime of the decorated function"""
  @functools.wraps(func)
  def wrapper_timer(*args, **kwargs):
    start_time = get_current_time()
    value = func(*args, *kwargs)
    end_time = get_current_time()
    run_time = end_time - start_time
    print(f"Finished {func.__name__!r} in {run_time:.4f} seconds")
    return value
  return wrapper_timer

@timer
def say(word):
  time.sleep(1)
  print(f"{word}")

