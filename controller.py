import subprocess

def run_mikesHouse():
    process = subprocess.Popen(["python", "mikesHouse.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)

    while True:
        line = process.stdout.readline().strip()

        if line == "createGoals":
            run_createGoals(process)
        elif line == "gameShop":
            run_gameShop(process)
        elif line == "schedule":
            run_NOTES(process)

def run_createGoals(process_mikesHouse):
    process = subprocess.Popen(["python", "createGoals.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)

    captured_line = None
    for line in process.stdout:
        print(line, end="")  # Print the output of home.py
        if "True" in line:
            captured_line = line
            process.terminate()  # Terminate home.py when "True" is printed
            break
    #data_from_createGoals = process_mikesHouse.stdout.readline().strip()
    

def run_gameShop(process_mikesHouse):
    process = subprocess.Popen(["python", "gameShop.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)

    captured_line = None
    for line in process.stdout:
        print(line, end="")  # Print the output of home.py
        if "True" in line:
            captured_line = line
            process.terminate()  # Terminate home.py when "True" is printed
            break

def run_NOTES(process_mikesHouse):
    process = subprocess.Popen(["python", "schedule.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)

    captured_line = None
    for line in process.stdout:
        print(line, end="")  # Print the output of home.py
        if "True" in line:
            captured_line = line
            process.terminate()  # Terminate home.py when "True" is printed
            break

if __name__ == "__main__":
    run_mikesHouse()
