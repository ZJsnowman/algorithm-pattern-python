# -*- coding: utf-8 -*-
class Solution:
    def diffWaysToCompute(self, input: str):
        # 递归终止条件
        if input.isdigit():
            return [int(input)]
        res = []
        for i, char in enumerate(input):
            if char in ['+', '-', '*']:
                # 1.分解
                # 2. 解决
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])

                # 3.合并
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)

        return res

if __name__ == '__main__':
    sol = Solution()
    input = '2-1-1'
    print(sol.diffWaysToCompute(input))