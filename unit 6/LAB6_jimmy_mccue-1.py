"""
    Username/Password validator
      Jimmy McCue
      The program asks a user for a username and a valid password or allows to log in as a guest
      and then assigns the user a security access level
      06-10-2025
"""

username_pass = {'user1': 'pass1', 
                 'user2': 'pass2', 
                 'user3': 'pass3', 
                 'user4': 'pass4',
                 'guest': 'guest'}
logging_in = True
username = ''
password = ''
security_level = 0

while logging_in:
  print('If you would like to log in as a guest: username= guest and password= guest')
  username = input('Please enter your username: ')
  if username in username_pass:
    password = input('Please enter your password: ')
    if password == username_pass[username]:
      if username == 'guest':
          security_level = 0
      else:
          security_level = 1
      logging_in = False
      print(f'{username} is logged in with a security level of {security_level}')
      input('Press enter to log out: ')
    else:
      print('Wrong Password, Good Bye')
      break
  else:
    print('User does not exist')
    break