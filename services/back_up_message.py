""" Backup Message """
import maya

from common.constant import PATH, TIMEFORMAT
from model.date_message import get_date
from model.message import get_message


def load_message(data):
    file_path = PATH.format(data['filename'])
    print(data['timezone'])
    with open(file_path, 'w') as file:
        dates = get_date(data['room'])
        for date in dates:
            file.write(f"*****{date['date']}*****\n")
            messages = get_message(date['date'], data['room'])
            for message in messages:
                time = maya.parse(message['time']).datetime(to_timezone=data['timezone']).time()
                time_format = time.strftime(TIMEFORMAT)
                line = "{user} - {time} : {message}\n".format(user=message['username'], time=time_format,
                                                              message=message['text'])
                file.write(line)
