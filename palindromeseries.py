num = int(input("Original number : "))
temp = num
rev = 0
while(num > 0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if(temp == rev):
    print("Yes, given number is palindrome")
else:
    print("No, given number is not palindrome")