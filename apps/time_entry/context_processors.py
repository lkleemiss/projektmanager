from datetime import datetime


def user_time_entries(request):
    if request.user.is_authenticated:
        today = datetime.today().date()
        user_time_entries = request.user.time_entries.all()
        entries_today = user_time_entries.filter(date=today)

        seconds_total = 0
        for entry in user_time_entries:
            seconds_total = seconds_total + entry.seconds
        minutes, seconds = divmod(seconds_total, 60)
        hours, minutes = divmod(minutes, 60)

        seconds_today_total = 0
        for entry in entries_today:
            seconds_today_total = seconds_today_total + entry.seconds
        minutes_today, seconds_today = divmod(seconds_today_total, 60)
        hours_today, minutes_today = divmod(minutes_today, 60)

        return {'time_entries': user_time_entries, 'entries_today': entries_today, 'today': today,
                'minutes_total': minutes, 'hours_total': hours, 'hours_today': hours_today,
                'minutes_today': minutes_today}
    return {}
