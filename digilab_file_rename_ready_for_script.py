#!/usr/bin/env python

import os
import re
import sys
import codecs

# Regex match for any non-alphanumeric/non-dot character
alpha_num = re.compile('[^0-9a-zA-Z.]+')
def rejigger_file_structure(directory):
    # get the parent directory
    parent_dir = os.path.split(PATH)[0]
    # get the directories just under the one specified
    for project_dirs in os.listdir(directory):
        ## skip hidden files and lightroom previews
        if (not project_dirs.startswith('.') 
            and not project_dirs.endswith('.lrdata')):
            ## Skip folders as directed by Barb
            #and not project_dirs == 'Darwin_DMP'
            #and not project_dirs == 'Portraits_Large'
            #and not project_dirs == 'Portraits_Small'
            #and not project_dirs == 'Scientific_Instruments_&_Historical_Artifacts'
            ## Skip folders as directed by Barb
            #and not project_dirs == 'Aristarchus_1572' 
            #and not project_dirs == 'Fontana_1646' 
            #and not project_dirs == 'Stelluti_1637'):
            project_dir = os.path.join(directory, project_dirs)
            # get the name of this directory, which is probably a project name
            base_name = os.path.basename(project_dir)
            base_name = alpha_num.sub('_', base_name)
            try:
                print(base_name)
            except Exception:
                pass
            # set the output directory
#            output_dir = os.path.join(parent_dir, 'to_bag', base_name)
            output_dir = os.path.join(OUTPUT_STR, base_name)
            ## crawl project directories only, not files at this level
            print(project_dir)
            if os.path.isdir(project_dir):
                #print(project_dir)
                for rel_sub_dir in os.listdir(project_dir):
                    # filter lightroom previews and hidden directories
                    if not rel_sub_dir.startswith('.') and not rel_sub_dir.endswith('.lrdata'):
                        #print(rel_sub_dir)
                        sub_dir = os.path.join(project_dir, rel_sub_dir)
                        for path, subdirs, files in os.walk(sub_dir):
                            # iterate over every file
                            for file in files:
                                # skip hidden files, jpegs, and lightroom previews
                                if (not file.startswith('.')
                                    and not file.endswith('.jpg') 
                                    and not file.endswith('.xmp') 
                                    and not file.lower() == 'thumbs.db' 
                                    and not file.endswith('.lrprev')  
                                    and not file.endswith('.lrdata') 
                                    and not file.lower() == 'root-pixels.db'                                    
                                    and not file.lower() == 'previews.db'):
                                                                    
                                    # get the full path of each file currently
                                    long_file_path = os.path.join(path, file)
                                    
                                    ## Check for any meaningful info in the direct parent folder of the file  only for second run
                                    parent_name_tmp = os.path.basename(path)
                                    # replace any special characters with underscores
                                    parent_name = alpha_num.sub('_', parent_name_tmp)
                                    parent_name = parent_name.lower()
                                    # strip out the base name from the parent name.  It's redundant
                                    base_name_lwr = base_name.lower()
                                    parent_name = parent_name.replace(base_name_lwr, '')
                                    # strip any leading/trailing underscores
                                    parent_name = parent_name.lstrip('_')
                                    parent_name = parent_name.rstrip('_')
                                    # strip out the base name from the parent name.  It's redundant                                   
                                    #print(parent_name)
                                    # get rid of specific format folders
                                    if parent_name.endswith('raw'):
                                        parent_name = parent_name[:-3]
                                    if parent_name.endswith('tiff'):
                                        parent_name = parent_name[:-4]
                                    # replace any special characters with underscores
                                    short_file = alpha_num.sub('_', file)
				    # special fixes
                                    short_file = short_file.replace('Hildegarde_', 'Hildegard_')
                                    short_file = short_file.replace('Hildegarde_', 'Hildegard_')
                                    short_file = short_file.replace(base_name, '')
				    # special fixes
				    if base_name == ('Finley_1887'):
				        short_file = short_file.replace('Finky_1887_', 'aa_')
				    if base_name == ('Borelli_1680_1681'):
				        short_file = short_file.replace('Borelli_1680_', 'aa_')
				    if base_name == ('Nieremberg_1635'):
				        short_file = short_file.replace('raws_', 'aa_')
                                    # strip out the base name from the file name.  It's redundant
                                    # strip any leading/trailing underscores
                                    short_file = short_file.lstrip('_')
                                    short_file = short_file.rstrip('_')
                                    ## Fix some specific stuff in Galileo_1623
                                    if (project_dirs == 'Galileo_1623'
                                        and short_file.startswith('10_26_12__0')):
                                        short_file = short_file.replace('10_26_12__0', '')
                                    ## Fix some specific stuff in Grassi_1619
                                    if (project_dirs == 'Grassi_1619'
                                        and short_file.startswith('Galileo_1618_')):
                                        short_file = short_file.replace('Galileo_1618_', '')
                                    ## Fix some specific stuff in Sacrobosco_1490
                                    if (project_dirs == 'Sacrobosco_1490'
                                        and short_file.startswith('Bosco_1490_')):
                                        short_file = short_file.replace('Bosco_1490_', '')
                                    ## Fix some specific stuff in Ptolemy_1496
                                    if (project_dirs == 'Ptolemy_1496'
                                        and short_file.startswith('Regiomontanus_1496_')):
                                        short_file = short_file.replace('Regiomontanus_1496_', '')
                                    #specific tweak requested by barb
                                    short_file = short_file.replace('Galileo2_', '')
                                    short_file = short_file.replace('Abraham_', '')
                                    short_file = short_file.replace('AbrahambarHiyya', 'barHiyya')
                                    short_file = short_file.replace('Newton_1687_', '')
                                    short_file = short_file.replace('Riccioli_1651_', '')
                                    short_file = short_file.replace('Kircheri_1667_','')
                                    short_file = short_file.replace('Asistarchus_1572_','')
                                    short_file = short_file.replace('Allen_Triantaphillidou_2011_','')
                                    output_dir = output_dir.replace('dAviso_1656', 'dAviso_1665')

                                    #print(short_file)
                                    # join the remaining parent name with the short file name
                                    ## Again, just for a second pass
                                    #short_file = os.path.join(parent_name, file)
                                    # get the new full path of each file
                                    short_file_path = os.path.join(output_dir, short_file)
                                    try:
                                        print('    old: ' + long_file_path)
                                    except Exception:
                                        pass
                                    try:
                                        print('    new: ' + short_file_path)
                                    except Exception:
                                        pass
                                    try:
                                        # Comment out the following line for safe mode
                                        os.renames(long_file_path, short_file_path)
                                        
                                        # Need a noop here to make safe mode work 
                                        pass
                                    except Exception:
					print( "NOPE!")
                                        pass
#PATH_STR = r'\\norfile.net.ou.edu\UL-DIGILAB\Workspace\Workspace_HoS-digilab\Projects completed'
OUTPUT_STR = r'/srv/temp/'
PATH_STR = r'/srv/workspace/Ready to Script/'
PATH = os.path.abspath(PATH_STR)

rejigger_file_structure(PATH)
