var=str(input("Enter the string: "))
bad = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
new_str = ""
for i in var:
	if i not in bad:
		new_str= new_str+ i
print(new_str)