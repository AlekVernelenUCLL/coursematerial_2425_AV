# write your code here
def hours(duration):
    h_in_duration = duration//3600
    return h_in_duration

def minutes(duration):
    h = hours(duration)
    minutes_in_leftover = (duration-(h*3600))//60
    return minutes_in_leftover

def seconds(duration):
    h = hours(duration)
    m = minutes(duration)
    seconds_in_leftover = duration-(h*3600)-(m*60)
    return seconds_in_leftover

