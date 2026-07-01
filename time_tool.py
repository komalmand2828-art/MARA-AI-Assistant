from datetime import datetime

def time_tool():

    return datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )