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
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        rango = 10**n
        cantidad = 10#Contamos 10 porque los numeros (0..9) de un solo digitos no se repiten        
        igual = []
        if n == 0:
            return 1        
        else:
            for number in range(10,rango):                
                number_ = str(number)
                if len(number_) == 2 and number_[0] != number_[1]:
                    cantidad += 1
                else:
                    for index,item in enumerate(number_):
                        if number_[index+1:].find(item) != -1:
                            igual.append(number)
                            break#No necesitamos saber si hay mas de 1 repeticion rompemos el ciclo para pasar al proximo numero
                    if number not in igual:
                        cantidad += 1
                    
            return cantidad

#Esta solucion tiene un tiempo de ejecucion de 19ms con n=2