"""
Generic class to send emails
"""

import datetime
from smtplib import SMTP

def sendmail(from_addr, to_addr, subject, body)

debuglevel = 1

smtp = SMTP()
smtp.set_debuglevel(debuglevel)
try:
	connection = smtp.connect('smtp-relay.sendinblue.com', 587)
	# connection = smtp.connect('smtp-relay.csmtp.net', 587)
	# print "connection: ", connection
	login = smtp.login('jcassid2@uottawa.ca', 'XF7YaPKrMWqQ604f') # TODO: move to settings
	# login = smtp.login('PGME_hlukasik@uottawa.ca', 'WiredForS0und') # TODO: move to settings
	# print "login: ", login
except Exception as e:
	print "error in emailer: ", e
	raise

date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )

msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (from_addr, to_addr, subject, date, body)

try: 
	smtp.sendmail(from_addr, to_addr, msg)
except Exception as e:
	print "error in emailer: ", e
finally:
	smtp.quit()