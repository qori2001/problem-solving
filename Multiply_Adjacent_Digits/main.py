

# Description:
# Multiply the adjacent digits which are not separated by a '-' or a '+' in a string, then do the sum.

# Examples
# "53+5"    -->   20  # = 5 * 3 + 5
# "266-66"  -->   36  # = 2 * 6 * 6 - 6 * 6
# "555"     -->  125  # = 5 * 5 * 5


def multiplication(s:str)->int:
    res  =1
    for c in s:
        res *= int(c)
    return res


def return_tab(exep):
    num = ""
    tab_num = []
    i = 0
    while i < len(exep):
        if exep[i] in "+-":
            tab_num.append(multiplication(num))
            tab_num.append(exep[i])
            print(num)
            num = ""
        else :
            num += exep[i]
        i+=1
    
    tab_num.append(multiplication(num))
    return tab_num

# print(return_tab("3434343-12121212+4949494-122"))







def digit_multiplication(expression):

    tab_num = return_tab(expression)

    res = 0
    i = 0
    while i < len(tab_num):
        pass



    return res




print(digit_multiplication('12345-11989+1231111'))


