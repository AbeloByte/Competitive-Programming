class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        win = 0
        for i in range(2,n+1):
            win = (win + k) % i
            print(win)
        return win + 1
            
            