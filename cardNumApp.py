import re
numList=list()
operation=None

def judge(num):
	if re.fullmatch('[0-9]{4}-?[0-9]{4}',num):
		return True
	else:
		return False

def saveNum():
	num=input('カード番号を入力(xxxx-xxxx)>')
	if judge(num):
		if '-' not in num:
			num=num[0:4]+'-'+num[4:]
		numList.append(num)
	else:
		print('番号が不正です。')

def output():
	if len(numList)>0:
		for x in numList:
			print(x)
	else:
		print('まだ登録されていません')

def search():
	count=0
	if len(numList)==0:
		print('まだ登録されていません')
	else:
		searchNum=input('検索する最初の数字を何桁か入れてください>')
		if re.fullmatch('[0-9]{1,4}-?[0-9]{0,4}',searchNum):
			if len(searchNum)>=5 and '-' not in searchNum:
				searchNum=searchNum[0:4]+'-'+searchNum[4:]
			for data in numList:
				if data.startswith(searchNum):
					count=count+1
					print(data)
			print(str(count)+'件')
		else:
			print('入力された内容が不適切です。')

while operation!='4':
	operation=input('操作を入力:1.入力,2.一覧,3.検索,4.終了>')
	if operation=='1':
		saveNum()
	elif operation=='2':
		output()
	elif operation=='3':
		search()
	elif operation=='4':
		print('終了')
	else:
		print('入力された内容が不正です。')
