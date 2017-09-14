
# coding: utf-8

# In[1]:

fileName = input("File:") # user gives me a file name
f = open(fileName + ".csv", "r") # add .csv extension and open file
content = f.read() # read the whole content 
f.close() # close file

print("Reading the data...")

rows = content.split("\n")

ASpent = []
BSpent = []
AEarned = []
BEarned = []

for row in rows:
    if row == "":
        continue
        
    cols = row.split(",")
    truck = cols[0].upper() # A/B
    cat = cols[1] # spent/earned
    amount = float(cols[2]) # $ amount
    
    if truck != "A" and truck != "B":
        print ("Invalid truck " + truck + " !")
    if cat != "earned" and cat != "spent":
        print ("Invalid category " + cat + " !")
    
    if truck == "A" and cat == "earned":
        AEarned.append(amount)
    elif truck == "A" and cat == "spent":
        ASpent.append(amount)
    elif truck == "B" and cat == "earned":
        BEarned.append(amount)
    elif truck == "B" and cat == "spent:":
        BSpent.append(amount)

        
print ("Done Reading Data. Starting Analysis...")

print ("On truck A, we spent " + str(sum(ASpent)))
print ("On truck A, we earned " + str(sum(AEarned)))
print ("On truck A, we profit " + str(sum(AEarned)-sum(ASpent)))
print ("On truck A, average earned " + str(sum(AEarned)-sum(ASpent)))

print ("On truck B, we spent " + str(sum(BSpent)))
print ("On truck B, we earned " + str(sum(BEarned)))
print ("On truck B, we profit " + str(sum(BEarned)-sum(BSpent)))
print ("On truck B, average earned " + str(sum(BEarned)/len(BEarned)))

        
print ("In total, we spent " + str(sum(ASpent)+sum(BSpent)))
print ("In total, we earned " + str(sum(AEarned)+sum(BEarned)))
print ("In total, we profit " + str(sum(AEarned)-sum(ASpent))+(sum(BEarned)-sum(BSpent)))


# In[ ]:



