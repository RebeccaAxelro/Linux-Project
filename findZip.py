# Open these files that were created 
medFile = open("antideprecords.txt", "r")
npizip  = open("npiandZip.txt", "r")
# Open this new file, with write permissions
antidepPerZip = open("numAntidepPerZip.txt", "w")

# Create the dictionaries
dictNpiZip = {}
tallyZip = {}

# Go through npizip.txt and create a dictionary: key is the npiforzip and data is the zip code
for line in npizip:
    field     = line.split()
    npiforzip = field[0]
    zipcode   = field[1]

    dictNpiZip[npiforzip] = zipcode

# Close file
npizip.close()        

# Go through the antideprecords.txt file
for record in medFile:

    fields = record.split()
    npi = fields[0]
    antidep = fields[1]

    # Check is the npi in antideprecords.txt is in the dictionary we created, if so then tally how many times the npi comes up, to keep track of the number of antidepressants for each npi
    if npi in dictNpiZip:
        
        if dictNpiZip[npi] in tallyZip:
            tallyZip[dictNpiZip[npi]] += 1
        else:
            tallyZip[dictNpiZip[npi]] = 1

# Close file
medFile.close()

# Collect each zip  code and tally within each item of tallyZip and write it to the new file antidepPerZip
for zipCode, tally in tallyZip.items():
    antidepPerZip.write(str(zipCode) + "|" + str(tally) + '\n')
    


