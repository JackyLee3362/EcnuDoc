class Solution:
    def rotatedDigits(self, n: int) -> int:
      map_enable = [1, 1, 1, 0, 0, 1, 1, 0, 1, 1] # 能够旋转
      map_diff   = [0, 0, 1, 0, 0, 1, 1, 0, 0, 1] # 旋转后值变化
      def isGood(num: int) -> bool:
        list = []
        flag = 0
        while num:
          list.append(num % 10)
          num //= 10
        for i in list:
          if map_enable[i] == 0: return False
          if map_diff[i] == 1: flag = 1
        return flag
      cnt = 0
      for i in range(2, n+1):
        cnt += isGood(i)
      return cnt
solution = Solution()
print(solution.rotatedDigits(10000000))

