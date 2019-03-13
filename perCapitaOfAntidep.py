# Open the files we created 
numAntidepPerZip = open("numAntidepPerZip.txt", "r")
popPerZip        = open("popZip.txt", "r")
# Open a new file with write permissions
percapitaPop     = open("percapitaPop.txt", "w")

# Create the dictionaries
dictPopZip = {}
dictAntiZip = {}

#Create the variables (zipcode and population) when going through popPerZip file
#Then add into a dictionary: the key being the zipCode and data being the population
for line in popPerZip:
    field = line.split()
    zipC = field[0]
    population = field[1]
    dictPopZip[zipC] = population

#Close file
popPerZip.close()

#Create the variables (zipcode and number of antidepressants) when going through numAntidepPerZip file
#Then add into a dictionary: the key being the zipCode and data being the number of antidepressants
for line in numAntidepPerZip:
    field = line.split('|')
    zipCo = field[0]
    numAnti = field[1].strip('\n')
    dictAntiZip[zipCo] = numAnti

#Close file
numAntidepPerZip.close()

# Go through each key (zip code) of the dictionary dictPopZip and see if that zip code is also in another dictionary dictAntiZip
for zipCode in dictPopZip:
    if zipCode in dictAntiZip:
        # If so, get the number of antidepressants divided by the population of that zip code, and thats your per capita that you will write to a file with the corresponding population
        numAnti = int(dictAntiZip[zipCode])
        population = int(dictPopZip[zipCode])
        perCapita = (numAnti/population) * 100
        percapitaPop.write(str(perCapita) + "|" +  str(population) + '\n')
