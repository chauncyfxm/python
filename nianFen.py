year = int(input('请输入你的年份：'))



if year%4 == 0 and year%100 != 0:
	print ('%d年，是闰年'%year)
elif year%400 == 0:
	print ('%d年，是闰年'%year)
else:
	print ('%d年，是平年'%year)

