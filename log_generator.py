import random
import os
from datetime import datetime, timedelta

#Makes sure the log file is created and read in the correct directory

BASE_DIR = os.path.dirname(__file__)
log_path = os.path.join(BASE_DIR, "server.log")

#Creating the Content of Log Rows that will be used with the Random Module

log_levels = ["INFO", "WARNING", "ERROR"]

actions = [
    "User purchased item B",
    "Site Cannot Be Reached",
    "Disk Space Low",
    "File Uploaded",
    "Invalid Email"
]
users = [
    "john",
    "beatrice",
    "carter",
    "sandra",
    "lily"
]
ips = [
    "192.168.1.15",
    "244.202.179.109",
    "179.225.108.190",
    "34.112.126.126",
    "110.148.72.68",
    "102.126.187.229",
    "66.96.197.14"
]

#Creating and Writing Random Log File

def generate_logs():
    with open (log_path, "w") as log_file:
        for i in range (20):
            random_log_level = random.choice(log_levels) 
            random_action = random.choice(actions)
            random_ip = random.choice(ips)     
            random_user = random.choice(users)  
            
            # RANDOM TIME
            random_min = random.randint(0,5000)
            timestamp = datetime.now() - timedelta (minutes=random_min)

            # Formatted Date/Time

            formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")

            #BUILD LOG LINE
            log_line = (
                f"{formatted_time} |"
                f" User={random_user} |"
                f" IP={random_ip} |"
                f" {random_log_level} |"
                f" {random_action}"
            )

            #WRITE TO FILE
            log_file.write(log_line + '\n')



#Reading Log File and Counting Message Types

def analyze_logs():

    error_count = 0
    warning_count = 0
    info_count = 0

    with open (log_path, "r") as file:
        contents = file.readlines()

    for x in contents:

        if "ERROR" in x:
            error_count+=1
        if "WARNING" in x:
            warning_count+=1
        if "INFO" in x:
            info_count+=1
    
    return error_count, warning_count, info_count
    

#Print Summary

def print_summary(error_count, warning_count, info_count):
    print ("\n===== LOG SUMMARY =====")
    print ("Error Count: ", error_count)
    print ("Warning count: ", warning_count)
    print ("Info Count: ", info_count)


generate_logs()
error_count, warning_count, info_count = analyze_logs()
print_summary(error_count, warning_count, info_count)


