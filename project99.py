import os
import time
import shutil
def main():
    deletedfilecount=0
    deletedfoldercount=0    
    path1 ='C:/Users/aines/Desktop/testfolder'
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path1):
        for rootfolder,folder,files in os.walk(path1):
            if seconds>=folderage(rootfolder):
                removefolder(rootfolder)
                deletedfoldercount=deletedfoldercount+1
                break 
            else:
                for x in folder:
                    folderpath=os.path.join(rootfolder,x)
                    if seconds>=folderage(folderpath):
                        removefolder(folderpath)
                        deletedfoldercount=deletedfoldercount+1
                        break 
                for file1 in files:
                    filepath=os.path.join(rootfolder,file1)
                    if seconds>=folderage(filepath):
                        removefile(filepath)
                        deletedfilecount=deletedfilecount+1
        else:
            if seconds>=folderage(path1):
                removefile(path1)
                deletedfilecount=deletedfilecount+1
    else:
        print('Path was not found.')  
    print(f"Total folders deleted: {deletedfoldercount}") 
    print(f"Total files deleted: {deletedfilecount}")                 

def folderage(path1):
    ctime=os.stat(path1).st_ctime
    return(ctime)
def removefile(path1):
    if not os.remove(path1):
        print('{path1}'+'is removed successfully')
    else:
        print('Unable to delete'+'{path}')    
def removefolder(path1):
    if not shutil.rmtree(path1):
        print('{path1}'+'is removed successfully')
    else:
        print('Unable to delete'+'{path1}')       
main()             








