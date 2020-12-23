def main():
    test_str = input('What is the input for the text to binary: ')
#   printing original string
	  print("The original string is : " + str(test_str))

	#  using join() + ord() + format()
	# Converting String to binary
	  res = ''.join(format(ord(i), 'b') for i in test_str)

	# printing result
	  print("The string after binary conversion : " + str(res))
    
main()
