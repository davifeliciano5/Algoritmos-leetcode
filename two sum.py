class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lista = []
        for a in range(len(nums)):
            for b in range(a+1 ,len(nums)):
                if nums[a] + nums[b] == target:
                    lista.append(a)
                    lista.append(b)
                    return lista

"""
você pode utilizar um dicionário (hashmap) para
 armazenar os valores e encontrar os pares em tempo linear O(n).
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Dicionário para armazenar valores e seus índices
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]  # Retorna os índices do complemento encontrado
            seen[num] = i  # Adiciona o valor atual ao dicionário