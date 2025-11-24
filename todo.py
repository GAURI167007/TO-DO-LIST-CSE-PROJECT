import random
import time
import os
import json
import datetime

if os.path.exists("tasks.json"):
    with open("tasks.json","r") as file:
        lists=json.load(file)
else:
    lists=[]
completedcount=0
quotes=[
    "Keep going, you're doing great!",
    "One step at a time ",
    "Tasks today, success tomorrow",
    "Tasks today, success tomorrow",
    "Almost there,don't give up"
]
def achieve(count):
    if count>=8:
        return "MASTER THE TASK"
    elif count>=4:
        return "Rising prodigy"
    elif count>=1:
        return "Beginner"
    else:
        return None
def addtask():
    task = input("ADD THE TASK YOU WANT TO COMPLETE:").strip()
    if not task :
            print("TASK CANNOT BE EMPTY!")
            return
    priority = input("SET THE PRIORITY: ").strip().capitalize()
    if priority not in ["High","Medium","Low"]:
            priority="Medium"
    
    createdat=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    tassks ={"name":task,"priority":priority}
    lists.append(tassks)
    print("YAY!! The task has been added successfully!!!!")
    print(random.choice(quotes))

        
def removetask():
        global completedcount
        os.system("clls" if os.name=="NT" else "CLEAR")
        if not lists:
            print("OOPS!WE DON'T HAVE ANYTHING TO REMOVE")
            return
        viewtasks()
        tasksinput=input("enter the task you are done with please:").strip()
        
        if tasksinput.isdigit():
            index=int(tasksinput)-1
            if 0<+index<len(lists):
                remove = lists.pop(index)
                completedcount+=1
                print("DONE!!THE TASK" + remove + " HAS BEEN REMOVED..")
            else:
                print("SUCH TASK NUMBER NOT FOUND")
        else:
            found=False
            for task in lists:
                if task["name"] == tasksinput:
                    lists.remove(task)
                    completedcount+=1
                    print(f"DONE!! WE HAVE REMOVED THE TASK YOU WANTED TO REMOVE i.e {tasksinput}")
                    found=True
                    break
                if not found:
                    print("ALAS!! NO SUCH TASK HAS BEEN FOUND")
def viewtasks():
    if lists:
        priority={"high":1,"medium":2,"low":3}
        sortedtasks=sorted(lists,key=lambda x: priority[x["priority"].lower()])
        print("THE FOLLOWING ARE THE TASKS TO BE COMPLETED :")  
        for i,task in enumerate (sortedtasks,start=1):
                print(f"{i}. {task['name']} -Priority: {task['priority']}")
        print("YOU HAVE" + str(len(lists)) + "tasks left")
        if sortedtasks:
            suggesting = random.choice(sortedtasks)
            print("SUGGESTION FOR YOU: " + suggesting["name"] + " - Priority: " + suggesting["priority"])   
        else:
            print("All is complete!!")

def showyourachievement():
            badge=achieve(completedcount)
            if badge:
                print("YOUR ACHIEVEMENT BADGE IS :" + badge)
            else:
               print("No achievemnt. YOU CAN DO ITTT!!")

while True:
         print("MENU")
         print("1.ADD A TASK")
         print("2.REMOVE A TASK")
         print("3.VIEW TASKS")
         print("4.YOUR ACHIEVEMENT")
         print("5.EXIT")

         try:
            choice = input("ENTER YOUR CHOICE (1-5): ").strip()
            if choice =="1":
                addtask()
            elif choice =="2":
                removetask()
            elif choice =="3":
                viewtasks()
            elif choice =="4":
                showyourachievement()
            elif choice =="5":
                print("Thank you for using this app, hope we created some changes in your life")
                showyourachievement()
                break
            else:
                print("NOO!!Invalid choice :( ")
         except ValueError:
             print("DONT ENTER INVALID INPUTS")

         time.sleep(1)
