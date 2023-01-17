li = [10, 20, 33, 46, 55]

def divisibility(li):
    print("Given list : ",li)
    print("Divisible by 5")
    for num in li:
        if num % 5 == 0:
            print(num)

divisibility(li)