numbers_x = [10, 20, 30, 40, 10] 
numbers_y = [75, 65, 35, 75, 30]

def check_list(li):
    if li[0] == li[-1]:
        print ("result is True")
    else:
       print ("result is False")

print("Given list : ",numbers_x)
check_list(numbers_x)
print(" numbers_y = ",numbers_y)
check_list(numbers_y)