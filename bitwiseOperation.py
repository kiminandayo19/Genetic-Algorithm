# This program is for binary operation only
# Please only use non-negative integer

class BitwiseOperator():

    def __init__(self, num1 = 0, num2 = 0):
        self.num1 = num1
        self.num2 = num2

    
    # -- CONVERTER --
    def decimal_to_binary(self, num):
        # Data type : string
        number = num
        if num < 0:
            number = (-1) * num
        result = []
        if number == 0:
            result.append(str(0))
        elif number == 1:
            result.append(str(1))
        elif number == -1:
            return str(-1)
        else:
            while number != 1:
                quotient = number % 2
                result.append(str(quotient))
                number = number // 2
            result.append(str(1))
        if num < 0:
            res = "-"+"".join(result[::-1])
            return res
        else:
            return "".join(result[::-1])


    def binary_to_decimal(self, num):
        # Data type : int
        number = num
        if num < 0:
            number = (-1) * num
        number = str(number)
        result = 0
        list_of_number = [i for i in number][::-1]
        for i in range(len(list_of_number)):
            temp_result = int(list_of_number[i]) * (2**i)
            result += temp_result
        if num < 0:
            result = 0 - result
        return result
    # -- END OF CONVERTER --


    # -- LOGIC --
    def and_logic(self, bit1, bit2):
        # Data type : int
        if bit1 == 0 and bit2 == 0:
            return 0
        elif bit1 == 0 and bit2 == 1:
            return 0
        elif bit1 == 1 and bit2 == 0:
            return 0
        elif bit1 == 1 and bit2 == 1:
            return 1


    def or_logic(self, bit1, bit2):
        # Data type : int
        if bit1 == 0 and bit2 == 0:
            return 0
        elif bit1 == 0 and bit2 == 1:
            return 1
        elif bit1 == 1 and bit2 == 0:
            return 1
        elif bit1 == 1 and bit2 == 1:
            return 1


    def xor_logic(self, bit1, bit2):
        if bit1 == 0 and bit2 == 0:
            return 0
        elif bit1 == 0 and bit2 == 1:
            return 1
        elif bit1 == 1 and bit2 == 0:
            return 1
        elif bit1 == 1 and bit2 == 1:
            return 0
    # -- END OF LOGIC --


    # -- OPERATOR --
    def and_operator(self, num1, num2):
        # Data type : int
        result = []
        bit1 = self.decimal_to_binary(num1)
        bit2 = self.decimal_to_binary(num2)
        bit1 = [i for i in bit1]
        bit2 = [j for j in bit2]
        diff = abs(len(bit1) - len(bit2))
        if len(bit1) != len(bit2):
            if len(bit1) < len(bit2):
                bit1 = [0 for i in range(diff)] + bit1.copy()
            elif len(bit2) < len(bit1):
                bit2 = [0 for i in range(diff)] + bit2.copy()
        for i in range(len(bit1)):
            temp = str(self.and_logic(int(bit1[i]), int(bit2[i])))
            result.append(temp)
        res = int("".join(result))
        res = self.binary_to_decimal(res)
        return res


    def or_operator(self, num1, num2):
        # Data type: int
        result = []
        bit1 = self.decimal_to_binary(num1)
        bit2 = self.decimal_to_binary(num2)
        bit1 = [i for i in bit1]
        bit2 = [j for j in bit2]
        diff = abs(len(bit1) - len(bit2))
        if len(bit1) != len(bit2):
            if len(bit1) < len(bit2):
                bit1 = [0 for i in range(diff)] + bit1.copy()
            elif len(bit2) < len(bit1):
                bit2 = [0 for i in range(diff)] + bit2.copy()
        for i in range(len(bit1)):
            temp = str(self.or_logic(int(bit1[i]), int(bit2[i])))
            result.append(temp)
        res = int("".join(result))
        res = self.binary_to_decimal(res)
        return res


    def xor_operator(self, num1, num2):
        # Data type: int
        result = []
        bit1 = self.decimal_to_binary(num1)
        bit2 = self.decimal_to_binary(num2)
        bit1 = [i for i in bit1]
        bit2 = [j for j in bit2]
        diff = abs(len(bit1) - len(bit2))
        if len(bit1) != len(bit2):
            if len(bit1) < len(bit2):
                bit1 = [0 for i in range(diff)] + bit1.copy()
            elif len(bit2) < len(bit1):
                bit2 = [0 for i in range(diff)] + bit2.copy()
        for i in range(len(bit1)):
            temp = str(self.xor_logic(int(bit1[i]), int(bit2[i])))
            result.append(temp)
        res = int("".join(result))
        res = self.binary_to_decimal(res)
        return res
    # -- END OF OPERATOR --


# -- TESTING --
# bit = BitwiseOperator()
# rest = bit.or_operator(20, 4)
# print(rest)
# -- END OF TESTING --