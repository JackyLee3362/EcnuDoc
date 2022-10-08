import random
import time
for i in range(100):
  a = random.randint(1,10)
  time.sleep(a/10)
  print(f"invaiding...process{i}%")