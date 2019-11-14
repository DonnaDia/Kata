#Vers 1
import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    strptime = datetime.datetime.strptime
    format = "%B %d, %Y"
    return strptime(current_date, format) <= strptime(expiration_date, format) and\
                             entered_code is correct_code


#Vers 2
from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
	now_date = datetime.strptime(current_date, '%B %d, %Y')
	exp_date = datetime.strptime(expiration_date, '%B %d, %Y')
	return True if entered_code == correct_code and now_date <= exp_date else False