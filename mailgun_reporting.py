import json
import requests
import csv

YOUR_API_KEY="key-dde07bbe7f707b0182e2cda8709a283a"

def get_recepients(user_type):
    return requests.get(
        "https://api.mailgun.net/v3/browserstack.com/events",
        auth=("api", YOUR_API_KEY),
        params={
                "begin" : "Mon, 19 Dec 2016 00:00:00 GMT",
                # "end": "Mon, 19 Dec 2016 00:00:00 GMT",
                "ascending" : "yes",
                "pretty" : "yes",
                "tags" : "automate-purchase",
                "event" : user_type,
                })

def print_recepients(usr_typ):
    recepients = [];
    recepients_json = get_recepients(usr_typ)
    recepient_list = json.loads(recepients_json.text)
    for i in recepient_list['items']:
        recepients.append(i['recipient'])
    print(recepients)
    recepients_unique = set(recepients)
    print(recepients_unique)



print_recepients("delivered")
print_recepients("opened")



# myfile = open(recepients, 'wb')
# wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# wr.writerow(recepients_unique)    
# delivered_response = get_delivered()
# delivered_list = json.loads(delivered_response.text)










# opened_response = get_opened()
# opened_list = json.loads(opened_response.text)

# for j in opened_list['items']:
#     openers.append(j['recipient'])

# delivered_unique = set(openers)
# print(delivered_unique)

# recepients_file= open('delivered', 'w')
# recepients_file.write(recepients)
# recepients_file.close()

# openers_file = open('opened', 'w')
# openers_file.write(openers)
# openers_file.close()







