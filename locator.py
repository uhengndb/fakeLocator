#! /usr/bin/python3
import json
import os
from sys import argv
from time import sleep
import requests

# load module file first
module_file = open("modules.json", "r")
jd = json.load(module_file)
module_file.close()

#check internet
def checkInternet():
    try:
        r = requests.get("http://google.com")
    except Exception:
        print("\33[1;91m[*] No internet access.\33[0m")
        exit()
# banner here
def banner():
    os.system('clear')
    print("""
\33[1;94m===================================\33[0m
\33[1;93m   ++++  User Locator  ++++\33[0m
\33[1;94m===================================\33[0m
    """)
    sleep(0.5)
banner()
# usages here
def usages():
    print("""\n      \33[1;94m+=+=+=+=+=+=+= \33[1;93mHELP \33[1;94m+=+=+=+=+=+=+=\33[0m
            
\33[1;92m[ Basic ]\33[0m
        \33[1;93mlocater    \33[1;94m:  To simply run the script\33[0m\n   
\33[1;92m[ Arguments ]\33[0m
        \33[1;93m--show-module   \33[1;94m:   Show all available modules\33[0m
        \33[1;93m--add-module    \33[1;94m:   Add new module\33[0m
    """)
    exit()
# show all availabel module function here
def show_module():
    print("\n\33[1;92m[*] Loading avilable module ...\33[0m\n")
    sleep(1)
    c = 1
    for i in jd:
        print(f"\33[1;94m[{c}] \33[1;95m{i}       \33[1;90m{jd[i]['site']}         \33[1;93m{jd[i]['discription']}\33[0m")
        sleep(0.01)
        c += 1
# add new module
def add_module():
    print("\33[1;92m[*] Checking Modules...\n")
    sleep(0.5)
    module_name = input("\33[1;94m>>> \33[1;92m[\33[1;93m NEW \33[1;92m] \33[1;94mEnter new module name : \33[1;92m")
    metadata = input("\33[1;94m>>> \33[1;92m[\33[1;93m NEW \33[1;92m] \33[1;94mEnter new module metadata : \33[1;92m")
    redirection_url = input("\33[1;94m>>> \33[1;92m[\33[1;93m NEW \33[1;92m] \33[1;94mEnter new module redirection url : \33[1;92m")
    title = input("\33[1;94m>>> \33[1;92m[\33[1;93m NEW \33[1;92m] \33[1;94mEnter new module title [Webpages title] : \33[1;92m")
    discription = input("\33[1;94m>>> \33[1;92m[\33[1;93m NEW \33[1;92m] \33[1;94mEnter new module discription : \33[1;92m")
    try:
        json_file = open("modules.json", "w")
        json_file.write("{\n")
        for i in jd:
            json_file.write('   "'+str(i)+'":{\n')
            json_file.write(f"""     "metadata" : "{jd[i]['metadata']}",\n """)
            json_file.write(f"""     "site" : "{jd[i]['site']}",\n """)
            json_file.write(f"""     "title" : "{jd[i]['title']}"\n """)
            json_file.write(f"""     "discription" : "{jd[i]['discription']}"\n """)
            json_file.write('   },\n')

        json_file.write('   "' + str(module_name) + '":{\n')
        json_file.write(f"""     "metadata" : "{metadata}",\n """)
        json_file.write(f"""     "site" : "{redirection_url}",\n """)
        json_file.write(f"""     "title" : "{title}",\n """)
        json_file.write(f"""     "discription" : "{discription}"\n """)
        json_file.write('   }\n')
        json_file.write("}")
        json_file.close()
    except Exception as e:
        print("\33[1;91m[*] An error occured during saving new module\33[0m")
        exit()
    print(f"\33[1;93m[*] New Module {module_name} Saved successfully.\33[0m")
# module selection here
def locate():
    checkInternet()
    print("\33[1;92m[*] Show help if you need module name.\33[0m\n")
    module_list = []
    for i in jd:
        module_list.append(i)
    #ask for module
    module = input("\33[1;94m>>>\33[1;92m[\33[1;93m module \33[1;92m] \33[1;94mEnter module name : \33[1;92m")
    if(module in module_list):
        print("\33[1;94m[*] Module Founded.\33[0m")
        # writing to index.php file
        index_file = open("index.php", "w")
        with open("data/1.data", 'r') as data1:
            data_one = data1.read()
        with open("data/2.data", 'r') as data2:
            data_two = data2.read()
        with open("data/3.data", 'r') as data3:
            data_three = data3.read()
        for i in jd:
            if(i == module):
                url = jd[i]['site']
                metadata = jd[i]['metadata']
                title = jd[i]['title']
        index_file.write(f"<html>\n<head>\n<title>{title}</title>\n{metadata}\n")
        index_file.write(f"{data_one}")
        index_file.write(f"You will simply redirecting to {url} ...\n")
        index_file.write(f"{data_two}")
        index_file.write(f"window.location.href = 'http://{url}'\n")
        index_file.write(f"{data_three}")
        index_file.close()

    else:
        print("\33[1;91m[*] Module not found.\33[0m")
        exit()
    # lounch main shell script
    os.system("bash main.sh")

if(len(argv) == 1):
    locate()
else:
    if(len(argv) > 2):
        print("\33[1;91m[*] Invaild argument.\33[0m")
        usages()
    elif(len(argv)== 2):
        if(argv[1] == "--show-module"):
            show_module()
        elif(argv[1] == "--add-module"):
            add_module()
        elif(argv[1] == '-h' or argv[1] == '--help'):
            usages()
        else:
            print("\33[1;91m[*] Invaild argument.\33[0m")
            usages()
    else:
        print("\33[1;91m[*] Invaild argument.\33[0m")
        usages()
