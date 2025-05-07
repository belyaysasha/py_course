class Follower:
    def __init__(self, name):
        self.follower_name = name
    def react(self):
        print(self.follower_name, "like the mess")
    def __str__(self):
        return f"follower({self.follower_name})"
    def __repr__(self):
        return f"rep ({self.follower_name})"

    
class creator:
    def __init__(self, name):
        self.sub_list = []
        self.creator_name = name        
    def follow(self, follower):
        self.sub_list.append(follower)
    def show_followers(self):
        print(self.sub_list)
    def notify_all(self):
        for follower in self.sub_list:
            follower.react()
    def create_post(self, message):
        print(self.creator_name, "public the message:")
        print(message)
        print()
        self.notify_all

creator1 = creator("MyChannel")
f1 = Follower("Peta")
f2 = Follower("Petr")
f3 = Follower("Petachok")

creator1.show_followers
creator1.follow(f1)
creator1.create_post("reegrogneorig")
creator1.follow(f2)
creator1.create_post("reegrogndfdgdfheorig")
creator1.follow(f3)
creator1.create_post("reegrogneorisfdg")
creator1.show_followers()
creator1.create_post("reegrogneorig")
