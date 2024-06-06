from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from uuid import getnode as get_mac
import datetime
import os.path

mac = get_mac()
# calId = "baa41f255293072c05bd9b9e29e7206b59e2637f5cc4dabf7159297e15c9cdf0@group.calendar.google.com"
calId = "primary"

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly", "https://www.googleapis.com/auth/calendar", "https://www.googleapis.com/auth/calendar.events", "https://www.googleapis.com/auth/calendar.events.readonly", "https://www.googleapis.com/auth/calendar.readonly", "https://www.googleapis.com/auth/calendar.settings.readonly"]

creds = None
if os.path.exists(f"26801205048542token.json"):
    creds = Credentials.from_authorized_user_file(f"26801205048542token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
else:
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json", SCOPES
    )
    creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open(f"26801205048542token.json", "w") as token:
        token.write(creds.to_json())

def show():
    try:
        service = build("calendar", "v3", credentials=creds)
        now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
        print("Getting the upcoming 10 events")
        events_result = (
            service.events()
            .list(
                calendarId=calId,
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found.")
            return

        # Prints the start and name of the next 10 events
        Events = []
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            Events.append((start.split("T")[0], event["summary"],event["description"]))
            print((start.split("T")[0], event["summary"]), event["description"])
        return Events

    except HttpError as error:
        raise error

def updateCal(sub:str, topic:str, addn:str=None)->None:
    try:
        service = build("calendar", "v3", credentials=creds)
        due = datetime.datetime.now()+datetime.timedelta(days=7,hours=0,minutes=0) 
        due1 = datetime.datetime.now()+datetime.timedelta(days=14,hours=0,minutes=0) 
        due2 = datetime.datetime.now()+datetime.timedelta(days=21,hours=0,minutes=0) 
        
        end0 = due+datetime.timedelta(hours=2,minutes=0)
        end1 = due+datetime.timedelta(hours=2,minutes=0)
        end2 = due+datetime.timedelta(hours=2,minutes=0)
        # Define the details of the event
        event = {
            "summary": "1 "+ sub + ": "+ topic,
            'description': addn or "No remark",
            'start': {
                # 'dateTime': due.strftime(start) ,
                'date': due.strftime("%Y-%m-%d"),
                'timeZone': 'Asia/Kolkata'
                },
            # 'end': {'dateTime': end.isoformat()+"Z", 'timeZone': 'Asia/Kolkata'},
            'end':{
                # 'dateTime': due.strftime(start) ,
                'date': due.strftime("%Y-%m-%d"),
                'timeZone': 'Asia/Kolkata'
                },
            'reminders': {
                'useDefault': False,
                'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
                ]
            }
        }
        
        # Insert the event into the Google Calendar and execute the request
        created_event = service.events().insert(calendarId=calId, body=event).execute()
        event1 = {
            "summary": "2 "+ sub + ": "+ topic,
            'description': addn or "No remark",
            'start': {
                # 'dateTime': due.strftime(start) ,
                'date': due1.strftime("%Y-%m-%d"),
                'timeZone': 'Asia/Kolkata'
                },
            # 'end': {'dateTime': end.isoformat()+"Z", 'timeZone': 'Asia/Kolkata'},
            'end':{
                # 'dateTime': due.strftime(start) ,
                'date': due1.strftime("%Y-%m-%d"),
                'timeZone': 'Asia/Kolkata'
                },
            'reminders': {
                'useDefault': False,
                'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
                ]
            }
        }
        created_event1 = service.events().insert(calendarId=calId, body=event1).execute()
        event2 = {
            "summary": "3 "+ sub + ": "+ topic,
            'description': addn or "No remark",
            'start': {
                # 'dateTime': due.strftime(start) ,
                'date': due2.strftime("%Y-%m-%d"),
                'timeZone': 'Asia/Kolkata'
                },
            # 'end': {'dateTime': end.isoformat()+"Z", 'timeZone': 'Asia/Kolkata'},
            'end':{
                # 'dateTime': due.strftime(start) ,
                'date': due2.strftime("%Y-%m-%d"),
                'timeZone': 'Asia/Kolkata'
                },
            'reminders': {
                'useDefault': False,
                'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
                ]
            }
        }
        created_event2 = service.events().insert(calendarId=calId, body=event2).execute()
    # Handle HTTP errors
    except HttpError as error:
        print (f"An error occurred: {error}")
