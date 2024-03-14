# https://leetcode.com/problems/rotate-array/
# Python3

def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    if k == n or n == 1:
        return
    if k > n:
        k = k % n
    
    # Primera solución (Usando listas de Python):
    res = []
    for i in range(n-k, n, 1):
        res.append(nums[i])

    for i in range(0, n-k, 1):
        res.append(nums[i])

    for i in range(0, n, 1):
        nums[i] = res[i]

    # Otra solución (Usando Python list slice):
    '''
    nums[:] = nums[n-k:] + nums[:n-k]
    '''