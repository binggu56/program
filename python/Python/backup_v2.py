#!/usr/bin/python
# Filename: backup.py
import os
import time
import sys
def main(argv):
    if len(argv) < 2:
        sys.stderr.write("Usage: %s <database>\n" % (argv[0],))
        return 1

    if not os.path.exists(argv[1]):
        sys.stderr.write("ERROR: Database %r was not found!\n" % (argv[1],))
        return 1

#if __name__ == "__main__":
#    sys.exit(main(sys.argv))
# 1. The files and directories to be backed up are specified in a list.
source = sys.argv[1]
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that
# 2. The backup must be stored in a main backup directory
target_dir1 = '/home/bing/backup/' # Remember to change this to what you will be using
target_dir2 = '/Users/bing/Dropbox/backup/'
# 3. The files are backed up into a zip file.
#today=target_dir+time.strftime('%Y%m%d')
#now=time.strftime('%H%M%S')
#if not os.path.exists(today):
#	os.mkdir(today)
#	print 'Successfully created directory',today

# 4. The name of the zip archive is the current date and time
#comment=raw_input('Enter a comment -->')
target1=target_dir1+time.strftime('%Y%m%d') + '.tar.gz'
target2=target_dir2+time.strftime('%Y%m%d') + '.tar.gz'
#if len(comment)==0:

#else:
#	target=today+os.sep+'_'+comment.replace('','_')+'.tar.gz'
# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
#zip_command = "tar zcvpf - %s | ssh bing@pople.psc.sc.edu "cat > %s"" %(source,target)
command1 = 'tar zcvpf - %s | ssh bing@pople.psc.sc.edu "cat > %s"' %(source,target1)
command2 = 'tar -cvzf %s %s'%(target2,source) 
place=raw_input('Where to backup: 1. POPLE 2. Dropbox')
if place=='1':
	if os.system(command1) == 0:
		print 'Successful backup to', target_dir1
	else:
		print 'Backup failed.'
elif place=='2':
	if os.system(command2) == 0:
		print 'Successful backup to', target_dir2
        else:
                print 'Backup failed.'
