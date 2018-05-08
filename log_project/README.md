# logs_report  
log_report.py is a Python program that utilizes the PostgresQL DB-API, _psycopg2_  
 to generate a data report. It provides the following queries generated from a  
 Udacity-provided database, _news_. The script must be run through the virtual  
  machine, VirtualBox, using Vagrant to install a Linux operating system.  

1. 3 Most Popular Articles
2. Authors Ordered by Views
3. Days that have more than 1.0% of views resulting in an error

## Installing VirtualBox  
Install from this [link](https://www.virtualbox.org/wiki/Downloads)

## Installing Vagrant  
Install from this [link](https://www.vagrantup.com/downloads.html)

## Running Vagrant  
Download the _vagrant_ configuration file from this [github repository](https://github.com/udacity/fullstack-nanodegree-vm)  
to the vagrant directory. To run vagrant, navigate to the vagrant directory where  
you installed vagrant using the Command Line Interface. Download and install the   
Linux OS with the command `vagrant up`. This will take several minutes. Then, log  
into the Linux OS with the command `vagrant ssh`. 

## Installing the _news_ Database  
Download the database from Udacity's Intro To Programming Nanodegree lesson [here](https://classroom.udacity.com/nanodegrees/nd000/parts/b910112d-b5c0-4bfe-adca-6425b137ed12/modules/a3a0987f-fc76-4d14-a759-b2652d06ab2b/lessons/0aa64f0e-30be-455e-a30d-4cae963f75ea/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91).  
If you do not have access, please reach out to the Udacity Support team and I am  
sure they will be happy to provide it for you. Place the .sql file you download  
in the vagrant directory after unzipping it. 

Start up Vagrant using the Running Vagrant instructions and navigate to the vagrant  
dirctory. Then run the command `psql -d news -f newdata.sql` to populate the environment  
with the _news_ database. 

## Creating Views  
The **logs_report.py** program requires several views to be created in the _news_ database.   

To create these views, first log in to the Vagrant VM and navigate to the **vagrant**  
directory. Then, run PostgresQL with the command `psql`. Connect to the _news_ database  
by entering `\c news`

In the _news_ database, enter the following queries:  
1. `CREATE VIEW errors AS`    
   `SELECT date_trunc('day',time) AS date, count(status) AS error_count`  
   `FROM log WHERE status='404 NOT FOUND'`  
   `GROUP BY date ORDER BY date ASC;`  
2. `CREATE VIEW daily_log AS`  
   `SELECT date_trunc('day',time) AS date, count(status) AS daily_views`  
   `FROM log`  
   `GROUP BY date ORDER BY date ASC;`  

## Running The Report   
Download and move **logs_report.py**, to the **vagrant** directory. You can exit psql by  
entering `\q`. From vagrant, run the command `python logs_report.py` and the report  
will generate. 