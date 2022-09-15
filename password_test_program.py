# Password test program
# Password is a123456
# User can only try to input password 3 times at maximum
# If input password is correct, show Log in successfully
# If input password is wrong, show wrong password and chance left to try

correct_password = 'a123456'
i = 0 # try time
while i < 3:
	print('You have', 3-i, 'try(s)')
	password = input('Please insert password: ')
	if password == correct_password:
		print('Log in succesfully')
		break
	else:
		i = i + 1
		print('Password is wrong and you still have', 3-i, 'try(s)')
		if i == 3:
			print('Fail to log in, please contact password agency') 