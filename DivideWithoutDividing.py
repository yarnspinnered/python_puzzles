import sys

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        s = Solution()
        negative_flag = False
        if divisor == 0:
            return 2147483647
        if dividend < 0 and divisor > 0:
            negative_flag = True
            dividend = -dividend
        elif dividend > 0 and divisor < 0:
            negative_flag = True
            divisor = -divisor
        elif dividend < 0 and divisor <0:
            dividend = -dividend
            divisor = -divisor

        if dividend < divisor:
            return 0

        current_product = divisor
        current_multiplier = 1
        current_product_shifted = 0

        while current_product < dividend:
            current_product = current_product << 1
            current_multiplier = current_multiplier << 1
            current_product_shifted += 1

        if current_product == dividend:
            if negative_flag:
                res = -current_multiplier
            else:
                res = current_multiplier
        else:
            if current_product_shifted > 1:
                left_over = dividend - (current_product >> 1)
                current_multiplier = current_multiplier >> 1
            else:
                if dividend - divisor > 0:
                    left_over = dividend - divisor
                    current_multiplier = 1

            if negative_flag:
                res = -(current_multiplier+ s.divide(left_over,divisor))
            else:
                res =  current_multiplier+ s.divide(left_over,divisor)

        if res > 2147483647:
            return 2147483647
        elif res < -2147483648:
            return -2147483648
        else:
            return res

s = Solution()
print(s.divide(2147483699,-1))