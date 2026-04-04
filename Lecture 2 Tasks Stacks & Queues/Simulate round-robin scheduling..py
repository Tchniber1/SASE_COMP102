from collections import deque
queue = deque()
n,q = map(int, input().split())
# Read each task name and its required CPU time.
for _ in range(n):
    task,t = input().split()  # task = process name, t = remaining time
    queue.append((task,int(t)))
# Stores tasks in the order they fully finish.
Done = []
# Keep running until no tasks are left in the queue.
while queue:
    task, t = queue.popleft()  # Take the task at the front (its turn now)
    if t <= q : # Task can finish within this time slice    
        Done.append(task)  # Finishes within this time slice
    else:
        queue.append((task, t-q))  # Not finished, put it back with less time
print(" ".join(Done))