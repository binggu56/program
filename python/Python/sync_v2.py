#!/usr/bin/python
# Filename: backup_v4
import time,os,sys

def check(dir):
	"check if the file exist."
	if not os.path.exists(dir):
		sys.exit('The file does not exist.')
	else:
		print("%s will be backuped." %(dir))

def sync(source,target_dir):
#	target_dir = '/home/bing/backup/' 
#	target=target_dir+time.strftime('%Y%m%d') + '.tar.gz'
	log.write("Backup %s to %s\n" %(source,target_dir))
	command='rsync -r -v --partial --max-size=100m %s %s' %(source,target_dir)
	if os.system(command) == 0:
		print('Successful backup to ',target_dir)
	else:
		print('Backup failed.')

##
# Configuration variables
##

# Local
script_dir = '/Users/bing/Documents/Python' # Dir of script

# Remote
remote_host = 'pople.psc.sc.edu'
remote_user = 'bing'
remote_dir = '/home/'+remote_user+'/backup'

# what to do 
send_alert = False # send emails alert of backup when it finished

# other
alert_email = 'binghongcha08@gmail.com'
path_to_sendmail = '/usr/sbin/sendmail'

# Start log file

log_path = "%s/backup.log" %(script_dir)
log = open(log_path,'a')
log.write(
	"Starting script at %s\n" % time.strftime("%m/%d/%Y %H:%M:%S")
	)
t1 = time.time()

while True:
	try:
		dest=int(input('Where to backup: 1) POPLE 2) Dropbox\n'))
		break
	except ValueError:
		print("Oops!  That was no valid number.  Try again...")


if dest==1:
	target_dir='bing@pople.psc.sc.edu:/home/bing/backup/'
else:
	target_dir='/Users/bing/Dropbox/backup/'
		
if len(sys.argv) < 2:
	src = input("Enter the name of file or directory you want to backup:")
	check(src)
	sync(src,target_dir)
else:
	for arg in sys.argv[1:]:
		check(arg)
		sync(arg,target_dir)

# End lof file
t2 = time.time()
log.write("Ending script at %s\n" % time.strftime("%m/%d/%Y %H:%M:%S"))
log.write("Time to run script: %s seconds\n" % (t2-t1))
log.write("********************************\n\n")
log.write("********************************\n")
log.close()

# send email alert
if send_alert:

	MAIL = path_to_sendmail
	msg = "To: %s\r\n Subject: Backup Log\r\n\r\n" %(alert_email)
	f = open(log_path, 'r') # Get contents of log file
	msg += f.read()
	f.close()

	p = os.popen("%s -t" % MAIL, 'w') # Send email
	p.write(msg)
	exitcode = p.close()
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that
