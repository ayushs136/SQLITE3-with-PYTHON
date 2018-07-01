import sqlite3

cn = sqlite3.connect('geeks.db')
c= cn.cursor()

def createTable():
	c.execute('CREATE TABLE IF NOT EXISTS geeks(Username TEXT, FullName TEXT, Email Varchar, Password BLOB)')

	

def data_entry():
	Username = str(input("Enter Username: "))
	FullName =str(input("Enterr FullName: "))
	Email = str(input("Enter Email:"))
	Password = str(input("Enter Password: "))
	c.execute("INSERT INTO geeks(Username, FullName, Email, Password) VALUES (?,?,?,?)", (Username, FullName, Email, Password))
	cn.commit()

def read_from_db():
	c.execute("SELECT * FROM geeks")
	data = c.fetchall()
	# print(data)
	for row in data:
		print(row)

def search(id):
	c.execute("SELECT * FROM geeks WHERE Username=?", (id,))
	data = c.fetchall()
	for row in data:
		print(row)

def delete_record():
	id = input("Enter Username: ")
	quit = True
	search(id)
	r = input("Are you sure you wanna delete this record(y/n): ")

	while quit:
		if r == 'y':
			c.execute("DELETE FROM geeks WHERE Username=?", (id,))
			cn.commit()
			print("Record Deleted...")
			break
		elif r=='n':
			quit = False
		else:
			print("Wrong input...")


def update():
	# c.execute('SELECT * FROM geeks')
	# [print(row) for row in c.fetchall()]
	pattern = ""
	quit = True
	while  quit:
		print("Press\n1. to change Password\n2. to change FullName\n3. to Quit\n")

		Choice = int(input("Your Choice: "))
		if Choice == 1:
			id = str(input("Enter Username: "))
			search(id)
			pattern = str(input("Enter New Password: "))
			c.execute("UPDATE geeks SET Password=? WHERE Username=?", (pattern, id))
			cn.commit()
			print("Password Updated....")
			break
		elif Choice == 2:
			id = input("Enter Username: ")
			search(id)
			pattern = str(input("Enter New Name: "))
			c.execute("UPDATE geeks SET FullName=? WHERE Username=?", (pattern, id))
			cn.commit()	
			print("Name Updated...")
			break
		elif Choice == 3:
			quit = False
		else:
			print("Wrong Input...")


	

def menu():
	print("Press\n1. to insert data in table\n2. Read the Record\n3. to update the Record\n4. to delete a record\n5. to Quit\n")


def calling():
	quit = False
	while not quit:
		print("\n--------------------------------\n")
		menu()
		what = int(input("Enter your Choice: "))
		if what == 1:
			print("\n=================================\n")
			data_entry()
		elif what == 2:
			print("\n=================================\n")
			read_from_db()
		elif what == 3:
			print("\n=================================\n")
			update()
		elif what == 4:
			print("\n=================================\n")
			delete()
		elif what == 5:
			print("\n=================================\n")
			quit = True
			print("Going out...")
		else:
			print("\n=================================\n")
			print("Wrong Input...")


calling()

c.close()
cn.close()