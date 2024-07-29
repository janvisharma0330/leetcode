class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        arr = [0] + arr + [float("inf")]
        A, B = [], []
        p, q = 1, len(arr)-2

        M = 0 
        while p <= q:
            if arr[p-1] <= arr[p]:
                A.append(arr[p])
                p += 1
            elif arr[q] <= arr[q+1]:
                B.append(arr[q])
                while A and A[-1] > B[-1]:
                    A.pop()
                q -= 1
            else:
                break

            M = max(M, len(A)+len(B))

        return n - M 
        