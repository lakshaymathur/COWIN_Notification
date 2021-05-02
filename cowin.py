import requests
import ast
import time
from datetime import datetime
from notify_run import Notify

date_range = ['01-05-2021','08-05-2021','15-05-2021','22-05-2021','29-05-2021'] #Range of dates you want to search
notify=Notify()
notify.register()
district_id = 188 # District id. Refer to DISTRICTS file.
polling_rate = 30


def make_request(date1):
    try:
        response = requests.get(
            'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict',
            params={'district_id': district_id, 'date':date1},
            headers={'Host': 'cdn-api.co-vin.in'},
            verify = False
        )
    
        crap = response.content.decode("UTF-8")
        data_t = ast.literal_eval(crap)
        data = data_t['centers']
        if(data):
            return data
    except:
        print("Unauthorized, trying again..")
    

def check_capacity(data):
    available_list=[]
    if(data):
        for centre in data:
            for session in centre['sessions']:
                tmp=dict()
                if session['available_capacity'] != 0:
                    print("Found!!!!!")
                    tmp['name'] = centre['name']
                    tmp['date'] = session['date']
                    tmp['available capacity'] = session['available_capacity']
                    print(centre['name'])
                    print(session['date'])
                    print(session['available_capacity'])
                if len(tmp) > 0:
                    available_list.append(tmp)
    return available_list



def find_me_vaccine():
    notification_list = []
    for i in date_range:
        notification_list = notification_list + check_capacity(make_request(i))
    if len(notification_list) > 0:
        text = str(notification_list)
        notify.send(text) # Uses notify.run service to hit endpoint which broadcasts message

            

def main():
    requests.packages.urllib3.disable_warnings()  # To supress SSL cert verification warning
    while(1):
        print(datetime.now().strftime("%H:%M:%S") + ' :: '+ "Checking Now...") # Prints on Console
        find_me_vaccine()
        time.sleep(polling_rate) 


if __name__ == "__main__":
    main()
    
