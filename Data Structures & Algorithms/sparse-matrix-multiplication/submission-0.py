class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        M, K, N = len(mat1), len(mat1[0]), len(mat2[0])
        result = [[0] * N for _ in range(M)]

        for i in range(M):
            for j in range(N):
                for k in range(K):
                    result[i][j] += (mat1[i][k] * mat2[k][j])
        
        return result
        