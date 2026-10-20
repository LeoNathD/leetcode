class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        
        is_sorted = True
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                is_sorted = False
                break
        
        divisors = []
        for d in range(1, int(n**0.5) + 1):
            if n % d == 0:
                divisors.append(d)
                if d * d != n:
                    divisors.append(n // d)
        
        if is_sorted:
            return sum(divisors)
            
        def check(k: int) -> bool:
            prev_max = -1
            
            for start in range(0, n, k):
                end = start + k
                
                drop_idx = -1
                for j in range(start, end - 1):
                    if nums[j] > nums[j + 1]:
                        if drop_idx != -1:
                            return False  
                        drop_idx = j
                
                if drop_idx != -1:
                    if nums[end - 1] > nums[start]:
                        return False  
                    min_val = nums[drop_idx + 1]
                    max_val = nums[drop_idx]
                else:
                    min_val = nums[start]
                    max_val = nums[end - 1]
                
                if prev_max > min_val:
                    return False
                prev_max = max_val
                
            return True

        ans = 0
        for k in divisors:
            if k == 1:
                continue
            if check(k):
                ans += k
                
        return ans