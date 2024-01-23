


#store a total numbers of row in a variable
row_line = 5

#create a outer loop and iterate the total rows 
for i in range(row_line + 1, 0, -1):
    for j in range(0, i - 1): #start a nested loop that reverse the row
        print("*" , end=" ") #print the asterisk 
    print(" ")



    