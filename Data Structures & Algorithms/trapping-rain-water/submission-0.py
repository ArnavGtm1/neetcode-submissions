class Solution:
    def trap(self, height: List[int]) -> int:
        #what i know: 
        #Starting point of the trapped water: Greatest height so far (greater than 0 tho)
        #Ending point of trapped water: Height greater than or equal to the greatest height.
        #Run loop left to right, with 2 pointers. When detected starting height, ending pointer moves forward to look for the ending point.
        prefix =  [0]*len(height)
        greatest = 0
        for i in range(len(height)):
            prefix[i] = greatest
            if height[i] > greatest:
                greatest = height[i]

        suffix = [0]*len(height)
        greatest = 0
        for i in range(len(height)-1, -1, -1):
            suffix[i] = greatest
            if(height[i] > greatest):
                greatest = height[i]

        total = 0
        for i in range(len(height)):
            if height[i] < prefix[i] and height[i] < suffix[i]:
                minheight = (prefix[i] if prefix[i] < suffix[i] else suffix[i])
                total += minheight - height[i]

        return total






                


        