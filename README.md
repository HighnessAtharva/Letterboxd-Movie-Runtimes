# Letterboxd-Movie-Runtimes
A Python CLI Script that gets the total runtime of the letterboxd movies logged from your account. Can also be used to get the total runtime of watchlisted movies, instructions below.

# Usage

## Get Your TMDB API KEY
https://www.themoviedb.org/settings/api

## Export Your Letterboxd Data
Go to https://letterboxd.com/settings/data/, click on the `Import and Export` tab and `Export your data`.Extract the downloaded zip and place the `watched.csv` file in the same folder as that of the Python Script.

If you would like to get the runtime of your watchlisted movies instead, just copy the `watchlist.csv` file and place it in the same folder as the Python script, but rename it to `watched.csv` before continuing.

## Run the Python Script
- IMPORTANT! - Set your `TMDB_KEY` as the environment variable before running the Python Script.
- To do this you can used the following command on
    - bash or zsh: `export TMDB_KEY="your_api_key"`
    - Windows cmd prompt: `setx TMDB_KEY "your_api_key"`
    - Powershell: `$env:TMDB_KEY = "your_api_key"`

- Run the script from your CLI as demonstrated in the image below
![lbx1](https://user-images.githubusercontent.com/68660002/180614312-2e3c7b88-07bb-45ed-8e15-e83630dfedcd.JPG)

- You will be able to view the progress in real time from the command line as CSV file is being read and processed.
![lbx2](https://user-images.githubusercontent.com/68660002/180614316-a28151a9-edfe-4a2e-b971-7b8d4e733373.JPG)

- A new CSV file will be generated with 2 columns - `Name` and `Runtime` of each movie you have logged in to your Letterboxd account. 
![lbx3](https://user-images.githubusercontent.com/68660002/180614320-9d871e9a-28dc-40fd-89a1-c94f4463760a.JPG)
