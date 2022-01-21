<p><img src="https://cdnnmundo1.img.sputniknews.com/img/07e5/02/12/1107933201_0:63:3073:1791_1920x0_80_0_0_4b7250bab9fa7d347757b14d5b73fa7d.jpg"></p>


### :raising_hand: **Hello and welcome to ASK SPORTY AYUSO** 
ASK SPORTY AYUSO aims to bring closer the passion for sports of our leader, Isabel Diaz Ayuso, to all citizens of the world living (of course) in Madrid.  
ASK AYUSO can grant you one of these three wishes:
1) Tell you ALL sport centers in Madrid with their closest Bicimad station 
2) Tell you for ONE sport center the closest Bicimad station 
3) Decide for you if you should do today sport or not (recommended option)

### :see_no_evil: **From an Isabel fan to the world**
This project is just the first draft done by a humble Isabel lover doing its first repository and project in Ironhack.

### :running: **How to ASK SPORTY AYUSO**
ASK SPORTY AYUSO 

With `--t`, Sporty Ayuso will tell you ALL sport centers in Madrid with their closest Bicimad station
With `--u`, Sporty Ayuso will tell ONE sport center the closest Bicimad station

### :computer: **Technology stack**
The main technologies used here are python and pandas (beginner level) 
And he libraries used are: 
- pandas
- request
- re
- Point from shapely.geometry
- geopandas


### :boom: **Core technical concepts and inspiration**
In order to not to make Ayuso lovers wait too much for their information, the acquisition and analysis of the information is done in advance with the file "Ayuso_updates.py". 
When executing "Ayuso_updates.py". file, the information from Madrid sport centers is read and updated from the REST API from the Open Data Portal of the Madrid City Council. 
When executing "Ask_Sporty_Ayuso".py it only asks the Ayuso lovers what information they would like to receive and therefore, the time it takes to respond reduces from more than 10s to less than 3s. 

### :wrench: **Configuration**
We recomend having the latest version of python for executing ASK SPORTY AYUSO. 

### :see_no_evil: **Please NOTE**
Please note that Bicimad information is read from a csv file that was downloaded in January 2022. Therefore, changes since this date are not covered. 

### :file_folder: **Folder structure**
```
└── project
    ├── main.py
    ├── main2.py
    ├── .gitignore
    ├── README.md
    ├── main_script.py
    ├── notebooks
    │   ├── notebook1.ipynb
    │   └── notebook2.ipynb
    ├── p_acquisition
    │   ├── acquisition.py
    ├── p_wrangling
    │   ├── wrangling.py
    └── data
        ├── bicimad_stations.csv
        ├── bicipark_stations.csv
        └── bicimad_sport_center_disntance.csv
```


### :love_letter: **Last thougts: **
I hope that this silly program will make you laugh :D

---