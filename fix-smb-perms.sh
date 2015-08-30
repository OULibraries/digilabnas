#!/bin/sh


#sudo find /srv/bagit -type f -exec sudo chmod -v  0764 {} +
sudo find /srv/bagit -type f -print0 |  sudo xargs -0 chmod -v  0764 

#sudo find /srv/bagit -type d -exec sudo chmod -v  775 {} +
sudo find /srv/bagit -type d -print0 |  sudo xargs -0 chmod -v  775


sudo chgrp -R SOONER\\lib-digilab-bagit-write /srv/bagit/
sudo chmod -v  g+s /srv/bagit/

#sudo find /srv/workspace -type f -exec sudo chmod -v  0764 {} +
sudo find /srv/workspace -type f -print0 | sudo xargs -0 chmod -v  0764

#sudo find /srv/workspace -type d -exec sudo chmod -v  775 {} +
sudo find /srv/workspace -type d -print0 | sudo xargs -0 chmod -v  775



sudo chgrp -R SOONER\\lib-digilab-workspace-write /srv/workspace/

sudo chmod -v  g+s /srv/workspace/
