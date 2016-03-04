#!/usr/bin/env python
# Filename: backup_ver2.py

import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = ['/var/lib/jenkins/jobs/eyas_prod231/workspace/target/ROOT','']
# If you are using Windows use  source = [r'C:\Documents', r'D:\Work'] or something like that 

# 2. The backup must be stored in a main bakcup directory
target_dir = '/var/lib/jenkins/prod231Backup/' # Remember to change this to what you will be using

# 3. The files are backed up into a tar file.
# 4. The current day is the name of the subdirectory in the main directory
today = target_dir + time.strftime('%Y%m%d')
# The current time is the name of the tar archive
now = time.strftime('%H%M%S')

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
	os.mkdir(today) # make directory
	print 'Successfully created directory', today

# The name of the tar file
target = today + os.sep + now + '.tar.gz'

# 5. We use the tar command (in Unix/Linux) to put the files in a tar archive
tar_command = "tar -cvzf '%s' %s -X /home/zj2008/excludes.txt" % (target, ' '.join(source))

# Run the backup
if os.system(tar_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'
