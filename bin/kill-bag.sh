#!/usr/bin/env bash

## Require bag path
if [ ! -z "$1" ]
then
  BAGPATH=$1
  echo "Killing $BAGPATH"
else
  echo "Requires bag path (eg. /srv/bagname) as argument"
  exit 1;
fi

sudo rm -rf $BAGPATH
sudo touch $BAGPATH
