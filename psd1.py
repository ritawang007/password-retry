password = 'a123456'
i = 3
while i > 0:
	psd = input('請輸入密碼：')
	if psd != password:
		i = i - 1
		print('密碼錯誤，還有', i ,'次機會')
	else:
		print('登入成功')
		break
