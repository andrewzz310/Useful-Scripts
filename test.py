class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        # find the number of zeros and assign two pointers one for the element of the last zero
        # and one for the element to preceding the last zero
        ans = []
        right = 0
        for i in range(len(A)):
            if A[i] < 0:
                right += 1

        left = right - 1

        while (0 <= left and right < len(A)):
            if A[left]** 2 < A[right]** 2:
                ans.append(A[left]** 2)
                left -= 1
            else:
                ans.append(A[right]** 2)
                right += 1

        while left >= 0:
            ans.append(A[left] ** 2)
            left -= 1

        while right < len(A):
            ans.append(A[right] ** 2)
            right += 1

        return ans

