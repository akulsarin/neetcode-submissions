class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posAndSpeed = sorted(list(zip(position, speed)), reverse=True)

        numFleets = timeToTarget = 0
        for pos, vel in posAndSpeed:
            timeRemaining = (target - pos) / vel
            if timeRemaining > timeToTarget:
                numFleets += 1
                timeToTarget = timeRemaining
        
        return numFleets