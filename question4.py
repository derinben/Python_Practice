    def canJump(self, nums: List[int]) -> bool:
                    	    
            ptr = 0       
            count_array = len(nums) - 1 

            for i in range(len(nums)):
                max_jump =  nums[i] + i

                if i > ptr:
                    return False
                
                if ptr < max_jump:
                    ptr = max_jump
                    
                if max_jump >= count_array:
                    return True

        
