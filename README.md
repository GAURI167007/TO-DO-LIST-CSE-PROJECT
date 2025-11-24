TO-DO LIST: 

A simple and interactive command-line To-Do List application built using Python.
This project helps users manage daily tasks efficiently with features like task priorities, motivational messages, achievements, and automatic data saving.

 Features:	Add tasks with priority levels (High/Medium/Low)
•	Remove tasks by task number or name
•	View tasks sorted by priority
•	Automatic timestamp for each created task
•	Motivational quotes for encouragement
•	Achievement badges based on completed tasks
•	Data stored in JSON file (persistent storage)
•	Lightweight and runs entirely in terminal

Testing Approach
Unit Testing: Each function tested individually to ensure correct behavior.
Integration Testing: Checked the complete workflow from adding to removing tasks.
Boundary Testing: Tested empty lists, invalid inputs, and non-existent tasks.
Randomness Testing: Verified motivational messages and task suggestions appear correctly.

TECHNOLOGIES USED :
1. PYTHON
2. LIBRARIES : JSON,Datetime,os
3. Environment : VS CODE INSIDERS

 Modules Used       Module	Purpose


random	            Display motivational quotes, random suggestion

time	              Provide small delays for better UX

datetime	          Add timestamps for tasks
json	              Save & load tasks (persistent storage)

os	                Clear console and check file existence

	
	
How to Run the Project:
1. Install Python (3.10+ recommended)
2. Open the folder in VS Code or terminal
3. Run the script:
python todo.py

Project Structure:
 todo-list-project
│── todo.py           
│── PROJECT REPORT.pdf        
│── README.md

 Functions Overview:
1. addtask()
Takes user input
Validates priority
Saves task with timestamp
Writes to JSON file

3. removetask()
Remove by number or name
Updates completed count
Saves updated list

4. viewtasks()
Sorts tasks by priority
Shows count + a suggested task

5. showyourachievement()
Awards badges: Master the task,Rising Prodigy, Beginner

 Objective:To help users organize and track tasks effectively through an easy-to-use Python CLI system that encourages productivity and motivation.
 
 Future Enhancements : Implement persistent storage (file/database) to save tasks permanently.
Develop a GUI version using Tkinter or PyQt.
Add reminders or notifications for pending tasks.
Enable task categories or tags for better organization.
Integrate analytics or dashboard to track completed tasks over time.
Integrate with calendar apps or email notifications.
 
Screenshots are as follows:
<img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/bd1d373d-c841-4b82-bd1d-510245b5bc57" />
<img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/4a5ed695-e4d7-47a6-819a-5bfdf1c24613" />
<img width="2000" height="1141" alt="image" src="https://github.com/user-attachments/assets/78efa48b-ebe4-4813-b444-740c439ff721" />
<img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/2e536150-781d-4f9b-9c1e-a1f87466b2d6" />
<img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/09a464de-62a2-424d-9570-70f87fa1c7ec" />





