from queue import PriorityQueue
import sys

print = sys.stdout.write
input = sys.stdin.readline

n = int(input())
queue = PriorityQueue()

for i in range(n):
    x = int(input())
    if x == 0:
      if queue.empty():
          print("0\n")
      else:
          print(str(queue.get()[1]))
          print("\n")
    else:
        queue.put((abs(x), x))