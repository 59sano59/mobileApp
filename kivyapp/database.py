import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            email, password, name, created = line.strip().split(";")
            self.users[email] = (password, name, created)

        self.file.close()

    def getUser(self, email):
        if email in self.users:
            return self.users[email]
        else: 
            return -1

    def addUser(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.getDate())
            self.save()
            return 1
        else:
            print("Sähköposti on jo käytössä")
            return -1
        
    def validate(self, email, password):
        if self.getUser(email) != -1:
            return self.users[email][0] == password
        else:
            return False
        
    def save(self):
        with open(self.filename, "w") as files:
            for user in self.users:
                files.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    @staticmethod
    def getDate():
        return str(datetime.datetime.now()).split(" ")[0]