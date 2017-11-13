# company_code_repo
#This is the password to get into our test servers. You can run the code at https://repl.it/languages/python3
def get_flag():
	flag=[102, 108, 97, 103, 123, 99, 111, 100, 101, 95, 114, 101, 112, 111, 115, 95, 99, 97, 110, 95, 104, 97, 118, 101, 95, 103, 114, 101, 97, 116, 95, 105, 110, 102, 111, 125]
	print(''.join(chr(i) for i in flag))

get_flag()
