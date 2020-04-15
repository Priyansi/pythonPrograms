from datetime import datetime

CITIES = {'Los Angeles': '4:00', 'New York': '7:00', 'Caracas': '7:30', 'Buenos Aires': '9:00', 'London': '12:00',
          'Rome': '13:00', 'Moscow': '15:00', 'Tehran': '15:30', 'New Delhi': '17:30', 'Beijing': '20:00', 'Canberra': '22:00'}


def city_time_diff(city):
    return datetime.strptime(CITIES[city], '%H:%M')


def time_difference(city_a, timestamp, city_b):
    x = datetime.strptime(timestamp, '%B %d, %Y %H:%M')
    diff = city_time_diff(city_b)-city_time_diff(city_a)
    return '{d.year}-{d.month}-{d.day} {d.hour:02}:{d.minute:02}'.format(d=x+diff)


print(time_difference("New York", "December 31, 1970 13:40", "Beijing"))
# returns output like - 1971-1-1 02:40
