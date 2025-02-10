months = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December"
    }
date_input = input("Enter the date. If a single digit, input 0 before number (mm/dd/yyyy): " )
month, day, year = date_input.split('/')
month_name = months[month]
readable_date = f"{month_name} {int(day)}, {year}"
print("Date Output: ", readable_date)


