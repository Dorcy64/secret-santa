import random
from data import participants
from whatsapp_selenium import send_messages
import time

Host_Name = 'Dorcy'


def generate_text(santa, santee, age):
    return f"""Dear {santa},\
\nThis year you are {santee}'s Secret Santa!. Ho Ho Ho!\
\nThis message was automagically generated from a computer by {Host_Name}\
\nNothing could possibly go wrong... Ho Ho Ho! ps {santee} is {age}.
"""


def generate_santas(participants_list):
    participant_choices = participants_list

    full_response = []

    for x in participants_list[::-1]:
        output = [x['phone']]

        stop = False
        timeout = 0
        while not stop:
            timeout += 1
            random_range = random.randrange(len(participant_choices))
            this_guy = participant_choices[random_range]
            if this_guy["id"] not in x["dont_pair"] and this_guy["id"] != x["id"]:
                output.append(generate_text(x['name'], this_guy['name'], this_guy['age']))
                stop = True
                participant_choices.pop(random_range)
            if timeout >= 61:
                raise ("Timeout error")
                break

        full_response.append(output)

    return full_response


santas_list = generate_santas(participants_list=participants)

time.sleep(2)
for santa in santas_list:
    send_messages(santa[0], santa[1])
