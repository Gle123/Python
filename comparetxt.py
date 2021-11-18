#comparing two text files and displaying the differences between the two
import sys

def compare(textFile1,textFile2): #send both arrays to this function

    for i in range (0,len(textFile1),1):
        for j in range (0,len(textFile2),1):
            if textFile1[i] == textFile2[j]: #if match
                #increment i
#                print("Match found")
#                print(textFile1[i])
                break
            if j == len(textFile2)-1: #if no match has been found display the field
                print(textFile1[i]) 
                break
                
textArr1 = []
textArr2 = []
#print(len(sys.argv))
if len(sys.argv) != 3:
    print("Make sure to provide 2 extra arguments")
    quit()
else:
    fName1 = sys.argv[1]
    fName2 = sys.argv[2]
    
#    print(fName1)
#    print(fName2)
    
    
#potentially pass values from a function and assign it to a list
try: #opening text file 1
    with open(fName1, 'r') as txtFile1:
        #do input with taking each value as a listed value within textArr1
        
        while True:
            #get next line from file
            line = txtFile1.readline()
            textArr1.append(line)
            
        #if line is empty / end of file is reached
            if not line:
                txtFile1.close()
                break
        txtFile1.close()
except IOError:
    print("Could not read file:",fName1)
    quit()
    
try: #opening text file 2
    with open(fName2, 'r') as txtFile2:
        #do input while taking each value as a listed value within textArr2
        
        while True:
            #get next line from file
            line = txtFile2.readline()
            textArr2.append(line)
        #if line is empty / end of file is reached
            if not line:
                break
        txtFile2.close()
except IOError:
    print("Could not read file:", fName2)
    quit()
 
print(fName1)
print("SHEET ONE DIFFERENCES") #displaying textArr1 differences
compare(textArr1,textArr2)
print(fName2)
print("SHEET TWO DIFFERENCES") #displaying textArr2 differences
compare(textArr2,textArr1)