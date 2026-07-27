#################################################
 # CS03B - Summer 2026
 # Assignment 2 - Question 2
 # Student Name: John Nguyen
 # SID: 20319444
 #################################################
class Dictclass:
    def __init__(self): #declaring local variables
        self.user_dict = {}
        self.search_dict = {}

    def get_dict(self):
        dict_size = int(input("Enter the size of dict: ")) #dict1

        for i in range(dict_size): #loop entry for data
            user_key = input("Enter next key entry: ")
            user_data = input("Enter next data entry: ")
            self.user_dict[user_key] = user_data

        dict_size = int(input("Enter the size of dict 2: ")) #dict 2
        
        for i in range(dict_size): #loop entry for data
            user_key = input("Enter next key entry: ")
            user_data = input("Enter next data entry: ")
            self.search_dict[user_key] = user_data

    def compare_dict(self): # compares the 2 dicts
        for key in self.user_dict:
                if key in self.search_dict and self.user_dict[key] == self.search_dict[key]:
                    print(str(key) + ": " + str(self.user_dict[key]) + " is in both user and search dict")

            

def main():
        tester = Dictclass() # make object
        tester.get_dict() # make dict to compare
        tester.compare_dict() # ]compares

main()