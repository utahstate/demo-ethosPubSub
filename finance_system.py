#
# Finance System - this code simulates a finance system collecting parking tickets
#
import time
from ethos import Ethos

API_KEY = 'f34bc7c9-c52d-41e3-b6fe-44a6eaa5b0fc'

def main():
    print('Starting finance system')

    ethos = Ethos(API_KEY)

    while True:

        print('Checking for change notifications in Ethos Integration')
        data = ethos.get_change_notifications()

        if data and len(data) > 0:
            process_change_notifications(data)
        else:
            print('No change notifications available')

        wait_seconds = .5
        print('Waiting for {seconds} seconds...\n'.format(seconds=wait_seconds))
        time.sleep(wait_seconds)

def process_change_notifications(data):
    print('Received {count} change notifications'.format(count=len(data)))
    for d in data:
        #parking_ticket = d['content']
        print(d["id"])

if __name__ == '__main__':
    main()
