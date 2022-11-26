class User:
    name_user = ""
    password_user = ""
    email_user = ""

    def __init__(self):
        pass

    def getName(self)->str:
        return self.name_user

    def setName(self, name:str):
        self.name_user = name
        del self.name_user

    def getEmail(self)->str:
        return self.email_user
    
    def setEmail(self, email:str):
        self.email_user = email
    
    def getPassword(self)->str:
        return self.password_user

    def setPassword(self, password:str):
        self.password_user = password


user = User()
user.setName("Carlos Eduardo")
user.setEmail("eduardo@hotmail.com")
user.setPassword("2331313")

print(user.getEmail())
print(user.getName())
print(user.getPassword())
