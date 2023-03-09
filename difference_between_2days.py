Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from dateutil.relativedelta import relativedelta
... from datetime import datetime
... 
... # Get the first date from user input
... date1_str = input("Enter the start date (YYYY-MM-DD): ")
... date1 = datetime.strptime(date1_str, '%Y-%m-%d').date()
... 
... # Get the second date from user input
... date2_str = input("Enter the finish date (YYYY-MM-DD): ")
... date2 = datetime.strptime(date2_str, '%Y-%m-%d').date()
... 
... # Calculate the difference between the two dates
... diff = relativedelta(date2, date1)
... 
... # Print the result
... print("Sure, difference between the two dates is:")
... print(f"{diff.years} Years, {diff.months} Months, {diff.days} Days")
