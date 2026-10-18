#palindrome or not!
numbers=[1,2,3,2,1]
num=numbers.copy()
num.reverse()
if(numbers==num):
    print("Palindrome")
else:
    print("Not Palindrome")