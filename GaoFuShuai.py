high = int(input('请输入身高：'))
fase = int(input ('请输入颜值分：'))
money = int(input ('你的身价是：'))




if high > 180 and fase >90 and money > 1000000:
	print ('你是高富帅')
elif high < 180 and fase >90 and money > 1000000:
	print ('你是富帅')
elif high < 180 and fase <90 and money > 1000000:
	print ('你是有钱人')
elif high < 180 and fase <90 and money < 1000000:
	print ('你是矮穷搓')
elif high > 180 and fase >90 and money < 1000000:
	print ('你是高帅')
else:
	print ('你输入错误！')


