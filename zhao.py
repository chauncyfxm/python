user_name = '123456'
passwd = 'abc'

my_name = input('请输入账号:')
my_passwd = input('请输入密码：')



if user_name == my_name and my_passwd == passwd:
	print ('登录成功')
elif user_name != my_name:
	print ('账号不对')
elif my_passwd != passwd:
	print ('密码不对')
