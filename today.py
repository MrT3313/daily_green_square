from datetime import date

current_date = str(date.today())

text_file = open("date_tracker.txt", "w")
record = "Today is " + current_date + "\n" + "Have a good Day!"
text_file.write(record)
text_file.close()
