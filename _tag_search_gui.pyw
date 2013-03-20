######################################################
# Beginning of File Search GUI
######################################################
import sys,sqlite3,os
cxn = sqlite3.connect('tags.db')
cur = cxn.cursor()
from PyQt4 import QtGui
query_tags=[]
class Dialog(QtGui.QWidget):
	def __init__(self):
		super(Dialog, self).__init__()
		text, ok = QtGui.QInputDialog.getText(self, 'Tag Search','Tag(s):')
		if ok:
			global query_tags
			query_tags = text.split(";")
app = QtGui.QApplication(sys.argv)
gui = Dialog()
print(query_tags)

######################################################
# Beginning of Database Search 
######################################################
returns=[]
for i in query_tags:
	cur.execute("SELECT file_path FROM filetags WHERE tag == '"+i+"'")
	returns.append(cur.fetchall())
end_results=set(returns[0])

for i in range(1,len(returns)):
	end_results=end_results&set(returns[i])
'''
for eachFile in end_results:
	print('>> ',end='')
	print(eachFile)
'''
######################################################
# Beginning of File Display
######################################################
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from random import randint
model = QStandardItemModel()
items=[[],[]]
for i in end_results:
	items[1].append(QStandardItem(i[0]))
	items[0].append(QStandardItem(i[0].split("\\")[-1]))
	#check = Qt.Checked if randint(0, 1) == 1 else Qt.Unchecked
	check = Qt.Unchecked
	items[0][-1].setCheckState(check)
	items[0][-1].setCheckable(True)
	items[0][-1].setEditable(False)
	model.appendRow(items[0][-1])
def something():
	for i in range(len(items[0])):
		if(items[0][i].checkState()==2):
			os.startfile(items[1][i].text())
view = QListView()
view.setModel(model)
btn = QtGui.QPushButton('OPEN', view)
btn.move(5, 5+17*len(end_results))
btn.clicked.connect(something)
view.setMaximumHeight(view.sizeHintForRow(0)*len(end_results)+40)
view.show()
app.exec_()
