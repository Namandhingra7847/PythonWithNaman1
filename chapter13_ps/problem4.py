def divisible(n):
    if n%5==0:
        return True
    return False

a = [3,4,5,65,332,735,645,3246,99]

f = list(filter(divisible, a))
print(f)