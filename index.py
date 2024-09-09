# Import requerd module 
from instabot import *
import os
#import opendrive as od
#Log in Instagram 
class pyBot1:

    # Install Bot 
     bot = Bot()


     def login_user():
       username = input('Enter your Instagran Username/Mobile number/Email id:-')
       password = input('Enter your Instagram Password:-')
         
       Bot.login(username=username,password=password)
    #Make a funtion call follow user
     def follow_user():
        pyBot1.Bot.follow_user('feelltubes')
        useridI = input('Enter the instagram username of user that you want to follow:-')
        pyBot1.Bot.follow_user(useridI)
     # Make a funtion call unfollow user
     def  unfollow_user():
         user_2 = input('Enter the Instagram Username that you want to unfollow:-')
         Bot.unfollow_user(user_2)

      # Make a function call block user
     def block_user():
         Bot.block_users()
      # Make a funtion call unfollow user who is not followback
'''
Upcomeing version have a features 
1. Unfollow user who is not follow you.
2. Uplode Story,Reels,Photo and Video.
3. Followback user who are follow you.
4. Auto confirm panding requst and some security update.
'''
      

print("1.Follow User\n2.Unfollow User\n3.Block User")
commant_1 = input(int('Enter the command number\nEX:-1 and Enter buttom:-'))
PYBOT = pyBot1()
if commant_1 == '1':
    print(f'You  number {commant_1}')
    PYBOT.login_user()
    PYBOT.follow_user()
if commant_1 == '2' :
    print(f'You choose is number {commant_1}')
    PYBOT.login_user()
    PYBOT.unfollow_user()
if commant_1 == '3':
    print(f'You choose is number {commant_1}')
    PYBOT.login_user()
    PYBOT.block_user()
    
else:
    print(
        ''''
     Try again!
     Choose valid commant like (1)
     If have any error report on mail {'soupornochakraborty40@gmail.com'}
        '''
    )
