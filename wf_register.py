from utils import wf
import json
from datetime import datetime, timezone
now = datetime.now(timezone.utc).isoformat()
 #dateFormat(now, "UTC:h:MM:ss TT Z");

#now = datetime.datetime.now().isoformat()
#now = str(datetime.datetime.utcnow())
#print(now)
wf_test = wf.workflow()
#wf_test.register()

wf_test.send_email('cro8@uottawa.ca','cro8@uottawa.ca', 'test', 'test message', now)
