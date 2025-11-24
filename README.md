A simple and interactive command-line To-Do List application built using Python.
This project helps users manage daily tasks efficiently with features like task priorities, motivational messages, achievements, and automatic data saving.

 Features:
•	Add tasks with priority levels (High/Medium/Low)
•	Remove tasks by task number or name
•	View tasks sorted by priority
•	Automatic timestamp for each created task
•	Motivational quotes for encouragement
•	Achievement badges based on completed tasks
•	Data stored in JSON file (persistent storage)
•	Lightweight and runs entirely in terminal

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


Project Structure

 todo-list-project
│── todo.py           
│── PROJECT REPORT.pdf        
│── README.md

 Functions Overview
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

Modules used : random ,json,os,datetime time (Built in modules)

Future Enhancements : GUI-based interface
Deadline & reminder feature
Categorized task groups
Export tasks to CSV/Excel
User login system
