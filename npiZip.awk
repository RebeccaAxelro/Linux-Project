BEGIN{

    # The dataset being extracted from
    npiData = "zcat npi.gz"

    # This dataset is tab delimited
    FS = "|"

    # Parse through npiData and if npi and zip code are note empty, then print the npi and the first 5 numbers of the zip code to npiandZip.txt
    while ((npiData | getline) > 0){	

	npi = $1
	zipCode = substr($33, 1, 5)
	if ( (npi != "") && (zipCode !="") ){
		if((npi ~ /[0-9]*/) && (zipCode ~ /[0-9]*/)){
		    print npi, zipCode > "npiandZip.txt"
		}
	}
	
    }
    
}
