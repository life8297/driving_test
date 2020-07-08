country = input('請輸入來自哪個國家(台灣/美國):')
age = input('請輸入年齡:')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif country == "美國":
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
else:
	print('請洽尋專員駕照問題')