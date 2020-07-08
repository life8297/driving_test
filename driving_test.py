country = input('請輸入來自哪個國家:')
age = input('請輸入年齡:')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
else:
	print('請尋求專員考取駕照問題')