import requests

message = {"user": "britney",
           "message": "HI!!!"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                  json=message)

print(r)
print(r.text)

r= requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/scoutmeister")
print(r.text)

# output_info = {"name": "Scout Rice",
#                "net_id": "asr43",
#                "e-mail": "ainsley.rice@duke.edu"}

# r = requests.post("http://vcm-21170.vm.duke.edu:5000/student",
#                   json=output_info)
# print(r)
# print(r.text)

# r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
# print(r.text)

# r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
# print(r)
# print(type(r)) # r printed 'Response, [200]'. The 200 is the status code that will
#                 # tell you if its a good request or not. status codes defined by industry. 200 = "OK". 404 = "Not Found"
# print(r.text)
# print(r.status_code)
# if r.status_code == 200:
#     answer = r.json() # if string is json encoded, will put into variable matching python data type
#     print(type(answer))
#     for branch in answer: # answer is now a list, so can iterate through it 
#         print(branch["name"])
# else: 
#     print("Bad request: {}".format(r.text))

