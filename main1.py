def checkpalindrome(str):
	if str[::-1]==str:
		return True
	else:
		return Flase
n=input

if checkpalindrome(n):
	print("palindrome")
else:
	print("not palindrome")