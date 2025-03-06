# This Documentation is for the previous Version.
### I might rewrite the documentation for this version Late

##  Simple Jarvis Bot

+ This bot is Created using Python <br>
+ It can open Websites and Search for something in Google using voice command <br>
+ Can Open and Close applications<br>
+ Can also play music on YT <br>
+ After running the PY file , You need to say **"Jarvis"** to give it further commands


### Installation Process

+ First download and open the files into an IDE <br>
+ Now u just have to install the Required modules <br>
+ To do that , Open the Terminal and paste ```pip install -r requirement.txt``` <br>
+ Now run the ```main.py``` file and you are all set


### Commands it can support

- "**Open < app name > App**" for Opening Applicaion
- "**Close < app name >**" for Closing Applicaion
- "**Open < Website name >**" for opening Website
- "**Search < Query >**" for Searching the Query on Google
- "**Play < song name >**" for Playing song on YT (or anywhere else as specified by the dictionary)
- "**Deactivate**" For Deactivating Jarvis


### *dict_lib.py*
+ ```dict_lib.py``` file contains the links and locations of music ,websites and Applications
+ This bot can only access or open the Links or Application mentioned in this file.
+ ```music``` :- add music title and its link (title should be in lowercase)
+ ```open_applications``` :- add App name and its location (App name in lowercase)
+ ```close_applications``` :- add accordingly to ```open_applications```
+ ```websites``` :- websites name and link (Website name in lowercase)
