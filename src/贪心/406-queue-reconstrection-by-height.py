# -*- coding: utf-8 -*-
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
       一般这种数对，还涉及排序的，根据第一个元素正向排序，根据第二个元素反向排序，或者根据第一个元素反向排序，根据第二个元素正向排序，往往能够简化解题过程。

       假设有一个队列，已知每个人的身高h和排在该人前面的更高或一样高的人数k，现在给你打乱顺序后的数组，要求恢复原来的队列。
        考虑将这群人依次加入新队列中，加入时需符合k的要求。注意到，一个人的k值实际上与身高更矮的人的位置无关，所以如果身高比他更高的人已经排好队了，
        这个人加入当前队列的位置就可以根据k值确定了。因此，身高较高的人应该先加入，我们先对队列按身高降序排序。此外，对于相同身高的人，k值较小的人位置在前，优先加入。

        :param people:
        :return:
        """
        people.sort(key = lambda x :(-x[0],x[1]))  # 身高升序，第二个元素降序
        result = []
        for p in people:
            if p[1]>=len(result):
                result.append(p)
            else:
                result.insert(p[1],p)
        return result