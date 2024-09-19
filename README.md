# PL-2024-25-Season
This is my first end-to-end data engineering project on English Premier League data for the season 2024/2025.
The project is a sports analytics data pipeline that scrapes the data from several website links, transforms the data and loads the data into cloud storage and a PostgreSQL database every Saturday and Sunday until the end of the season.

Detailed Overview:
1. I inspected the websites from which I was to extract the data and chose BeautifulSoup to scrape the data since they were all static websites.
2. Built my web scraping script to get and transform the data.
3. Provisioned a blob storage container on Azure and uploaded my extracted data as a Parquet file.
4. Provisioned a PostgreSQL database on Azure and uploaded my extracted data to it.
5. Automated this whole process using GitHub Actions and scheduled it to run every Saturday and Sunday until the end of the season.
