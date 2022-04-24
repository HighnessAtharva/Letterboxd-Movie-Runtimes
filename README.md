# Letterboxd-Movie-Runtimes
Get the total runtime of the letterboxd movies logged from your account. 

## Get Your TMDB API KEY
https://www.themoviedb.org/settings/api

## Export Your Letterboxd Data
Go to https://letterboxd.com/settings/data/, click on the `Import and Export` tab and `Export your data`.Extract the downloaded zip and place the `watched.csv` file in the same folder as that of the Python Script.

## Run the Python Script
Set your TMDB_KEY as the environment variable before running the Python Script. A new CSV file will be generated with 2 columns - Name and Runtime of each movie you have logged in to your Letterboxd account. A command line result will also be displayed as the operation is being performed.