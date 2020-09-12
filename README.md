<p align="center">
<img src="static\download.png" width="200" alt="Logo">
  <h3 align="center"></h3>
  <p align="center">
  Recruiting candidates to fit a particular job profile is a task crucial to most of the companies, In this era of technology, job searching has become smarter and more accessible at the same time. There have been lots of work done for the job searching process. Whereas, the process of selecting a candidate based on their resume has not been entirely automated.
    <br/>
    <br />
    We have used the state-of-the-art Natural Language Processing Model for data processing and feature extraction (Spacy) thus enabling us to deliver the automated work flow system for recruitors for effective time management and increase in efficiency
    <br>
    <br>
  </p>
</p>

## Abstract

To achieve the desired goal, the entire process has been divided into three segments. The first segment consists of converting the unstructured resumes in structured data using NLP, and the second segment consists of the extraction phase, where the relevant information is extracted from the resume and giving them an identifier value. Finally, based on the values assigned, the resumes are ranked accordingly in the final segment.

## Overview

**a)** **The NLP algorithm uses a pre-defined terminology** of keywords such as “AI developer”, “Keras” or “TensorFlow” to parse the resumes.

**b)** The system then **extracts the features, stores them on json config file** for easier data management system.Now We then extract the necessary data elements from the json config files and **then pipeline them to the dashboard in realtime**

**c)** The end result is **an automated profile analyser system that can analyze complex resumes and categorize relevant candidates** based on specified profile keywords. The integration of AI with ATS accelerates the recruitment process and performance without compromising with the quality of hire.

**d)** We integrated the model to our dashboard which adds on few features like,
* Dashboad View -- Monitors the employee status 
* Hiring View -- loads up the resumes for easier reference for the recruitors
* User Management View -- To manage the system board.
* Resume Analyser View -- Triggers the dump of emails from the system and starts the model processing.
* Notifications are also added for meeting schedule.

**e)** **Mail Management System** enables the model to automatically fetch the resumes from the mail system and also enables the user to send out emails for Interview.

## Folder Structure
  ```bash
  Recruitem Dashboard/
  │
  |── Extras - Contains log file and hashed password for the mail system.
|     ├── logfile.txt - manages all the logs for the system operation
  |     └── pas.1 - hashed password for the mailing system.
  |
 |── json_files - holds the extracted features from the resumes.
 |── Static - contains the images for the html page.
 |
 |── Templatesconsists of templates that are being render by the flask engine.
  |   ├── dash_board.html hold all the elements of the dashboard page
 |   └── new_index.html Login page
 |
  ├── app.py - main script to run the flask Module
  |
  ├── attachment.py - Downloads the email from the HR system.
  ├── model.py - NLP model file to extract features from the pdf to json configs 
  ├── data_loader.py - creates a sqlite engine and updates all the features from the json file
  |── dashboard.py - Runs the db operations for the entire system
  |
  │── mail.py - Manages the mailing system
  ├── clock.py - Runs the automated scheduler on Heroku Cloud engine
  │── extra.py - Manages the log file ownership
  │──log_load.py -- automated process to trigger the model.py
  |
  |
  |── nltk.txt - Nlp module for the heroku cloud
  └── ProcFile - Heroku deployment file
  ```

## Requirements
* pyresparser==1.0.6
* Flask-Markdown
* imbox==0.9.8
* Flask==1.1.2
* spacy==2.3.1
* APScheduler==3.0.0
* gunicorn
* [Spacy](https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz)

### Contributors

- [Divakar R](https://github.com/rexdivakar)
- [Aakash](https://github.com/aakash-cse)

## Licence

[GNU General Public License v3.0](license.txt)

## Documentation 

## [PPT]()
