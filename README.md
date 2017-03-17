# Assorted Scripts Related to the DigiLab NAS


```
bin/
├── digilab_file_rename_ready_for_script.py
├── fix-smb-perms.sh
├── kill-bag.sh
└── rsync_shares_to_norfile.sh
```



## digilab_file_rename_ready_for_script.py

On an as-needed basis, we do the following file name normalization on image sets that are ready to be bagged:

1. Run the report to see if everything looks OK. 
```
/opt/digilabnas/bin/digilab_file_rename_ready_for_script.py --src /srv/workspace/5_Ready_for_script/ /srv/temp >output
```
1. Run in destroy mode to actually make changes
```
/opt/digilabnas/bin/digilab_file_rename_ready_for_script.py --src /srv/workspace/5_Ready_for_script/ --dest /srv/temp --destroy >output
```
1. Move renamed files to their final destination
```
mv -v --no-clobber /srv/temp/* /srv/workspace/6_Prep_to_bag/ > move.out
```