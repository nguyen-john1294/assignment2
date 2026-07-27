#################################################
 # CS03B - Summer 2026
 # Assignment 2 - Question 3
 # Student Name: John Nguyen
 # SID: 20319444
 #################################################
class Stringwork:
    def __init__(self):
        userwords = ""
        words = []

    def getstr(self):
        self.userwords = input("Enter a sentence to reverse:")
        self.words = self.userwords.split()
        #print(self.words) Tester for split output

    def reverse(self):
        
        revwords = [] # list to store reversed words
        for word in self.words: 
            rev = ""
            for char in word:
                rev = char + rev
            revwords.append(rev)
        #print(revwords) tester line for reversing words
        self.words.clear()
        for word in revwords:
            self.words.append(word)
        print(" ".join(self.words)) # adds the spaces back in between the words and prints the reversed sentence

def main():
    tester = Stringwork()
    tester.getstr()
    tester.reverse()

main()
