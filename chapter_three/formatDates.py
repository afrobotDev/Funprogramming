def sort_dates(dates):
    dates_sorted = sorted(dates, key=format_date)# Use format_date() to order
    return dates_sorted 


def format_date(date):
    date_list = date.split('-')
    return f"{date_list[2]}{date_list[0]}{date_list[1]}"
