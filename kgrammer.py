#################################################
 # CS03B - Summer 2026
 # Assignment 2 - Question 4
 # Student Name: John Nguyen
 # SID: 20319444
 #################################################
class Kgrammer:
    def pattern(self,row,column):
        start = "0"
        finish = ""
        print("row 1: " + start)
        
        for i in range(1,row):# loop for number of rows except row 1 which is always the same
            for char in start:
                if char == "0":
                    finish += "01"
                elif char == "1":
                    finish += "10"
            print("row " + str(i + 2 ) + ": " + finish) # fixing weird indexing printing
            start = finish # updates start for next row

        print("Index: " + finish[column-1]) 


def main():
    tester = Kgrammer()
    row = int(input("Enter the number of rows: "))
    column = int(input("Enter index to return: "))
    tester.pattern(row,column)

main()