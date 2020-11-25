class User:
    """User class"""

    def __init__(self, id=None, username=None):
        """Constructor to initialize attributes"""
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


# Creating object without setting attributes
user_1 = User()
user_1.id = "001"
user_1.username = "ashutoshkrris"

print(user_1.id, user_1.username)

# Creating object and setting attributes at the same time
user_2 = User('002', 'ashutosh')
print(user_2.id, user_2.username)

user_1.follow(user_2)
print(user_1.followers, user_1.following)
print(user_2.followers, user_2.following)
