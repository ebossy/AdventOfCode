#powershell command to generate Files

#!!!!!!!!!!!!
#change these
#!!!!!!!!!!!!
year = 2024
day = 23

command = f'cd {year}; mkdir {day}; cd {day}; New-Item -Name "{day}-1.py" -ItemType File; New-Item -Name "{day}-2.py" -ItemType File; New-Item -Name "{day}-1.txt" -ItemType File; git add {day}-1.py {day}-2.py {day}-1.txt'
import subprocess
subprocess.run(["powershell", "-Command", command], check=True)

