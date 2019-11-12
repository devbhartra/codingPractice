# # Recursive function to return gcd of a and b 
# def gcd(a,b): 
#     if a == 0: 
#         return b 
#     return gcd(b % a, a) 
  
# # Function to return LCM of two numbers 
# def lcm(a,b): 
#     return (a*b) / gcd(a,b) 
sum = []

a = [float(i) for i in input().split()]   #fraction 1
b = [float(i) for i in input().split()]   #fraction 2 

for i in range(0, 1):
    sum = ((a[i] * b[i + 1]) + (a[i + 1] * b[i])) / (a[i + 1] * b[i + 1])     #prints the decimal output

print(sum)

