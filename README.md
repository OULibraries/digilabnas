# Assorted Scripts Related to the DigiLab NAS


```
bin/
├── digilab_file_rename_ready_for_script.py
├── fix-smb-perms.sh
├── kill-bag.sh
└── rsync_shares_to_norfile.sh
```



## digilab_file_rename_ready_for_script.py

On an as-needed basis, we use this script to do some file name normalization on image sets that are ready to be prepped for bagging.

1. Run in test mode (default) to genearate a report of the changes that would be made and send them to the DigiLab for review. 
```
digilab_file_rename_ready_for_script.py --src /srv/workspace/5_Ready_for_script --dest /srv/temp > output
```
2. Run in destroy mode to actually make changes
```
digilab_file_rename_ready_for_script.py --src /srv/workspace/5_Ready_for_script --dest /srv/temp --destroy > output
```
3. Move renamed files to their final destination
```
mv -v --no-clobber /srv/temp/* /srv/workspace/6_Prep_to_bag/ > move.out
```
