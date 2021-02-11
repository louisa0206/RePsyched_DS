# RePsyched
***

## Glascontainer
the Framework used for Web Scraping here is ***Scrapy***

### Structure
Components of the Glascontainer folder
* *Glascontainer.csv*
* *settings.py* 
* *pipelines.py*
* *GlascontainerSpider.py*

### Getting Started
#### Installing Scrapy
Install scrapy in an IDE (PyCharm was used here).
```
pip install scrapy
```
#### Starting a project
Start a Scrapy Porject.
```
scrapy startproject Glascontainer
```
`cd` into the project folder.
```
cd Glascontainer
```
#### Creating a Spider
Create a Spider.
```
scrapy genspider GlascontainerSpider berlin.de/ba-charlottenburg-wilmersdorf/verwaltung/aemter/umwelt-und-naturschutzamt/umweltschutz/altglascontainer
```
#### Installing Packages
Install packages for the pipeline.
```
pip install requests
pip install geopy
pip install google_trans_new
```
#### Copying the code
Open the *GlascontainerSpider.py* and copy the code into the created Spider in your IDE.\
Open the *pipelines.py* file and copy the code into the pre-created pipelines.py in your IDE.\
Open the *settings.py* file and copy the code into the pre-created settings.py in your IDE.

#### Running the Spider
Run the Spider in Scrapy.
```
scrapy crawl GlascontainerSpider
```
#### Done!
The Code need some time to run.\
The CSV-File is available.





## Recyclinghoefe
the Framework used for Web Scraping here is ***BeautifulSoup***

#### Structure
Components of the Recyclinghoefe folder:
* *Recyclinghoefe_Locations.csv*
* *Recyclinghoefe_Locations.ipynb*

#### How to run the code
* The Code to scrape the website that contains the location of all Recyclinghoefe in Berlin can be found in the notebook *Recyclinghoefe_Locations.ipynb*
* Clone the repository to run it on your local computer

#### Done!
The Csv-File named *recyclinghoefe_locations.csv* is available now.




## Waste Categories
for the purpose of scraping, ***BeautifulSoup*** has been used.

#### Components/Files
There are two files in wasteinfo folder:
* *wasteinfo_BSR.csv*
* *wasteinfoscrapping_BSR.ipynb*

#### How to run the code
* Information regarding the different categories of waste has been extracted using BSR website and can be found in a jupiternotebook file *wasteinfoscrapping_BSR.ipynb*
* Clone the repository to run it on your local computer

#### Done!
The Csv-File named *wasteinfoscrapping_BSR.csv* is available now.

***
See https://github.com/users/louisa0206/projects/1 for the complete RePsyched Project\
Link to the main Repository: https://github.com/louisa0206/RePsyched.git \
Link to the Web Development Repository: https://github.com/leagruen/WebDev.git
