class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def greet(self):
        return f"Hello, {self.username}!"

# Creating an instance of the User class
user1 = User("JohnDoe", "johndoe@example.com")

# Accessing attributes and calling methods
print(user1.username)  # Output: JohnDoe
print(user1.greet())   # Output: Hello, JohnDoe!
