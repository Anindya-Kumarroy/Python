
def cal_sum(n):
    if(n==0 ):
        return 0
    else:
        return n+cal_sum(n-1)
    
n=int(input("Enter n:"))
print(cal_sum(n))