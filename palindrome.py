def is_palindrome(num):
  temp=num
  reverse=0
  while(temp>0):
    digit=temp%10
    reverse=reverse*10+digit
    temp=temp//10
  if(num==reverse):
    print('palindrome')
  else:
    print('no palindrome')

is_palindrome(11)