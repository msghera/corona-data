# Data Fetcher for COVID-19

It is seen that ***covid-19 data*** for small research purposes  is unavailable in the format of csv. To fulfill this requirement this repo is created. 

### Prerequisites

Python module ***requests*** and ***pandas*** are required for this projects.

```
pip install requests
pip install pandas
```

## Running the project 

First clone the project 
```
https://github.com/msghera/corona-data.git
```

Change directory to the folder
```
cd corona-data
```

There are two ways to run the project 
```
[1] python corona_data.py
[2] python corona_data.py {country_name}
```
running [2] will create two more files than [1] based on country specific data.

You might find the files in the data folder in a folder with the timestamp the script started to run.

## Authors

* [**Mohamad Sheikh Ghazanfar** - *Nascenia IT*](https://github.com/msghera)

You are highly wellcome as a contributor. 

## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* This is basically a wrapper for [NovelCOVID/API/](https://github.com/NovelCOVID/API/) 
* Data is fetched from [here](https://www.worldometers.info/coronavirus/)

## Disclaimer

* Any gurantee of authentic data is not provided. 