# RePsyched
***


## Glascontainer
### Structure
Inside the Glascontainer are some files
* the Glascontainer.csv: 
* the s
* the Framework used for Web Scraping here is ***Scrapy***

### Getting Started
#### Installing Scrapy
Install scrapy in an IDE (PyCharm was used here).

`pip install scrapy`


#### Starting a project
Start a Scrapy Porject.\
`scrapy startproject Glascontainer`
`cd` into the project folder.\
`cd Glascontainer`
#### Creating a Spider
Create a Spider.\
`scrapy genspider GlascontainerSpider berlin.de/ba-charlottenburg-wilmersdorf/verwaltung/aemter/umwelt-und-naturschutzamt/umweltschutz/altglascontainer`
#### Installing Packages
Install packages for the pipeline.\
```
pip install requests
pip install geopy
pip install google_trans_new
```
#### Copying the code
Open the directory *spiders* and copy the code the *GlascontainerSpider.py* into the created Spider in your IDE.
Open the *pipelines.py* file and copy the code into the pre-created pipelines.py in your IDE.
Open the *settings.py* file and copy the code into the pre-created settings.py in your IDE.

#### Running the Spider
Run the Spider in Scrapy.
`scrapy crawl GlascontainerSpider`
If it i not working, install the packages for the Pipeline 

#### Done!
The CSV-File is available.
