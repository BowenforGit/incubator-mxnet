outputfile=results.csv
echo "Mode,Workers,Time" >> results.csv
for mode in "sync" "synccol" "async" "asynccol"
do
	for nworkers in 2 4 6 8
	do
		filename="log-$mode-$nworkers.txt"
		if test -f $filename; then
			echo "Processing results for $filename"
			avg=$(cat $filename | grep Average | cut -d: -f2 | jq -s add/length)
			echo "$mode,$nworkers,$avg" >> $outputfile
		fi
	done
done
