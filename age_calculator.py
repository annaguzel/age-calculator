from datetime import datetime
from datetime import time
import datetime

def check_birthdate(year, month, day):
	birthdate=datetime.date(year, month, day)
	if (birthdate>=datetime.date.today()):
		return False
	else:
		return True


def calculate_age(year, month, day):
	birthdate=datetime.date(year, month, day)
	today_year = datetime.date.today()
	age=(today_year-birthdate)
	age_in_years=age.days/365
	print ("You are {} years old".format(age_in_years))


def main():
	year=int(input("Enter year of birth:"))
	month=int(input("Enter month of birth:"))
	day=int(input("Enter day of birth:"))

	if (check_birthdate(year,month,day)==True):
		calculate_age(year,month,day)
	else:
		print("Birthdate is invalid")
	# write main code here


if __name__ == '__main__':
	main()
