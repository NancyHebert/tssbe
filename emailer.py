# Just run at the commandline to see how it works.
import datetime
from smtplib import SMTP

debuglevel = 1

smtp = SMTP()
smtp.set_debuglevel(debuglevel)
try:
	connection = smtp.connect('smtp-relay.sendinblue.com', 587)
	print "connection: ", connection
	login = smtp.login('jcassid2@uottawa.ca', 'XF7YaPKrMWqQ604f')
	print "login: ", login
except Exception as e:
	print "error in emailer: ", e
	raise

from_addr = "John Doe <john@doe.net>"
to_addr = "shamdan@uottawa.ca"

subj = "hello"
date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )

message_text = "Hello\nThis is a mail from your server\n\nBye\n"

msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, to_addr, subj, date, message_text )

try: 
	smtp.sendmail(from_addr, to_addr, msg)
except Exception as e:
	print "error in emailer: ", e
finally:
	smtp.quit()