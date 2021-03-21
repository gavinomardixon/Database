import sqlite3

class Database:
	def __init__(self, db) -> gav.py:
		self.conn= sqlite3.connect(db)
		self.cur= self.conn.cursor()
		self.cur.execute("""CREATE TABLE db (id INTEGER PRIMARY KEY,
	   [NAME] text, [PARISH] text, 
	   [TELEPHONE] integer, [EMAIL] text, 
	   [TEST] text, [LAB] text, [USER] text, [ID] integer, [DATE] date, [TIME] time)""")
		self.conn.commit()

	def fetch(self):
		self.cur.execute("SELECT * FROM db")
		rows= self.cur.fetchall()
		return rows
	def insert(self, NAME, PARISH, TELEPHONE, EMAIL, TEST, LAB, USER, ID, DATE, TIME):
		self.cur.execute ("INSERT INTO db VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"(id, NAME, PARISH, TELEPHONE, EMAIL, TEST, LAB, USER, ID, DATE, TIME))
		self.conn.commit()
	def remove (self, id):
		self.cur.execute("DELETE FROM db WHERE id=?",(id,))
		self.conn.commit()
	def update (self, id, NAME, PARISH, TELEPHONE, EMAIL, TEST, LAB, USER, ID, DATE, TIME):
		self.cur.execute("UPDATE db SET NAME=?, PARISH=?, TELEPHONE=?, EMAIL=?, TEST=?, LAB=?, USER=?, ID=?, DATE=?, TIME=?, WHERE id=?", (NAME, PARISH, TELEPHONE, EMAIL, TEST, LAB, USER, ID, DATE, TIME)
		self.conn.commit()
	def delete (self, id):
		self.cur.execute("DELETE FROM db WHERE id=?", (id,))
		self.conn.commit()
	def __del__(self):
		self.conn.close()










	