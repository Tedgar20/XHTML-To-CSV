#/bin/bash

touch weather.csv
echo "state,city,weather,temperature,humidity,pressure" > weather.csv

while true; do
	NY=`date '+%Y-%m-%d-%H-%M-%S'`-NY.html
	`touch ${NY}`
	echo `curl -L https://forecast-v3.weather.gov/point/40.78,-73.97` > ${NY}     #NY, New York
	`java -jar tagsoup-1.2.1.jar --files ${NY}`

	CA=`date '+%Y-%m-%d-%H-%M-%S'`-CA.html
	`touch ${CA}`
	echo `curl -L https://forecast-v3.weather.gov/point/34.02,-118.45` > ${CA}     #CA, Los Angeles
	`java -jar tagsoup-1.2.1.jar --files ${CA}`

	IL=`date '+%Y-%m-%d-%H-%M-%S'`-IL.html
	`touch ${IL}`
	echo `curl -L https://forecast-v3.weather.gov/point/41.78,-87.76` > ${IL}     #IL, Chicago
	`java -jar tagsoup-1.2.1.jar --files ${IL}`

	TX=`date '+%Y-%m-%d-%H-%M-%S'`-TX.html
	`touch ${TX}`
	echo `curl -L https://forecast-v3.weather.gov/point/29.64,-95.28` > ${TX}     #TX, Houston
	`java -jar tagsoup-1.2.1.jar --files ${TX}`

	AZ=`date '+%Y-%m-%d-%H-%M-%S'`-AZ.html
	`touch ${AZ}`
	echo `curl -L https://forecast-v3.weather.gov/point/33.69,-112.07` > ${AZ}     #AZ, Phoenix
	`java -jar tagsoup-1.2.1.jar --files ${AZ}`

	PA=`date '+%Y-%m-%d-%H-%M-%S'`-PA.html
	`touch ${PA}`
	echo `curl -L https://forecast-v3.weather.gov/point/40.08,-75.01` > ${PA}     #PA, Philadelphia
	`java -jar tagsoup-1.2.1.jar --files ${PA}`

	FL=`date '+%Y-%m-%d-%H-%M-%S'`-FL.html
	`touch ${FL}`
	echo `curl -L https://forecast-v3.weather.gov/point/30.23,-81.67` > ${FL}     #FL, Jacksonville
	`java -jar tagsoup-1.2.1.jar --files ${FL}`

	for file in *.xhtml
	do
	    echo `python makeCSV.py ${file}` >> weather.csv
	done
	sleep 1h
done
