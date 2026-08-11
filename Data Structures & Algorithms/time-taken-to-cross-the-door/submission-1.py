class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        N = len(arrival)
        ENTER, EXIT = 0, 1
        waiting = {ENTER: deque([]), EXIT: deque([])}
        
        answer = [-1] * N
        lastTime, lastState = -2, -1
        t, j, processed = 0, 0, 0
        while processed < N:
            if not waiting:
                t = arrival[j]

            while j < N and t >= arrival[j]:
                waiting[state[j]].append(j)
                j += 1

            allowState = lastState
            if t > lastTime + 1 or min(len(waiting[ENTER]), len(waiting[EXIT])) == 0:
                allowState = EXIT if waiting[EXIT] else ENTER

            if waiting[allowState]:
                person = waiting[allowState].popleft()
                answer[person] = t
                lastTime = t
                lastState = allowState
                processed += 1

            t += 1

        return answer