class Solution:
    def isPalindrome(self, x: int) -> bool:

        new = abs(x)
        check = 0
        while x > 0:
            last = x % 10
            check =check * 10 + last
            
            x = x // 10
              
        
        return new == check


        
        
        