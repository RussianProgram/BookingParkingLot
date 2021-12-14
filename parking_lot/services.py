import datetime
import pytz

def to_datetime(string:str):
    str_datetime = datetime.datetime.strptime(string,'%d.%m.%Y %H:%M:%S')
    str_datetime.replace(tzinfo=pytz.UTC)
    return str_datetime.timestamp()