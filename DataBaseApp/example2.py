import MySQLdb

class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host = self.host,
                user = self.user,
                passwd = self.password,
                db = self.db,
                use_unicode=True,
                charset='utf8'
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()

class Team:
    def __init__(self, db_connection, name, description):
        self.db_connection = db_connection.connection
        self.name = name
        self.description = description

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO team (name, description) VALUES (%s, %s);", (self.name, self.description))
        self.db_connection.commit()
        c.close()

class Teams:
    def __init__(self, db_connection):
        self.db_connection = db_connection.connection

    def select_all(self):
        c = self.db_connection.cursor()
        c.execute("SELECT * FROM team;")
        teams = c.fetchall()
        c.close()
        return teams

    def delete_all(self):
        c = self.db_connection.cursor()
        c.execute("TRUNCATE table team;")
        self.db_connection.commit()
        c.close()


con = Connection('root', '', 'db_first')
with con:
    team = Team(con, 'ЦСКА', 'Профессиональный футбольный клуб')
    team.save()
    team = Team(con, 'Зенит', 'Просто Зенит')
    team.save()
    teams = Teams(con)
    select_teams = teams.select_all()
    print(select_teams)
    teams.delete_all()
    print('---------------------')
    select_teams = teams.select_all()
    print(select_teams)




