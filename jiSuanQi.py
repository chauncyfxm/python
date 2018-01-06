x = int(input('请输入x：'))
y = int(input('请输入y：'))
hao = input('请输入\'+、-、×、/\':')


if hao == '+':
	print (x+y)
elif hao == '-':
	print (x-y)
elif hao == '*':
	print (x*y)
elif hao == '/':
	print (x/y)
else:
	print ('输入错误')
