server ="https://api.pushbullet.com/v2/pushes"

import requests

token="o.8DEd2IH3vFcuUfmL3WvZ4z1YWdKPmovY"
header = {"Content-Type" : "application/json",
          "Access-Token" : "o.8DEd2IH3vFcuUfmL3WvZ4z1YWdKPmovY"}

data={"type" : "note",
      "title" : "python test",
      "body" : "hey this works"
     }

res = requests.post(url= server, json = data, headers = header)

print(res.content)
