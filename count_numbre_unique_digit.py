"""
Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

Example 1:
    Input: n = 2
    Output: 91
    Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99

Example 2:
    Input: n = 0
    Output: 1 

Constraints:
0 <= n <= 8
"""
class Solution(object):
    def countNumbersWithUniqueDigits(self, n:int)->int:
        """
        :type n: int
        :rtype: int
        """
        rango = 10**n
        cantidad = 10        
        igual = []
        if n == 0:
            return 1
        else:
            for number in range(10,rango):
                number_ = str(number)
                for index,item in enumerate(number_):
                    if number_[index+1:].find(item) != -1:
                        igual.append(number)
                        break
                if number not in igual:
                    cantidad += 1
                    
            return cantidad

#Esta solucion tiene un tiempo de ejecucion de 24ms con n=2

