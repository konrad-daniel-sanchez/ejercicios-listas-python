# https://leetcode.com/problems/concatenation-of-array/
# Versión Python3

def getConcatenation(self, nums: List[int]) -> List[int]:
    # Primera solución:
    respuesta = []
    for num in nums:
        respuesta.append(num)
    for num in nums:
        respuesta.append(num)
    return respuesta

    # Otra solución posible:
    # return nums + nums
