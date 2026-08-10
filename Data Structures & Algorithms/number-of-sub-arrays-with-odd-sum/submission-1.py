class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:        
        even_count = 1
        odd_count = 0
        
        prefix = 0
        res = 0
        
        for num in arr:
            prefix += num
            
            if prefix % 2 == 0:
                res += odd_count
                even_count += 1
            else:
                res += even_count
                odd_count += 1
                
        return res

        