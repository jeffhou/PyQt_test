import sqlite3,os

cxn = sqlite3.connect('tags.db')
cur = cxn.cursor()
try:
	cur.execute('CREATE TABLE filetags(file_path VARCHAR(255), tag VARCHAR(20))')
except:
	pass
control=0
#try:
while control!=-1:
	print("1) TAG A FILE")
	print("2) LIST TAGS")
	print("3) LIST FILES")
	print("4) FIND FILES BY SINGLE TAG")
	print("5) FIND FILES BY TAGS")
	print("6) CLEAR DATABASE")
	print("-1) QUIT")
	control=int(input("$ "))
	if control==1:
		file_dir=input("FILE$ ")
		tag=input("TAG$ ")
		cur.execute('INSERT INTO filetags VALUES("'+file_dir+'","'+tag+'")')
	if control==2:
		cur.execute('SELECT DISTINCT tag FROM filetags')
		print('==TAGS')
		for eachTag in cur.fetchall():
			print('>> '+eachTag[0])
	if control==3:
		cur.execute('SELECT DISTINCT file_path FROM filetags')
		print('==FILES')
		for eachFile in cur.fetchall():    
			print('>> '+eachFile[0])
	if control==4:
		print("SEARCH TAG")
		find_tag=input("$ ")
		cur.execute("SELECT * FROM filetags WHERE tag == '"+find_tag+"'")
		print('==TAGS')
		a=cur.fetchall()
		#help(a)
		for eachFile in cur.fetchall():
			print('>> ',end='')
			print(eachFile)
	if control==5:
		print("SEARCH TAGS")
		tags=input("$ ").split(";")
		print(tags)
		returns=[]
		for i in tags:
			cur.execute("SELECT file_path FROM filetags WHERE tag == '"+i+"'")
			returns.append(cur.fetchall())
		print(returns)
		end_results=set(returns[0])
		
		for i in range(1,len(returns)):
			end_results=end_results&set(returns[i])
		for eachFile in end_results:
			print('>> ',end='')
			print(eachFile)
	if control==6:
		cur.execute("DELETE FROM filetags")
cur.close()
cxn.commit()
cxn.close()
'''
cur.execute('INSERT INTO users VALUES("john", 100)')
cur.execute('INSERT INTO users VALUES("jane", 110)')
cur.execute('SELECT * FROM users')
for eachUser in cur.fetchall():
	 print eachUser
cur.execute('DROP TABLE users')
cur.close()
cxn.commit()
cxn.close()
'''
