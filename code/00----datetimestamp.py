from datetime import datetime

now = datetime.now()
print "%d-%02d-%02d" % (now.year, now.month, now.day)