# 密碼登入程式
# paeeword = '12345'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確就印出'登入成功!'
# 如果不正確就印出'密碼錯誤! 還有__次機會!'
# 輸入3次錯誤就印出'密碼錯誤! 已無法登入!'

password = '12345'
remaining = 3
while True:
	pwd = input('請輸入密碼: ')
	remaining = remaining - 1
	if pwd == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤! 還有', remaining, '次機會')
		if remaining == 0:
			break

