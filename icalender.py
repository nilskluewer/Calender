# Initialize the calendar
from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz
import os

cal = Calendar()
cal.add('prodid', '-//My Calendar Product//mxm.dk//')
cal.add('version', '2.0')

# Data to be included in the calendar
# Updated data to be included in the calendar
data = [
    # ... Existing events here ...
    {
        'day': 'Mon',
        'time': '17:00 - 18:30',
        'date': '09.10.2023',
        'end_date': '22.01.2024',
        'location': '(LIVE)',
        'description': 'Lectures',
        'event_type': 'Lecture'
    }
    # ... Add more events here if needed ...
]


# Vienna time zone
vienna_tz = pytz.timezone('Europe/Vienna')

# Add events to calendar
for entry in data:
    event = Event()
    date_str = entry['date']
    time_str = entry['time'].split(' - ')[0]  # taking start time
    date_time_str = f"{date_str} {time_str}"

    event_start_time = datetime.strptime(date_time_str, '%d.%m.%Y %H:%M')
    event_start_time = vienna_tz.localize(event_start_time)

    event_end_time = datetime.strptime(f"{date_str} {entry['time'].split(' - ')[1]}", '%d.%m.%Y %H:%M')
    event_end_time = vienna_tz.localize(event_end_time)

    event.add('summary', entry['description'])
    event.add('dtstart', event_start_time)
    event.add('dtend', event_end_time)
    event.add('location', entry['location'])
    cal.add_component(event)

# Save to file
file_path = 'Sustainability in Computer Science.ics'
with open(file_path, 'wb') as f:
    f.write(cal.to_ical())

file_path
