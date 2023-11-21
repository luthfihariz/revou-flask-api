from flask import Blueprint
from datetime import datetime, timedelta
from event.constants import EVENT_DATE_FORMAT

event_blueprint = Blueprint("event", __name__)

events = [{'name': 'Lecture 1 Flask Fundamentals', 'start_date': datetime(2023, 11, 21, 19, 10, 0)}]

@event_blueprint.route("", methods=["GET"])
def get_event_list():
    new_events = []
    for event in events:
        new_events.append({
            'name': event['name'],
            'start_date': datetime.strftime(event['start_date'], EVENT_DATE_FORMAT)
        })


    return list(map(lambda event: 
                    {'name': event['name'], 'start_date': datetime.strftime(event['start_date'], EVENT_DATE_FORMAT)}, 
                    events))