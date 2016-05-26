#!/usr/bin/python
#coding:utf-8
import psutil,subprocess
#function of Get Memory    
def getMemorystate(): 
        phymem = psutil.virtual_memory()
        line =[
            phymem.percent,
            int(phymem.used/1024/1024),
            int(phymem.total/1024/1024)
            ]
        return line
if __name__=="__main__":
    p = subprocess.Popen('wmic DISKDRIVE get Caption,size,InterfaceType', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print p.stdout.read()
    retval = p.wait()
