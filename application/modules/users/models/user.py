from core.DBModel import DBModel


class User(object):

    def __init__(self):
        self.user_id = 0
        self.name = ''
        self.last_name = ''

    def index(self):
        sql = "SELECT user_id from user WHERE user_id > 0"
        return DBModel().execute(sql)

    def get(self):
        sql = """SELECT user_id, name, email
            FROM user WHERE user_id = %d LIMIT 1""" % (self.user_id)
        results = DBModel().execute(sql)
        for row in results:
            self.user_id = row[0]
            self.name = row[1]
            self.email = row[2]

    def save(self):
        if(self.user_id == 0):
            sql = "INSERT INTO user (name, email) VALUES ('%s', '%s')" % (
                self.name, self.email)
            self.user_id = DBModel().execute(sql)
        else:
            sql = """UPDATE user SET name = '%s', email = '%s'
            WHERE user_id = %d""" % (self.name, self.email, self.user_id)
            self.user_id = DBModel().execute(sql)

    def destroy(self):
        sql = "DELETE FROM user WHERE user_id = %d" % (self.user_id)
        DBModel().execute(sql)

