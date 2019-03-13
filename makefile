all: graph.pdf clearGraph.pdf

clean:
	rm antideprecords.txt npiandZip.txt numAntidepPerZip.txt popZip.txt percapitaPop.txt graph.pdf clearGraph.pdf

antideprecords.txt: antidepressants.txt Medicare.gz
	gawk -f ./takeOutAntidepressants.awk

npiandZip.txt: npi.gz
	gawk -f ./npiZip.awk

numAntidepPerZip.txt: antideprecords.txt npiandZip.txt
	python3 ./findZip.py

popZip.txt: CENSUS_AGE65.csv
	gawk -f ./takeOutPopPerZip.awk

percapitaPop.txt: numAntidepPerZip.txt popZip.txt
	python3 ./perCapitaOfAntidep.py | sort

graph.pdf: graph.py percapitaPop.txt
	python3 ./graph.py

clearGraph.pdf: clearGraph.py percapitaPop.txt
	python3 ./clearGraph.py
