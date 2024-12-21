# geovelo-geojson

## Why this project ?

I wanted to visualise all the trips I made with Geovelo on a map.
After downloading my data from Geovelo, the json file named _sent_traces.json_ didn't really work as a geojson file and needed to be worked on for it to work on [geojson.io](https://geojson.io) or QGIS.

## How do I use it ?

To run the script, you need to have python installed and use the following command

> ./geovelo-geojson.py -i sent_traces.json -o youroutputfile.json

Parameters :

- -i / --input : input file provided by geovelo
- -o / --output : name of your output file
