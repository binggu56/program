
# Copyright 2009 James Crickmere <james.crickmere@googlemail.com>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0


"""
    Common functions for the configuration and deamon scripts to use.
"""

import os, glob, sqlite3, cPickle, shutil, re, string, time

LOGFILE = os.environ['HOME'] + '/pyadis-log'

# Location of settings file (containing a pickled dictionary like 'DEFAULTS').
SETTINGS = os.environ['HOME'] + '/.pyadis-config'

# Values to use to create a new settings file if it does not exist.
DEFAULTS = {
    'backup_dirs':[os.environ['HOME'], ],
    'backup_to':'/mnt/fileserver/backup',
    'scan':15,
    'current_revision':1,
}

# Name of the backup index file.
INDEX_FILE = os.environ['HOME'] + '/.pyadis-index-2.sqlite3'

def get_settings():
    """Returns a dictionary of settings from the pickled data in
    'SETTINGS'.
    
    Creates the file with values 'DEFAULTS' id it does not exist.
    """
    
    try:
        config = open(SETTINGS, 'r')
        settings = cPickle.load(config)
    except IOError:
        config = open(SETTINGS, 'w')
        settings = DEFAULTS
        cPickle.dump(settings, config)
    
    config.close()
    return settings


def save_settings(settingsdict):
    """Writes 'settingsdict' to the settings file."""
    with open(SETTINGS, 'w') as config:
        cPickle.dump(settingsdict, config)


def scan_path(path):
    """Scans 'path' and returns a list of tuples, the first value
    of which is the relative path to each file, and the second value
    is the date of last content modification.
    """
    
    os.chdir(path)
    root_files = glob.glob('*')
    dirs = [ ]
    files = [ ]
    for f in root_files:
        if os.path.isdir(f):
            dirs.append(f)
        elif os.path.isfile(f):
            files.append(f)
    
    while len(dirs) > 0:
        newdirs = [ ]
        
        for d in dirs:
            dirscan = glob.glob(d + '/*')
            for f in dirscan:
                if os.path.isdir(f):
                    newdirs.append(f)
                elif os.path.isfile(f):
                    files.append(f)

        dirs = newdirs
    
    files_and_dates = [ ]
    
    for f in files:
        stats = os.stat(f)
        files_and_dates.append( (f, stats.st_mtime) )

    return files_and_dates
    

def get_index_files(base_dir):
    """Returns a list with the same format as 'scan_dir', except
    from the backup index."""
    
    settings = get_settings()
    connection = sqlite3.connect(INDEX_FILE)
    cursor = connection.cursor()
    
    try:
        cursor.execute("select path, updated from files where base_dir=?", (base_dir, ))
    except sqlite3.OperationalError:
        cursor.execute("create table files (base_dir, path, updated)")
        return [ ]
    
    results = cursor.fetchall()
    connection.close()
    return results


def log(message):
    date_time = time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime())
    log_message = '[' + date_time + '] ' + message
    print '[LOG]' + log_message
    with open(LOGFILE, 'a') as log:
        log.write(log_message + '\n')


def compare_files(real_files, index_files):
    to_backup = [ ]
    for real in real_files:
        if real not in index_files:
            to_backup.append(real[0])
    
    return to_backup


def can_backup():
    """Returns bool depending on weather the 'backup to' directory is available."""
    settings = get_settings()
    return os.path.isdir(settings['backup_to'])


def backup(base_dir, files):
    
    if len(files) == 0:
        return None
    
    if base_dir[-1] == '/':
        base_dir = base_dir[:-1]
    
    settings = get_settings()
    
    # Check if we can access the backup directory.
    if can_backup() == False:
        log("Target directory unavailable.")
        return None
    
    connection = sqlite3.connect(INDEX_FILE)
    cursor = connection.cursor()
    
    revision = settings['current_revision'] + 1
    target = settings['backup_to'] + '/' + str(revision) + '_' + re.sub(r'[^a-z0-9\.]', '.', string.lower(base_dir))
    while os.path.exists(target):
        revision += 1
        target = settings['backup_to'] + '/' + str(revision) + '_' + re.sub(r'[^a-z0-9\.]', '.', string.lower(base_dir))
    
    os.mkdir(target)
    settings['current_revision'] = revision
    save_settings(settings)
    
    num_files = len(files)
    log("About to copy %s files as revision %s in %s." % (str(num_files), str(revision), target))
    
    for f in files:
        try:
            # Create folders
            chuncked = f.split('/')
            if len(chuncked) > 1:
                chuncked = chuncked[:-1]
                so_far = ''
                for folder in chuncked:
                    if os.path.isdir(target + '/' + so_far + folder) == False:
                        os.mkdir(target + '/' + so_far + folder)
                    so_far = so_far + folder + '/'
            
            shutil.copyfile(base_dir + '/' + f, target + '/' + f)
            stats = os.stat(f)
            cursor.execute("select * from files where base_dir=? and path=?", (base_dir, f))
            if len(cursor.fetchall()) > 0:
                connection.commit()
                cursor.execute("update files set updated=? where base_dir=? and path=?", (stats.st_mtime, base_dir, f))
            else:
                connection.commit()
                cursor.execute("insert into files values (?, ?, ?)", (base_dir, f, stats.st_mtime))
            
        except IOError as (errno, errstr):
            log("Failed to copy file %s: %s." % (f, errstr))
    
    connection.commit()
    connection.close()
    log("Done.")


def reset_revision_counter():
    settings = get_settings()
    settings['current_revision'] = 0
    save_settings(settings)



    
    
