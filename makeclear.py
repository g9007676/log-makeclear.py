#! /usr/bin/python

import os, re, datetime

yestoday = datetime.date.today() + datetime.timedelta(days=-1)

yestoday = yestoday.strftime("%Y%m%d")

log_dir = '/var/tmp'
for file in os.listdir(log_dir):
    filenames = os.path.splitext(file)
    ret = re.search('access|error', filenames[0])
    if ret:
        new_filename = log_dir + '/log/' + yestoday + '-' + filenames[0] + filenames[1]
        filename = os.path.abspath(file)
        os.rename(filename, new_filename)



day_limit = datetime.date.today() + datetime.timedelta(days=-3)
print day_limit
log_dir = '/var/tmp/log'
for file in os.listdir(log_dir):
    file_pref = file.rsplit('-', 2)[0]
    file_time = datetime.datetime.strptime(file_pref, "%Y%m%d").date()

    if file_time < day_limit:
        filenames = os.path.splitext(file)
        filename = filenames[0] + filenames[1]
        os.remove(log_dir + '/' + filename)
