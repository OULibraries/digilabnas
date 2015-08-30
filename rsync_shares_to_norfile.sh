#!/bin/sh
PATH=/usr/local/bin:/usr/bin:/bin:/sbin:$PATH
LOGFILE=/var/log/replication/rsync_to_norfile.log
TODAY=`date`
EMAIL="libsyslogs@ou.edu"
## Go away if we're still running
(
  flock -x -w 10 200 || exit 1;

  rsync -az --ignore-times --omit-dir-times --no-perms --log-file=$LOGFILE /srv/workspace/ /mnt/autofs/workspace2
  mail -s "rsync lib-52 to norfile $TODAY" $EMAIL < $LOGFILE
  rsync -az --ignore-times --omit-dir-times --no-perms --log-file=$LOGFILE /srv/bagit/ /mnt/autofs/bagit2
  mail -s "rsync lib-52 to norfile $TODAY" $EMAIL < $LOGFILE
) 200>/var/lock/freezer_bag_cronlock
