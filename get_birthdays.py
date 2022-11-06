from datetime import datetime, timedelta

users = [
    {
        'name': 'Jake',
        'birthday': datetime(year=1988, month=12, day=1)
    },
    {
        'name': 'Fin',
        'birthday': datetime(year=1988, month=11, day=10)
    },
    {
        'name': 'Bubble Gum',
        'birthday': datetime(year=1988, month=11, day=11)
    },
    {
        'name': 'Fiona',
        'birthday': datetime(year=1989, month=11, day=11)
    },
    {
        'name': 'Pam',
        'birthday': datetime(year=1989, month=1, day=2)
    },
    {
        'name': 'Philip',
        'birthday': datetime(year=1990, month=2, day=3)
    },
    {
        'name': 'Noah',
        'birthday': datetime(year=1990, month=1, day=3)
    },
    {
        'name': 'Jane',
        'birthday': datetime(year=1990, month=1, day=1)
    },
    {
        'name': 'Jim',
        'birthday': datetime(year=1990, month=1, day=1)
    },
    {
        'name': 'Bill',
        'birthday': datetime(year=1994, month=1, day=1)
    },
    {
        'name': 'Bob',
        'birthday': datetime(year=1990, month=12, day=31)
    }
]

week = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

def get_birthdays_per_week(users):
    current_date = datetime.now()
    date_in_week = current_date + timedelta(days=7)
    current_year = current_date.year
    current_month = current_date.month
    date_in_week_month = date_in_week.month

    months = []
    months.append(current_month)
    if not date_in_week_month in months:
        months.append(date_in_week_month)

    days = []
    for i in range(1, 8):
        check_date = current_date + timedelta(days=i)
        days.append(check_date.day)

    birthdays = {}

    for user in users:
        name = user['name']
        birthday = user['birthday']
        birthday_day = birthday.day
        birthday_month = birthday.month

        if birthday_day in days and birthday_month in months:
            current_birthday_date = datetime(year=current_year, month=birthday_month, day=birthday_day)
            if birthday_month == 1 and birthday_day <= 7 and current_month == 12:
                current_birthday_date = datetime(year=current_year+1, month=birthday_month, day=birthday_day)

            current_birthday_date_weekday = week[current_birthday_date.weekday()]
            if current_birthday_date_weekday in ('Saturday', 'Sunday'):
                current_birthday_date_weekday = 'Monday'

            if birthdays.get(current_birthday_date_weekday) is None:
                birthdays[current_birthday_date_weekday] = [name]
            else:
                birthdays[current_birthday_date_weekday].append(name)

    for birthday in birthdays:
        names = ', '.join(birthdays[birthday])
        str = f"{birthday}: {names}"
        print(str)

get_birthdays_per_week(users)
