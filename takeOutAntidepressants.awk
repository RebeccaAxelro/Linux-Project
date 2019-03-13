BEGIN{

    # This file is a list of antidepressants taken from https://www.fda.gov/downloads/Drugs/DrugSafety/InformationbyDrugClass/UCM161647.pdf
    antidepressants = "antidepressants.txt"
    medicareData = "zcat Medicare.gz"

    # Makes a list of antidepressants from  antidepressants.txt
    while ((getline < antidepressants) > 0){
	antidepressant[$1] = $1
    }
    
    # Medicare Data is tab delimited
    FS = "\t"

    
    # Parse through  Medicare data, if the drug name or genric name is in the list of antideprsessants, then write to a a file (antideprecords.txt) the npi number and antidepressant 
    while((medicareData | getline) > 0){
	
	if(tolower($8) in antidepressant){ print $1, $8 > "antideprecords.txt" }

	if(tolower($9) in antidepressant){ print $1, $9 > "antideprecords.txt" }
   }
    
}
