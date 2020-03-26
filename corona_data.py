from file_manager import FileManager
from fetcher import Fetcher
import pandas as pd
from sys import argv

def main():

    fm = FileManager()
    fe = Fetcher()

    folder_dir = fm.get_folder_dir()

    df = [fe.statistics(), fe.coutries_data(), fe.countries_historical_data()]
    filenames = ['statistics', 'all_country_data', 'all_country_historical_data']
    
    for i in range(3):
        filename = '{}/{}.csv'.format(folder_dir, filenames[i])
        df[i].to_csv(filename, index=False)

        print('{} is created successfully.'.format(filename))

    if len(argv) > 1:

        country = argv[1]
            
        df = [fe.coutry_data(country), fe.country_historical_data(country)]
        filenames = ['{}__country_data'.format(country), '{}__country_historical_data'.format(country)]
        
        
        for i in range(2):
            filename = '{}/{}.csv'.format(folder_dir, filenames[i])
            df[i].to_csv(filename, index=False)

            print('{} is created successfully.'.format(filename))

if __name__ == '__main__':
    main()
