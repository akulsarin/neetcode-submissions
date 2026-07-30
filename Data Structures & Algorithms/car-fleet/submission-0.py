class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posAndSpeed = sorted(zip(position, speed), key = lambda item: -item[0])
        stack = []        
        for i in range(len(posAndSpeed)):
            pos, speed = posAndSpeed[i]
            timeToTarget = (target - pos)/speed
            if len(stack) == 0 or timeToTarget > stack[-1]:
                stack.append(timeToTarget)

        return len(stack)



        