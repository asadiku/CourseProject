# CourseProject

 1) Overview:  
For our project, we decided to choose the Intelligent Browsing topic because we wanted to provide additional functionality on top of existing web browsers. In particular, we wanted to build a Chrome extension for linking user queries to Coursera video segments. This is a problem currently because Coursera only allows you to search for exact terms when looking for a particular topic video. However, we would like to improve this by using the BM25 retrieval function on transcript data to allow for more complex searches. Instead of looking for exact search results, our extension would look at all the possible video segments (of CS410 lecture videos) and rank them in order of relevance based on the BM25 retrieval function. Then, we would show the user the most relevant video segments based on their query. 
 2) How it is implemented:  
The main components of this project are a chrome extension and a backend flask server which runs our python function.  
In the ChromeExtensionJS folder, this contains the relevant front end code in the popup.html file.  
Also in that folder, there is the popup.js, which is important as it is the one which calls the backend API implementation of the BM25 function.  
In the flask app folder, that contains the server code of our project as well as the python implementation of the BM25 function which utilizes metapy.  
To modify how the search function works/extend it, you would look at changing the server.py file.  
You could also create more endpoints/methods in search_server.py  
The other folders are no longer used but were used to scrape the coursera data we needed and initial creation of the python function.  
 3) How to install and run (Also explained in the demo video https://youtu.be/9LsBYPtbf1s):  
Clone this repository  
Set up anaconda/other environment:  
conda create --name testenv python=3.5 
proceed ([y]/n)?  
y  
conda activate testenv
Move to flaskApp folder  
Pip install -r requirements.txt  
Load the ChromeExtensionJS folder as unpacked into the chrome extension developer area  
Move to flaskApp, start up server  
python search_server.py config.toml  
  4) Contributions:  
  Albert Sadiku, scraped the data from coursera and implemented the BM25 function we used  
  Matthew Tang, created the front end/backend server which takes the implementation and runs it.  
