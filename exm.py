a=int(input("Enter the number: "))
temp = a
rev = 0
while temp > 0:
    r = temp % 10
    rev = (rev * 10) + r
    temp = temp // 10
if a == rev:
  print('Palindrome')
else:
  print("Not Palindrome")
