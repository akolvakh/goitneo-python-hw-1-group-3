from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    days_of_week = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days
        day_of_week = (today + timedelta(days=delta_days)).strftime("%A")

        if delta_days < 7:
            days_of_week[day_of_week].append(name)
        elif delta_days == 7 and next_week.weekday() == 0:  # if birthday falls on a weekend
            days_of_week['Monday'].append(name)

    for day, names in days_of_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")

# Приклад виклику функції з відповідним списком користувачів
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 12, 5)},
    {"name": "Jan Koum", "birthday": datetime(1976, 12, 10)},
    # Додайте інших користувачів, використовуючи таку ж структуру словників
]

get_birthdays_per_week(users)
