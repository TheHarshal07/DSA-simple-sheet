# Here first we need convert Decimal to Binary after toggling them again convert Binary to Decimal

def decimal_to_binary(nums):
    binary = format(nums, 'b')
    return binary

def Toggling(nums):
    toggles = []
    for i in nums:
        if i == "1":
            toggles.append("0")
        else:
            toggles.append("1")
    return "".join(toggles)

def binary_to_decimal(num):
    decimal = int(num, 2)
    return decimal

number = 10
Binary_pres = decimal_to_binary(number)
print(Binary_pres)

toggle_number = Toggling(Binary_pres)
print(toggle_number)

Final_number = binary_to_decimal(toggle_number)
print(Final_number)