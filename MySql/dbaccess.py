import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'poopyface11924',
    database = 'accounts'
)

mycursor = mydb.cursor()

def user_exists(username):
    query = f'SELECT name FROM account WHERE name = "{username}"'

    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return len(myresult) > 0

def create_user(username, password):
    if(user_exists(username)):
        return False

    query = f'INSERT INTO account (name, password) VALUES ("{username}", "{password}")'

    mycursor.execute(query)
    myresult = mycursor.fetchall()
    mydb.commit()

    return True

def change_pass(username):
    if(not user_exists(username)):
        return False
    
    query = f'SELECT password FROM account WHERE name = "{username}"'
    mycursor.execute(query)
    dbpass = mycursor.fetchall()[0][0]


    password = input('Enter current password: ')
    if password == dbpass:
        for _ in range(5):
            new_pass = input('Enter new password: ')
            if new_pass == input('Confirm new password: '):
                query = f'UPDATE account SET password = "{new_pass}" WHERE name = "{username}"'

                mycursor.execute(query)
                mydb.commit()

                return True

def confirm_login(username, password):
    query = f'SELECT password FROM account WHERE name = "{username}"'
    mycursor.excecute(query) 
    dbpass = mycursor.fetchall()[0][0]
    if password == dbpass:
        return True
    return False
        

change_pass('tanush')

# flag = True
while flag:
    username = input('Enter username: ')
    password = input('Enter password: ')
    conf_pass = input('Confirm password: ')
    
    if(password == conf_pass):
        if(create_user(username, password)):
            # account successfully created
            flag = False
        else:
            # account not created
            continue
    else:
        print('Passwords do not match! Try again.')