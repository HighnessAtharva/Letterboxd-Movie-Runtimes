import requests
import json
import csv
import os
import time

# Set your API key as enviroment variable. Key should be 'TMDB_KEY' or replace it directly here instead of os.getenv()
API_KEY=os.getenv('TMDB_KEY')

def sanitize(movie_name):
    """
    Takes in a movie name containing spaces and returns a sanitized URL version of it.
    """
    return movie_name.replace(' ', '+')
    

def get_movie_id(API_KEY, movie_name, movie_year):
    """
    Takes in a movie name and release year, queries it using the API and return the movieID.
    """
    movie_name=sanitize(movie_name)
    query=f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}'
    # query=f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}&primary_release_year={movie_year}'
    # print(query)
    response =  requests.get(query)
    if response.status_code != 200:
        return ("error")
    results = response.json()['results']
    if len(results) > 0:
        return results[0]['id']
    else:
        return None
        

def get_runtime(API_KEY, movie_id):
    """
    Takes in a movieID and returns its movie name and runtime in minutes.
    """
    query=f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US'
    # print(query)
    response =  requests.get(query)
    if response.status_code != 200:
        return ("error")
    movie_name=response.json()['original_title']
    runtime=response.json()['runtime']
    return (movie_name, runtime)


def read_csv(csv_file):
    """
    Takes in the name of the CSV file. Reads the file and displays the formatted contents. Shows a total row count at the end.
    """
    try:
        with open(csv_file, encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                else:
                    print(f'\tName: {row[1]} | Year: {row[2]}.')
                line_count += 1
            print(f'Read {line_count} movies.')
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("I/O error.")
    

def calculate_runtime(csv_file): 
    """
    Takes in the name of the CSV file, reads it, simultaneously calculates the runtime of each movie and writes it to a new CSV file. Also, displays the calculated runtime of each movie and the total runtime of all movies to the command line.
    """
    try:
        # Read the CSV file
        with open(csv_file, encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0  
            total_runtime_minutes = 0
            
            # Create a new CSV file to write the calculated runtime to
            with open('letterboxd_runtimes.csv', encoding="utf8", mode='w', newline='') as csv_file:   
                # Set the column headers as the first row in the new CSV file
                fieldnames = ['MovieName', 'Runtime (in minutes)']
                # Write the column headers to the new CSV file
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                # iterate over the rows in the CSV file. 
                for row in csv_reader:
                    # If the row is the first row, skip it
                    if line_count == 0:
                        print('Calculating The Runtime...')
                        print('-----------------------------------------------------')
                        total_start = time.time()
                    else:
                        start_time = time.time()
                        # Row 1 is Movie Title from the CSV file.
                        name=row[1] 
                        # Row 2 is Movie Release Year from the CSV file.
                        release=row[2]
                        # Pass in the details and grab the movie ID
                        movie_id=get_movie_id(API_KEY, name, release)

                        if movie_id is None:
                            print(f'Error: {name} not found.')
                            break
                        # Get the movie name and runtime by passing the movie ID
                        movie_name, runtime=get_runtime(API_KEY, movie_id)
                        # update the total runtime in minutes by adding the runtime of each movie
                        total_runtime_minutes+=runtime
                        
                        # Conversion of runtime in minutes to runtime in hours and minutes format
                        hours = total_runtime_minutes // 60
                        minutes = total_runtime_minutes % 60
                        total_runtime_hours = f'{hours}H {minutes}M'
                        total_runtime_days = f'{hours//24}D {hours%24}H {minutes}M'

                        print(f'{movie_name} - {runtime}')
                        print(f'Total Runtime till now: {total_runtime_minutes} minutes OR {total_runtime_hours} OR {total_runtime_days}.')
                        

                        # Write the movie name and runtime to the CSV file. Format is Dictionary and key value pairs.
                        print('Writing to file letterboxd_runtimes.csv...')    
                        writer.writerow({'MovieName': movie_name, 'Runtime (in minutes)': runtime})
                         
                        end_time = time.time()
                        print(f'Time taken: {end_time - start_time:.4f}s')

                        print('\n-----------------------------------------------------\n')
                    line_count += 1
        print("SUCCESS!")
        print(f'Finished Calculating Runtime of  {line_count} movies.')
        print(f'Total Runtime Report: {total_runtime_minutes} minutes OR {total_runtime_hours} OR {total_runtime_days}.')
        total_end = time.time()
        print(f'Total Time taken to process: {total_end - total_start:.4f}s')
    except ValueError as e:
        print(e)
    except FileNotFoundError:
         print("File not found.")

# Uncomment to debug if required
"""        
 movie_id=get_movie_id(API_KEY, '(500) Days of Summer', 2009)
 # print(movie_id)
 movie_name, runtime=get_runtime(API_KEY, movie_id)
 print(f'{movie_name} - {runtime}\n')
"""

# run the driver functions
read_csv(csv_file='watched.csv')
calculate_runtime(csv_file='watched.csv')
