class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        N = len(nums)

        adj = defaultdict(list)
        inDegrees = {n: 0 for n in nums}
        for sequence in sequences:
            for i in range(len(sequence) - 1):
                src, dst = sequence[i], sequence[i + 1]
                adj[src].append(dst)
                inDegrees[dst] += 1

        queue = deque([n for n in inDegrees if inDegrees[n] == 0])
        processed = 0
        while queue:
            if len(queue) > 1:
                return False

            curr = queue.popleft()
            if curr != nums[processed]:
                return False

            processed += 1 
            for node in adj[curr]:
                inDegrees[node] -= 1
                if inDegrees[node] == 0:
                    queue.append(node)

        return len(queue) == 0