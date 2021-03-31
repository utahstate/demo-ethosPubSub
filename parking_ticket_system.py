#
# Parking Ticket System - this code simulates a parking ticket system generating
# and posting parking tickets to Ethos Integration.
#
import random
import time
import string
import uuid
from ethos import Ethos

API_KEY = '2d7ef0f1-83d4-4e0f-b8ed-2c66122ebea9'

def main():
    print('Starting parking ticket system')

    ethos = Ethos(API_KEY)

    while True:
        t = generate_random_parking_ticket()

        print('Generated Parking Ticket for {first} {last}, Amount ${amount}, License Plate: {plate}'
            .format(first=t['firstName'],last=t['lastName'],amount=t['amount'],plate=t['licensePlate']))

        cn = convert_ticket_to_change_notification(t)
        print('Publishing change-notification')
        print(cn)
        ethos.send_change_notification(cn)

        wait_seconds = random.randint(1,20)
        print('\nWaiting for {seconds} seconds...\n'.format(seconds=wait_seconds))
        time.sleep(wait_seconds)

def generate_random_parking_ticket():
    ticket = {'parkingTicketId':'', 'firstName' : '', 'lastName': '', 'licensePlate': '', 'amount': 0}

    ticket['firstName'] = random.choice(['Billy','Joey','Jen','Taylor','Marissa','Clay','Chris','Nick','Keith','Wyatt','Christian','Priya'])
    ticket['lastName'] = random.choice(['Smith','Johnson','Williams','Brown','Jones','Miller','Davis','Garcia','Rodriguez','Wilson'])
    ticket['amount'] = random.choice([25,50,75,100])
    ticket['licensePlate'] = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
    ticket['parkingTicketId'] = str(uuid.uuid4())

    return ticket

def convert_ticket_to_change_notification(ticket):
    change_notification = { 'resource' : {'name':'', 'id':''},'operation': '','contentType':'','content': None}

    change_notification['operation'] = 'created'
    change_notification['contentType'] = 'resource-representation'
    change_notification['resource']['name'] = 'parking-tickets'
    change_notification['resource']['id'] = ticket['parkingTicketId']
    change_notification['content'] = ticket

    return change_notification

if __name__ == '__main__':
    main()
