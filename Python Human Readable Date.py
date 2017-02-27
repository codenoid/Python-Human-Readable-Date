from datetime import datetime

# Inspired By Blurbs Framework - Human Readable Date
# Rubi Jihantoro - jihantoro8@gmail.com

now    = datetime.today()
date    =  datetime(2017, 2, 24, 23, 36, 1) #your date

# Language 
second = ' Second Ago'
minute = ' Minute Ago'
hours = ' Hours Ago'
ytd = 'Yesterday, At '
on = ' On '

dnow = [
                    now.strftime('%Y'),
                    now.strftime('%m'),
                    now.strftime('%d'),
                    now.strftime('%H'),
                    now.strftime('%M'),
                    now.strftime('%S'),
                    now.strftime('%p')
               ]
myd = [
                    date.strftime('%Y'),
                    date.strftime('%m'),
                    date.strftime('%d'),
                    date.strftime('%H'),
                    date.strftime('%M'),
                    date.strftime('%S'),
                    date.strftime('%p'),
                    date.strftime('%b')
               ]
dpo = int(myd[2])+1
def read():
     if dnow[0]+dnow[1]+dnow[2]+dnow[3]+dnow[4] == myd[0]+myd[1]+myd[2]+myd[3]+myd[4]:
          ns = int(dnow[5])
          ms = int(myd[5])
          nr = ns-ms
          x = repr(nr) + second
          print(x)
     elif dnow[0]+dnow[1]+dnow[2]+dnow[3] == myd[0]+myd[1]+myd[2]+myd[3]:
          ns = int(dnow[4])
          ms = int(myd[4])
          nr = ns-ms
          x = repr(nr) + minute
          print(x)
     elif dnow[0]+dnow[1]+dnow[2] == myd[0]+myd[1]+myd[2]:
          ns = int(dnow[3])
          ms = int(myd[3])
          nr = ns-ms
          x = repr(nr) + hours
          print(x)
     elif dnow[0]+dnow[1]+dnow[2] == myd[0]+myd[1]+str(dpo):
          x = ytd + myd[3] + ':' + myd[4] + myd[6]
          print(x)
     elif dnow[0]+dnow[1]+dnow[2] > myd[0]+myd[1]+str(dpo):
          x = myd[2] + ' ' + myd[7] + ' ' + myd[0] + on + myd[3] + ':' + myd[4] + myd[6]
          print(x)

read()
