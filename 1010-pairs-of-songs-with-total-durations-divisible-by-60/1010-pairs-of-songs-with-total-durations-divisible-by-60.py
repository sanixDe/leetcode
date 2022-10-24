class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        
        dict = {}
        # array = []
        for i in time:
            cur = (60-(i%60))%60
            count += dict.get(cur, 0)
            dict[i%60] = 1+dict.get(i%60, 0)
            
        print(dict)
        return count
    
    '''
    Time Complexity = O(N)
    Space Complexity = O(60) = O(1)
    '''