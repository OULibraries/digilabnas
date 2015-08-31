#!/usr/bin/env python

import os
import re
import sys
import codecs
import argparse

# Regex match for any non-alphanumeric/non-dot character
alpha_num = re.compile('[^0-9a-zA-Z.]+')

# Project Skip List
skip_projects = ['']

# test function for file extensions and prefixes that we want to skip
def skip_kind(path):
    """Returns True if the path points to a kind of file that should be skipped, based on extensions (mostly). False otherwise"""
    low_file = os.path.basename(path).lower()
    if( low_file.startswith('.')
        or low_file.endswith('.lrdata')
        or low_file.endswith('.jpg') 
        or low_file.endswith('.xmp') 
        or low_file.endswith('.lrprev')  
        or low_file.endswith('.lrdata')
        or low_file.lower() == 'thumbs.db' 
        or low_file.lower() == 'root-pixels.db'                                    
        or low_file.lower() == 'previews.db'):
        return True
    else:
        return False

# returns full new path to file
def rejigger_path(OUT_STR, project_name, path):
    """Returns new path that a file should be moved to in the OUT_STR folder, under project_name"""


    # AD HOC adjustments to project name could go here
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

    # AD HOC adjustments to filenames could go here
    ###    
        
    return os.path.join(project_out, newpath)



def calculate_moves(OUT_STR, project_name, project_path):
    """ Returns a list of file moves in the form of (src,dest) tuples that should be performed on a project"""
    project_moves = []
    for path, subdirs, files in os.walk(project_path):
        for filename in files:
            filepath = os.path.join(path, filename)
            
            # We don't want some of the files
            if(skip_kind(filepath)):
                continue

            out_filepath = rejigger_path(OUT_STR, project_name, filepath)
            project_moves.append( (filepath, out_filepath) )
            
    # return list sorted by destination to improve reviewability
    project_moves.sort(key=lambda  x:x[1])

    return project_moves

    


        
def main():
    """Normalizes project filenames and paths in preparation for bagging"""
    # What game shall we play today??
    parser = argparse.ArgumentParser(description="Normalize filenames to clean up hierarchy priory to bagging." )
    parser.add_argument("--destroy", help="Set this flag to really move files.",action="store_true")
    parser.add_argument("--src", required="true", help="pre-bag project source folder")
    parser.add_argument("--dest", required="true", help="pre-bag project destination folder")
    args = parser.parse_args()

    IN_STR = args.src
    OUT_STR = args.dest

    # get the directories just under the one specified
    # these are the projects that we need to bag.
    for project_maybe in os.listdir(IN_STR):
        
        # skip things that don't look like projects or that we're
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

        # calculate moves
        project_moves = calculate_moves(OUT_STR, project_name, project_in)

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

