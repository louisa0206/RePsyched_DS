# Scrapy settings for Glascontainer project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Glascontainer'

SPIDER_MODULES = ['Glascontainer.spiders']
NEWSPIDER_MODULE = 'Glascontainer.spiders'

FEED_FORMAT='csv'
FEED_URI='Glascontainer.csv'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = { 'Glascontainer.pipelines.GlascontainerPipeline': 300,}

