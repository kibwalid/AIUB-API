# AIUB-API

An Unofficial API Server for AIUB (American International University, Bangladesh) Portal and Website. It uses a Python Scraper to get the data from AIUB Database and creates JSON formated Data for your application. 

## Installation


Use [Git](https://git-scm.com/downloads) and package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements with the following commands one by one,

```bash
git clone https://github.com/kibwalid/AIUB-API.git
cd AIUB-API
.\env\Scripts\activate
pip install -r requirements.txt
python run.py
```
Make sure to have [Python3](https://www.python.org/downloads/release/python-383/) installed 

## Usage
For AIUB Notice send GET request to following path which expects a JSON request, 
```python
URI = "yourwebserver.com"
json_data = {"DATA": "all"} 
response = requests.get(URI + "website", json_data) # Returns all notice's Title and Links

# ------ #

link = "https://www.aiub.edu/holiday-due-to-eid-ul-azha-2020"
json_data = {"DATA": "one", "LINK": link} 
response = requests.get(URI + "website", json_data) # Returns title and data of the link
```
For AIUB Portal Send GET request to following path which expects a JSON request
```
URI = "yourwebserver.com"
json_data = {"ID": "", "PASS": "", "DATA": ""} # AIUB_ID, AIUB PASSWORD, Desired data from Portal
# Valid Parameters for Portal "DATA" key are, 
# "DATA": "courses" -> Returns All Courses and Results of taken ones. 
# "DATA": "cgpa" -> Returns total CGPA. 
# "DATA": "personal_data" -> Returns Personal Data of Student. 

response = requests.get(URI+ "portal", json_data) # Returns all notice's Title and Links
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Updates
This is still a WORK IN PROGRESS. If you have any suggestions or query please let me know. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
