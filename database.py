import mysql.connector as sql

con = sql.connect(host='sql6.freesqldatabase.com', 
                  user='sql6585984', 
                  passwd='AbApRb9gI5', 
                  database='sql6585984')

mycursor = con.cursor(buffered=True)

try:
    mycursor.execute("""
                    CREATE TABLE IF NOT EXISTS answername(
                        username VARCHAR(150),
                        qid INT
                    );
    """)
    
    con.commit()

except:
    con.rollback()

try:
    mycursor.execute("""
                    CREATE TABLE IF NOT EXISTS user(
                        uid INT PRIMARY KEY AUTO_INCREMENT,
                        username VARCHAR(100),
                        gmail VARCHAR(100),
                        passwd VARCHAR(100),
                        score INT DEFAULT 0
                    );
    """)
    
    con.commit()

except:
    print('Hi1')
    con.rollback()
    
try:
    mycursor.execute("""
                     CREATE TABLE IF NOT EXISTS quiz(
                         question VARCHAR(200),
                         options VARCHAR(200),
                         answer INT,
                         username VARCHAR(150),
                         qid INT PRIMARY KEY AUTO_INCREMENT
                     );
    """)
    
    con.commit()
    
except:
    print('Hi2')
    con.rollback()

curUser = None
score = 0
first = True
answersL = []
state = 1
answerNameL = []
qidL = []
correctAns = True
corrupted = False
submitB = True
fState = True

print(qidL, 'Database')

def reset():
    global answersL, state, score, corrupted, fState, submitB, correctAns, first
    answersL = []
    state = 1
    score = 0
    corrupted = False
    fState = True
    submitB = True
    correctAns = True
    first = True

def insertValues(user, mail, passwd):
    if checkGmailName(mail, user):
        sql = '''
        INSERT INTO user(username, gmail, passwd) VALUES('{}', '{}', '{}');
        '''.format(user, mail, passwd)
            
        try:
            mycursor.execute(sql)
            con.commit()
        except:
            con.rollback()

        return True
    return False

def checkGmailName(mail, username):
    sql = 'SELECT * FROM user WHERE gmail = \'{}\' or username = \'{}\';'.format(mail, username)
    
    try:
        mycursor.execute(sql)
    except:
        con.rollback()
        
    if mycursor.rowcount == 0:
        return True
    return False

def authenticate(username, passwd):
    sql = '''SELECT * from user WHERE username='{}' and passwd='{}';'''.format(username, passwd)
    
    try:
        mycursor.execute(sql)
    except:
        con.rollback()

    if mycursor.rowcount == 1:
        global curUser
        curUser = username
        return True
    return False

def answerName():
    sql = '''
    SELECT qid FROM answername WHERE username = '{}'
    '''.format(curUser)
    
    try:
        mycursor.execute(sql)
        data = mycursor.fetchall()
        for i in data:
            answerNameL.append(i[0])
        format_string = ','.join(map(str, answerNameL))
    except:
        pass
    
    return format_string

def addQuiz(ques, options, answer):
    sql = '''
    INSERT INTO quiz(question, options, answer, username) VALUES('{}', '{}', {}, '{}');
    '''.format(ques, options, answer, curUser)
    
    try:
        mycursor.execute(sql)
        con.commit()
    except:
        con.rollback()
    
    sql = '''
    UPDATE user SET score = score + 2 WHERE username = '{}';
    '''.format(curUser)
    
    try:
        mycursor.execute(sql)
        con.commit()
    except:
        con.rollback()

def answers():
    qids = answerName()
    if qids != '':
        sql = '''
        SELECT * FROM quiz WHERE username != '%s' AND qid NOT IN (%s) ORDER BY qid DESC;
        '''%(curUser, qids)
    else:
        sql = '''
        SELECT * FROM quiz WHERE username != '{}' ORDER BY qid DESC;
        '''.format(curUser)
    
    print(sql)
    
    try:
        mycursor.execute(sql)
        
        data = mycursor.fetchall()
        for i in data:
            answersL.append(i[2])
        print(answersL, 'answers')
    except:
        con.rollback()

def Qdata():
    qids = answerName()
    if qids != '':
        sql = '''
        SELECT * FROM quiz WHERE username != '%s' AND qid NOT IN (%s) ORDER BY qid DESC;
        '''%(curUser, qids)
    else:
        sql = '''
        SELECT * FROM quiz WHERE username != '{}' ORDER BY qid DESC;
        '''.format(curUser)
    
    try:
        mycursor.execute(sql)
    except:
        con.rollback()

def fetchData():
    try:
        data = mycursor.fetchone()
        qidL.append(data[4])
        return data
    except:
        pass

def updateScore():
    sql = '''
    UPDATE user SET score = score + '{}' WHERE username = '{}';
    '''.format(score, curUser)
    
    try:
        mycursor.execute(sql)
        con.commit()
    except:
        con.rollback()

def updateAnsName():
    print(qidL)
    for i in qidL:
        sql = '''
        INSERT INTO answername VALUES('{}', {});
        '''.format(curUser, i)
        
        try:
            mycursor.execute(sql)
            con.commit()
        except:
            con.rollback()

def leaderBoard():
    sql = '''
    SELECT username, score FROM user ORDER BY score DESC LIMIT 8;
    '''
    
    try:
        mycursor.execute(sql)
        return mycursor.fetchall()
    except:
        con.rollback()

def yourScore():
    sql = '''
    SELECT COUNT(*) + 1 FROM user WHERE username != '{}' AND 
    score > (SELECT score FROM user WHERE username = '{}');
    '''.format(curUser, curUser)
    
    try:
        mycursor.execute(sql)
        return mycursor.fetchall()
    except:
        con.rollback()
