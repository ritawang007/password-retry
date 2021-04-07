password = 'a123456'
i = 3
while True:
	psd = input('請輸入密碼：')
	if psd != password:
		i = i - 1
		if i == 0:
			break
		print('密碼錯誤，還有', i ,'次機會')
	else:
		print('登入成功')
		break
