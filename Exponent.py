#print(2**3)
#by function
def raise_to_power(base_num,pow_num):
    result=1
    for wow in range(pow_num):
        result = result*base_num
    return result
print(raise_to_power(4,3))