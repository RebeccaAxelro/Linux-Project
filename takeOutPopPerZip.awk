BEGIN{

    # Cat the Census data which is data for ages 65+, we will use to get the population per zip code
    popPerZip = "cat CENSUS_AGE65.csv"

    # Comma delimited
    FS = ","

    # Go through each record in the Cenesus data and make sure the zip code ($2) and population ($6) are accurate representations and print to a file popZip.txt
    while (( popPerZip | getline) > 0){
	if (($2 ~ /[0-9]{5}/) && ($6 ~ /[0-9]*/)){
	    print $2, $6 > "popZip.txt"
	}
    }

}
