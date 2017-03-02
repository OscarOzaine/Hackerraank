## Day 18: Queues and Stacks
## https://www.hackerrank.com/challenges/30-queues-stacks

class Solution:
    stack = []
    queue = []
    
    def __init__(self):
        self.stack = []
        self.queue = []
        
    def pushCharacter(self, char):
        self.stack.append(char)
    
    def enqueueCharacter(self, char):
        self.queue.insert(0, char)
    
    def popCharacter(self):
        popped = self.stack.pop(len(self.stack) - 1)
        return popped
    
    def dequeueCharacter(self):
        dequeued = self.queue.pop()
        return dequeued
    
