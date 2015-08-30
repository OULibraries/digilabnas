#!/usr/bin/env python

import os
import re
import sys
import codecs
import argparse

# Regex match for any non-alphanumeric/non-dot character
alpha_num = re.compile('[^0-9a-zA-Z.]+')

# Project Skip List
skip_projects = ['Clavius_1570']

# test function for file extensions and prefixes that we want to skip
def skip_kind(path):
    low_fn = os.path.basename(path).lower()
    if( low_fn.startswith('.')
        or low_fn.endswith('.lrdata')
        or low_fn.endswith('.jpg') 
        or low_fn.endswith('.xmp') 
        or low_fn.endswith('.lrprev')  
        or low_fn.endswith('.lrdata')
        or low_fn.lower() == 'thumbs.db' 
        or low_fn.lower() == 'root-pixels.db'                                    
        or low_fn.lower() == 'previews.db'):
        return True
    else:
        return False

# returns full new path to file
def rejigger_path(OUT_STR, project_name, path):


    # AD HOC adjustments to project name can go here
    ###
    
    project_out = os.path.join(OUT_STR, project_name)

    newpath = os.path.basename(path)
    newpath = newpath.lower()
    newpath = alpha_num.sub('_', newpath)    
    newpath = newpath.replace(project_name.lower(), '')

    newpath = newpath.lstrip('_')
    newpath = newpath.rstrip('_')

    if (newpath.endswith('.tiff')):
        newpath = newpath[:-1]
    
    if (newpath.endswith('.lrcat')):
        newpath = 'lrcat.lrcat'

    if(not newpath):
        newpath = "EMPTY"

    # AD HOC adjustments to filenames can go here
    ###    
        
    return os.path.join(project_out, newpath)
        
def main():

    # What game shall we play today??
    parser = argparse.ArgumentParser(description="Normalize filenames to clean up hierarchy priory to bagging." )
    parser.add_argument("--destroy", help="Set this flag to move files around.",action="store_true")
    args = parser.parse_args()


    # Set up input and output folders
    IN_STR = r'/Users/lmc/Projects/opt-digilabnas-bin/srv/workspace/Ready to Script'
    OUT_STR = r'/Users/lmc/Projects/opt-digilabnas-bin/srv/temp'    

    
    # get the directories just under the one specified
    # these are the projects that we need to bag.
    for project_maybe in os.listdir(IN_STR):
        
        # skip things taht don't look like projects or that we're
        # specifically skipping
        if ( skip_kind(project_maybe)
             or project_maybe in skip_projects):
            continue

        # Also skip anything that isn't a directory, because all
        # projects are directories
        project_in =os.path.join(IN_STR, project_maybe) 
        if (not os.path.isdir(project_in)):
            continue
            
        # If we haven't skipped it at this point, we assume that it's
        # a project and set it up as one. 
        project_name = alpha_num.sub('_', project_maybe)
        print "BEGIN PROJECT:", project_name

        project_moves = []

        # We'll get all of the files in the project
        for path, subdirs, files in os.walk(project_in):
            for filename in files:
                filepath = os.path.join(path, filename)

                # We don't want some of the files
                if(skip_kind(filepath)):
                    continue
                out_filepath = rejigger_path(OUT_STR, project_name, filepath)

                project_moves.append( (filepath, out_filepath) )

        # sort by destination to improve reviewability
        project_moves.sort(key=lambda  x:x[1])
                

        moved=[]
        for src,dest in project_moves:

            print  "%s <--- %s" % (dest,src )

            # keep track of where we're moving things in case of data
            # loss we want to print all file moves, and not have to
            # deal with finding problems one at a time, so do this as
            # a review step and not when createing the list
            if dest in moved:
                print ">>>> WARNING: multiple files moved to:%s" %(dest)
            if dest.endswith("EMPTY"):
                print ">>>> WARNING: nothing retained in filename, using %s" %(dest)

            moved.append(dest)

            if (args.destroy) :
                try:
                    os.renames( move[0], move[1])
                except Exception:
		    print( "NOPE! Unable to rename.")

                        
        print "END PROJECT:", project_name
        print ""
    
if __name__ == "__main__":
    main()
