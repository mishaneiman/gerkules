from pymongo import MongoClient


class GerkulesFood:
    def __init__(self, name, calories_100g):
        self.name = name
        self.calories_100g = calories_100g


class GerkulesMongodb:
    def __init__(self):
        self.gerkules_client = MongoClient("localhost", 27017, maxPoolSize=50)
        self.gerkules_database = self.gerkules_client["gerkules_database"]
        self.gerkules_foods = self.gerkules_database["foods"]
        self.gerkules_users = self.gerkules_database["users"]

    def add_user(self, user):
        if user.id in self.gerkules_users.distinct("User ID"):
            found_user = self.gerkules_users.find_one({"User ID": user.id})
            found_username = found_user['Username']
            if found_username != user.username:
                self.gerkules_users.update_one({"User ID": user.id}, {"$set": {"Username": user.username}})
            else:
                return
        else:
            new_user = {"User ID": user.id, "Username": user.username}
            self.gerkules_users.insert_one(new_user)

    def add_food(self, food):
        if food.name in self.gerkules_foods.distinct("Name"):
            print("Food already exists in database.")
        else:
            self.gerkules_users.insert_one({"Name": food.name, "Caloric Value (per 100g)": food.calories_100g})


