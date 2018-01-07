import MySQLdb

db = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='',
    db='db_first',
    use_unicode=True,
    charset='utf8'
)

c = db.cursor()

c.execute("INSERT INTO team (name, description) VALUES (%s, %s);", ('Зенит', 'Профессиональный футбольный клуб'))
db.commit()

c.execute("SELECT * FROM team;")
teams = c.fetchall()
for team in teams:
    print(team)

c.execute("DELETE FROM team;")
db.commit()

c.execute("SELECT * FROM team;")
teams = c.fetchall()
print('БД после удаления:')
for team in teams:
    print(team)

c.close()
db.close()
