from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue=deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        
        # 2. Define the minimum valid timestamp for the 3000ms window
        min_valid_time = t - 3000
        
        # 3. Evict all old timestamps from the front of the queue
        while self.queue and self.queue[0] < min_valid_time:
            self.queue.popleft() # Fast O(1) removal from the left
            
        # 4. The size of the queue is the number of recent calls
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)