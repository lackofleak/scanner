import requests , urllib.request , os

def clearsc():
    "clear terminal screen"
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def subdomain_sc(domain , sub_list):
    "fnc for scan subdomains.."
    try :
        sub_list = open(sub_list).read()
        subdomains = sub_list.splitlines()
    except FileNotFoundError :
        print(f"No File Named [{sub_list}]")
        exit()
    for sub in subdomains:
        sub_domain = f"http://{sub}.{domain}" 
        try:
            requests.get(sub_domain)
        except requests.ConnectionError: 
            pass
        else:
            print("[FOUND] ",sub_domain)




def directory_sc(domain , dir_list):
    "fnc for scan directories.."
    try :
        dir_list = open(dir_list).read()
        dirs = dir_list.splitlines()
    except FileNotFoundError :
        print(f"No File Named [{dir_list}]")
        exit()

    for dir in dirs:
        dir_enum = f"http://{domain}/{dir}/" #.html"
        r = requests.get(dir_enum)
        if r.status_code==404: 
            pass
        else:
            print("[VALID DIR] " ,dir_enum)


    

banner ="""
 ==============================
| Domain & Directory Scanner  |
 ==============================
"""
if __name__ == "__main__":
    clearsc()
    print(banner)
    inpt1 = input("Choose An Item To Continue :\n[1].SubDomain Scanner\n[2].Directory Scanner\n[3].Exit\n")
    if inpt1 == "1":
        clearsc()
        print(banner)
        domain = input("Enter Your Domain :\n")
        sub_list = input("Enter Your word list File : \n")
        subdomain_sc(domain , sub_list)
    elif inpt1 == "2":
        clearsc()
        print(banner)
        domain = input("Enter Your Domain :\n")
        dir_list = input("Enter Your word list File : \n")
        directory_sc(domain , dir_list)
    else :
        clearsc()
        exit()
    