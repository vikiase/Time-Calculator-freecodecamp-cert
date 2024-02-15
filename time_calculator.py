def add_time(start, duration, start_day=''):
    #duration
    duration_split = duration.split(':')
    duration_minutes = int(duration_split[0])*60 + int(duration_split[1])
    #start info
    start_split = start.split(':')
    start_second_split = str(start_split[1]).split()
    start_hours = start_split[0]
    start_minutes = int(start_second_split[0]) + int(start_hours)*60
    a_pm = start_second_split[1]
    #values pro vypocty
    final_hours = (start_minutes+duration_minutes)//60
    if final_hours > 12:
        final_hours = final_hours - (final_hours//12)*12
        if final_hours == 0:
            final_hours = str(12)
        else:
            final_hours = str(final_hours - (final_hours // 12) * 12)
    final_minutes = (start_minutes+duration_minutes) - ((start_minutes+duration_minutes)//60)*60
    if final_minutes < 10:
        final_minutes = '0' + str(final_minutes)
    else:
        final_minutes = str(final_minutes)
    half_days = ((start_minutes + duration_minutes)/60)/12
    AM = 'AM'
    PM = 'PM'
    final_am_or_pm = str(am_pm(start_minutes, duration_minutes, a_pm, half_days))
    final_days_later = int(days_later(start_minutes, duration_minutes, a_pm, half_days))
    if final_days_later == 1:
        final_days_later_msg = "(next day)"
    elif final_days_later == 0:
        final_days_later_msg = ""
    else:
        final_days_later_msg = f"({final_days_later} days later)"
    new_time = f"{final_hours}:{final_minutes} {final_am_or_pm} {final_days_later_msg}"

    if start_day != '':
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for day in week:
            if start_day.lower() == day.lower():
                index = week.index(day)
                if final_days_later + index > 6:
                    sub = final_days_later - final_days_later//7
                    final_day = week[sub + index]
                    new_time = f"{final_hours}:{final_minutes} {final_am_or_pm}, {final_day} {final_days_later_msg}"
                else:
                    final_day = week[final_days_later + index]
                new_time = f"{final_hours}:{final_minutes} {final_am_or_pm}, {final_day} {final_days_later_msg}"

    return new_time

def days_later(start_minutes, duration_minutes, a_pm, half_days):
    full_days = half_days/2
    days_later_msg = ''
    if 2 > full_days > 1 and a_pm == 'AM':
        days_later_msg = 1
        return days_later_msg
    elif 3 > half_days > 1 and a_pm == 'PM':
        days_later_msg = 1
        return days_later_msg
    elif full_days > 2 and a_pm == 'AM':
        days_later_msg = full_days
        return days_later_msg
    elif half_days > 3 and a_pm == 'PM':
        days_later_msg = half_days/2 + 1
        return days_later_msg
    else:
        days_later_msg = 0
        return days_later_msg

def am_pm(start_minutes, duration_minutes, a_pm, half_days):
    AM = 'AM'
    PM = 'PM'
    if half_days >= 1:
        if a_pm == 'AM' and int(half_days)%2 != 0:
            return PM
        elif a_pm == 'AM' and int(half_days)%2 == 0:
            return AM
        elif a_pm == 'PM' and int(half_days)%2 != 0:
            return AM
        else:
            return PM
    else:
        return a_pm
