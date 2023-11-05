import subprocess

def run_home():
    # Run home.py and capture its output in real-time
    process = subprocess.Popen(["python", "createGoals.py"], stdout=subprocess.PIPE, universal_newlines=True)

    for line in process.stdout:
        print(line, end="")  # Print the output of home.py
        if "True" in line:
            break

def run_schedule():
    # Run schedule.py
    subprocess.run(["python", "gameShop.py"])

if __name__ == "__main__":
    run_home()
    run_schedule()