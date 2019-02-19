# Log Analysis
**`newsdb.py`** is used to connect Postgres and run SQL queries.   
**`news.py`** contains the basic webpage interface that displays query results.

## How to run
Run following commands from terminal:    
`git clone git@github.com:ZoeVonFeng/FS_LogAnalysis.git`   
Go into directory that contains all files.  
If database is not setup yet, be aware that this application runs on linux with python3 and postgres. If you are not using Vagrant, make sure to run:   
`sudo -u postgres createdb news` before `psql -d news -f newsdata.sql`   

Finally, run:   
`python3 news.py`   

At last, open `localhost:8000` in your browser to view result.    

**P.S.**: *This applcation is designed on Debian without using Vagrant. Please make sure the `PORTNUM` is also applied on your own machine for postgre connection. In this case, `5433` is the postgres port number. *
