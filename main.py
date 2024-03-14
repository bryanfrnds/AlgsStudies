class StarCookie:
    milk = 0.1
    def __init__(self,color,weight):
        self.weight = color
        self.color = weight
    
    
star_cookie1 = StarCookie("Red", 15)
print(star_cookie1.weight)
print(star_cookie1.color)
print(star_cookie1.__dict__)
print(StarCookie.__dict__)



class Youtube:
    def __init__(self, username, subscribers=0, subscriptions=0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions
    
    def subscribe(self,user):
        user.subscribers += 1
        self.subscriptions += 1
        
        

user1 = Youtube("Bryan" )

print(user1.username)
print(user1.subscribers)


user2 = Youtube("Fernd")
user2.subscribers = 5

user1.subscribe(user2)
print(user2.username)
print(user2.subscribers)
print(user2.subscriptions)
print(user1.subscriptions)