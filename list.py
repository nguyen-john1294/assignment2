class Listclass:
    def __init__(self): #declaring local variables
        self.things = []
        self.keys = []
        self.combined_dict = {}

    def get_list(self):
        list_size = int(input("Enter the size of list: ")) #list must match size for dict conversion
        for i in range(list_size): #loop entry for data
            entry = input("Enter next list entry: ")
            self.things.append(entry)
            entry = input("Enter next key entry: ")
            self.keys.append(entry)
        print("Input:") 
        print(self.things)
        print(self.keys)

    def make_dict(self): #turns the two list into a dict while keeping the original 2 list
         for i in range(len(self.things)):
              self.combined_dict[self.keys[i]] = self.things[i] 
    
def main():
        tester = Listclass() # make object
        tester.get_list() # make list
        tester.make_dict() # make dict
        print("Output:") # output check
        print(tester.combined_dict)

main()