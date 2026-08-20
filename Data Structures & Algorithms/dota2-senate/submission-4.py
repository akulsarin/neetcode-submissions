class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        rQueue = deque([i for i, c in enumerate(senate) if c == 'R'])
        dQueue = deque([i for i, c in enumerate(senate) if c == 'D'])

        while rQueue and dQueue:
            rSen = rQueue.popleft()
            dSen = dQueue.popleft()
            if rSen < dSen:
                rQueue.append(rSen + n)
            else:
                dQueue.append(dSen + n)

        return "Radiant" if rQueue else "Dire"