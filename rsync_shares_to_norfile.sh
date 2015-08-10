#!/bin/sh
PATH=/usr/local/bin:/usr/bin:/bin:/sbin:$PATH
LOGFILE=/home/libacct/replication.log
rsync -a --ignore-times --omit-dir-times --no-perms --log-file=$LOGFILE /srv/workspace/ /mnt/autofs/workspace2 || exit 1;
rsync -a --ignore-times --omit-dir-times --no-perms --log-file=$LOGFILE /srv/bagit/ /mnt/autofs/bagit2 || exit 1;
