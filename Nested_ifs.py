#boolean tells us the truth(true or false)
print('Welcome to SSE Bank')
card_inserted = True
pin = int(input('set your pin ' ))
balance = int(input('set your balance '))
withdraw = True
print('='*43)
print('Welcome to SSE ATM')
print("please insert your card")
if card_inserted:
  print('Card detected')
  print('='*43)
  for i in range (3):
    user_try = int(input("enter you pin "))
    if pin == user_try:
      print('access granted')
      print('your balance is', balance)
      print('='*43)
      if withdraw:
        withdraw_amt = int(input('how much do withdraw? '))
        print('Withdrawn Amount =', withdraw_amt)
        if withdraw_amt <= balance:
          balance = balance - withdraw_amt
          print('current balance is', balance)
          print('='*43)
          break
        else:
          print('you dont have enough balance')
      else:
        print('the person does not wants to withdraw')
    else:
      print('wrong password')
      print('attempts left', 3 - (i+1))
      print('='*43)
  else:
    print('Card blocked due to 3 wrong attempts')
else:
  print('Insert the card')
