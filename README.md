# School Report Card Management System
Python built Software that generates a Report Card for a student in either pdf or docx or both formats.

## Technologies Used:
The project is created using :
* Python 3.9.1
* tkinter (for GUI Interface)

## Getting Started
Clone the repo on local machine:
```sh
$ git clone https://github.com/BasuDevTyagi10/SchoolReportCardGenerator.git
$ cd "virtual-keyboard"
```
### Create a virtual environment (for better control (version control) over the project)
It is better to use Anaconda Navigator ([Anaconda Documentation - Installation](https://docs.anaconda.com/anaconda/install/)) for handling such (and further mentioned) tasks of creating virtual environments, installing packages, IDEs, Applications, etc.
<br>
<br>For performing the mentioned operations manually (without Anaconda) :
<br><br>Install ```virtualenv``` module to create isolated virtual environments.
```sh
$ pip install virtualenv
```
To create a Virtual Environment for Python 2.x do the following
```sh
$ virtualenv myenv
```
For a Python 3 virtual environment type –
```sh
$ python3 -m venv myenv
```
To activate the virtual environment -
<br>On Windows, run:
```sh
$ myenv\Scripts\activate.bat
```

### Installing required packages
The required packages for this project are listed below to run the python scripts:
<br>```tkinter```, ```pandas```, ```docx-mailmerge```, ```docx2pdf``` and ```sqlite3```
<br><br>Install the above mentioned packages in your virtual environment using Anaconda, and without it by:
<br>_run the below command after you're in your virtual environment_
```sh
(myenv)$ pip install tkinter docx-mailmerge docx2pdf sqlite3
```

### Run the script:
(make sure youre in the home directory) run the following command -
```sh
(myenv)$ python main.py
```

## Project Overview
<b>MAIN SCRIPT:</b> main.py
<br><b>SCRIPTS FOR CODE DISTRIBUTION:</b> ```res.py``` (for common resources), ```dashboard.py``` (for dashboard UI  and functionality), ```login.py``` (for login UI and functionality), ```frontend.py``` (for main UI), ```backend.py``` (for main UI's backend to add, edit, delete and update data) and ```reportcard.py``` (for reportcard generation in pdf and docx format).
<br><b>DATABASE FILE:</b> ```database.db```
<br><b>ADDITIONAL FILES:</b>
<br>ReportCard Template - template.docx
<br>Image Resources - in ```/res``` directory

<br>Login Credentials and Passwords:
<br>Username: master
<br>Password: admin
<br>Password for editing template.docx: masteruser

## Documentations Refered:
The following documentations were refered to create this project :
* [Python 3.8.8](https://www.python.org/doc/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)

## Authors

-   **Basudev Tyagi** - _Initial work_ - [BasuDevTyagi10](https://github.com/BasuDevTyagi10)

