from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання

    new_dict = {}
    dates_range = []

    list_Monday = []
    list_Tuesday = []
    list_Wednesday = []
    list_Thursday = []
    list_Friday = []
    list_Saturday = []
    list_Sunday = []

    if len(users) == 0:
        return new_dict


    now = date.today()
    #now = datetime(year=2023, month=12, day=27).date()

    for i in range(7):
        date_interval = timedelta(days=i)
        tmp_date = now + date_interval
        dates_range.append(tmp_date)
        i += 1


    for user in users:
        
        if user['birthday'].month == 1 and now.month == 12:
            tmp_date = datetime(year=now.year + 1, month= user['birthday'].month, day=user['birthday'].day).date()    
        else:
            tmp_date = datetime(year=now.year, month= user['birthday'].month, day=user['birthday'].day).date()

        if tmp_date in dates_range:

            if tmp_date.weekday() == 0:
                list_Monday.append(user['name'])
            
            if tmp_date.weekday() == 1:
                list_Tuesday.append(user['name'])
            
            if tmp_date.weekday() == 2:
                list_Wednesday.append(user['name'])
            
            if tmp_date.weekday() == 3:
                list_Thursday.append(user['name'])
            
            if tmp_date.weekday() == 4:
                list_Friday.append(user['name'])
            
            if tmp_date.weekday() == 5:
                #list_Saturday.append(user['name'])
                list_Monday.append(user['name'])
            
            if tmp_date.weekday() == 6:
                #list_Sunday.append(user['name'])
                list_Monday.append(user['name'])

    if len(list_Monday) > 0:
        new_dict['Monday'] = list_Monday
    
    if len(list_Tuesday) > 0:
        new_dict['Tuesday'] = list_Tuesday
    
    if len(list_Wednesday) > 0:
        new_dict['Wednesday'] = list_Wednesday

    if len(list_Thursday) > 0:
        new_dict['Thursday'] = list_Thursday

    if len(list_Friday) > 0:
        new_dict['Friday'] = list_Friday
    
    if len(list_Saturday) > 0:
        new_dict['Saturday'] = list_Saturday
    
    if len(list_Sunday) > 0:
        new_dict['Sunday'] = list_Sunday

    return new_dict


if __name__ == "__main__":
    
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 2).date()},
        {"name": "Jan1 Koum", "birthday": datetime(1977, 2, 15).date()},
        {"name": "Jan2 Koum", "birthday": datetime(1978, 3, 11).date()},
        {"name": "Jan3 Koum", "birthday": datetime(1979, 4, 14).date()},
        {"name": "Jan4 Koum", "birthday": datetime(1980, 5, 8).date()},
        {"name": "Jan5 Koum", "birthday": datetime(1981, 6, 22).date()},
        {"name": "Jan6 Koum", "birthday": datetime(1982, 7, 25).date()},
        {"name": "Jan7 Koum", "birthday": datetime(1983, 8, 30).date()},
        {"name": "Jan8 Koum", "birthday": datetime(1976, 9, 29).date()},
        {"name": "Jan9 Koum", "birthday": datetime(1976, 10, 5).date()},
        {"name": "Jan10 Koum", "birthday": datetime(1976, 11, 28).date()},
        {"name": "Jan11 Koum", "birthday": datetime(1976, 12, 27).date()},
        {"name": "Jan12 Koum", "birthday": datetime(1976, 10, 7).date()}
    ]
    

    result = get_birthdays_per_week(users)
    
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")