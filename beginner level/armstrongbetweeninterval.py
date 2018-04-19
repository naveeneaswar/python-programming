def main():
    pass
a,b=raw_input().split()
a=int(a)
b=int(b)
for num in range(a,b+1):
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
