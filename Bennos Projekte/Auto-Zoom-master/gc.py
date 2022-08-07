from icalendar import *
import requests
from datetime import datetime, date, timezone, timedelta, time
import pytz
import time as t
import Auto
import threading
import winsound


class EVENT:
    def __init__(self):
        self.name = None
        self.start = None
        self.end = None

    def set_name(self, name):
        self.name = name

    def set_start(self, start):
        self.start = start

    def set_end(self, end):
        self.end = end

    def get_name(self):
        return self.name

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end


class ZMT:
    def __init__(self, name, id, pw, link=None):
        self.name = name
        self.id = id
        self.pw = pw
        self.link = link


active = False
url = "http://digicampus.uni-augsburg.de/dispatch.php/ical/index/YQYWvmN8"
events = []
meetings = [
    ZMT("Diskuusion zu Vorlesung, Numerische Verfahren", None, None, link="https://uni-augsburg.zoom.us/j/92384192432?pwd=Z0czWnlybWdHQ2VIYXpmRUpGU3VDdz09"),
    ZMT("Praktikum Mess- und Regelungstechnik", None, None, link="https://uni-augsburg.zoom.us/j/95193816917?pwd=N0R5cWNzZFdkY0hUdGJRNmd1d21hUT09"),
    ZMT("Praktikum für Produktionstechnik", None, None, "https://uni-augsburg.zoom.us/j/95352087019?pwd=dTFNQ21qcFh4VkhVcHVkL3I5R25PQT09"),
    ZMT("Systemnahe Informatik", None, None, link="https://uni-augsburg.zoom.us/j/95120172814?pwd=bUFVTlc5RFpIOGE1bjlDbWs1T25yZz09"),
    ZMT("Vorlesung, Modellierung informationstechnischer Systeme", None, None, link="https://uni-augsburg.zoom.us/j/91527370995?pwd=NmdaS0xTVTduWklvTHo0SytqY09OUT09"),
    ZMT("Übung, Modellierung informationstechnischer Systeme", None, None, link="https://uni-augsburg.zoom.us/j/99404611629?pwd=WnVJcloxUXEyWDV3ZHh6Y1NjUDNMZz09"),
    ZMT("Ü-SNI", None, None, link="https://uni-augsburg.zoom.us/j/92814142816?pwd=TmxNN2dmQ2N4OVdpUEhITHBLeWQ2dz09")
]

def load():
    today = datetime.utcnow().replace(tzinfo=pytz.utc)
    calendar = Calendar.from_ical(requests.get(url).content)
    for component in calendar.walk():
        if component.name == "VEVENT":
            name = component.get('summary')
            start = component['DTSTART'].dt
            end = component['DTEND'].dt
            print("Event:")
            print(name)
            print(start)
            print(end)
            print(today - start)
            print()
            now = (today.hour + 1)*60*60 + today.minute*60 + today.second
            delta = today - start
            secs = -(delta.seconds + delta.days*86400)
            print(secs, now, 86400 - now)
            if (secs <= 86400 - now and secs > 0):
                event = EVENT()
                event.set_name(name)
                event.set_start(start)
                event.set_end(end)
                events.append(event)
    print()
    print(len(events), "events today!")


def join_meeting(name):
    print()
    print("Joining meeting...")
    print("Name:", name)
    meeting = None
    for met in meetings:
        if met.name in name:
            meeting = met
            break
    if meeting == None:
        print("ERROR: Meeting not found")
        return
    print("Meeting found")
    if meeting.link == None:
        print("Joining with ID...")
        Auto.manualjoin(meeting.id, meeting.pw)
    else:
        print("Joning with Link...")
        Auto.linkjoin(meeting.link)


def activate_event(event):
    global active
    active = True
    winsound.Beep(1500, 500)
    winsound.Beep(2000, 500)
    winsound.Beep(2500, 500)
    print("Alert!")
    print(event.get_name(), "in 5 minutes")
    print(event.get_start())
    while True:
        print("Do you want to join? (Y,n)")
        ans = input(">>>")
        if ans in ("", "Y", "y"):
            join_meeting(event.get_name())
            break
        elif ans in ("N", "n"):
            break
    active = False


def loop():
    while True:
        now = (datetime.utcnow() + timedelta(hours=1)).replace(tzinfo=pytz.timezone("CET"))
        e = None
        for event in events:
            delta = now - event.get_start()
            if -(delta.seconds + delta.days*86400) <= 60*3:
                thread = threading.Thread(target=activate_event, args=[event])
                thread.daemon = True
                thread.start()
                e = event
                break
        if e != None:
            events.remove(e)
        t.sleep(5)
        if len(events) == 0 and not active:
            print("All done")
            print("Terminating...")
            t.sleep(5)
            exit(0)
        t.sleep(55)

load()
loop()
