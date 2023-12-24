class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix or not matrix[0]:
            return False

        pred=deque(matrix[0])

        for i in range(1,len(matrix)):
            row= matrix[i]
            pred.pop()
            pred.appendleft(row[0])

            for j in range(1,len(row)):
                if(row[j]!=pred[j]):
                    return False
        return True


        