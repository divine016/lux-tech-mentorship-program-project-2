year = int(input(' please enter any year of your  choice.'))
if((year%4==0) or (year%400==0)):
    print("the year " + str( year) + " is  a leap year.")
else:
  if(year%100 != 0):
    print('this year is not a leap year.')
    