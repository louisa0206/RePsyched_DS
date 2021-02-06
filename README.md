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


#### Recyclinghoefe
the Framework used for Web Scraping here is ***BeautifulSoup***

### Structure
Components of the Recyclinghoefe folder:
* *Recyclinghoefe_Locations.csv*
* *Recyclinghoefe_Locations.ipynb*

### How to run the code
* Open the file *Recyclinghoefe_Locations.ipynb*
* Click on "Raw" to see the code as a text in the json-format.
* Press ctrl+s to save it as a .ipynb file on your computer.
* Run the code in your preferred IDE. (Jupyter Notebook or VS Code were used by me)

### Done!
The Csv-File named *recyclinghoefe_locations.csv* is available now.
