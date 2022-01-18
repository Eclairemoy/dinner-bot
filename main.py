import os
import requests
from datetime import datetime
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')

# the phone number of the person who is organizing the meal
organizers_phone_num='+XXXXXXXXXXX'

# the list of numbers of the family members 
family_nums = ['+XXXXXXXXXXX', '+XXXXXXXXXXX']

account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
messaging_service_sid= os.environ.get('MESSAGING_SERVICE_SID')
client = Client(account_sid, auth_token)

@app.route('/schd-msg', methods=['POST'])
def schedule_msg():
    '''
    A function that schedules an outgoing message to the organizer phone number
    '''
    #note that you have to schedule >=60 min from current time and < 7 days out
    message = client.messages \
        .create(
            messaging_service_sid=messaging_service_sid,
            body='what would you like for dinner?',
            # format is year, month, day, hour, minute
            send_at=datetime(2022, 1, 18, 17),
            schedule_type='fixed',
            to=organizers_phone_num
        )

    print(message.sid)
    return message.sid

@app.route('/send-rec', methods=['POST'])
def send_rec():
    """
    a function that responds with the SMS message to the family members
    """
    # get the string of what the person messaged in and cast it to lowercase
    incoming_msg = request.values.get('Body', 'message error').lower()
    sender_phone_number = request.values.get('From', 'unknown_sender')
    
    # reset session (helpful to use for testing, would need to set it to some sort of auto refresh)
    if 'reset' in incoming_msg:
        del session['sms_count']
        session.pop(sender_phone_number, None)
        sms_message = "resetting your session"
        resp = MessagingResponse()
        msg = resp.message()
        msg.body(sms_message)
        return str(resp)
        
    if not 'sms_count' in session:
        session['sms_count'] = 0
        
    sms_count = session['sms_count']
    
    if sms_count == 0:
        # if it's the first time someone is messaging this number then it will be the meal organizer
        # we want the meal organizer to send their options in as a comma separated list

        # send a message to the organizer as a confirmation
        sms_message = "Thanks for these options. We'll let you know what the family says."

    else:
        try:
            # respond to the sender with what they chose as a confirmation


        except:
            # if they send in a response that doesn't match any of the options ask them to try again


    session['sms_count'] += 1
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(sms_message)

    return str(resp)

def message_organizer(phone_number, selection):
    '''
    a function that messages the organizer to let them know the family votes
    '''
