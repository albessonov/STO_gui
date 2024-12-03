import os
import subprocess
os.chdir("pillows")
TTF_SIDE_ARR=[]
SRES_SIDE_ARR=[]
TTF_DPT_PPT_ARR=[]
SRES_FRONT_ARR=[]
TTF_DAB_ARR=[]
TTF_PAB_ARR=[]
subprocess.call("arrays.txt", shell=True)
lines=['','','','','','']
file=open("arrays.txt",'r')
for i in range(0,6):
    line=file.readline()
    line=line.split('=')
    if('\n' in line[1]):
        line[1]=line[1].replace('\n','')
    lines[i]=line[1]
print(lines)
for i in range(len(lines[0].split(','))):
    TTF_SIDE_ARR.append(int(round(float(lines[0].replace('[','').replace(']','').split(',')[i])/0.01)))
print(TTF_SIDE_ARR)
for i in range(len(lines[1].split(','))):
    SRES_SIDE_ARR.append(int(round(float(lines[1].replace('[','').replace(']','').split(',')[i])/10e-9)))
print(SRES_SIDE_ARR)
for i in range(len(lines[2].split(','))):
    TTF_DPT_PPT_ARR.append(int(round(float(lines[2].replace('[','').replace(']','').split(',')[i])/0.01)))
print(TTF_DPT_PPT_ARR)
for i in range(len(lines[3].split(','))):
    SRES_FRONT_ARR.append(int(round(float(lines[3].replace('[','').replace(']','').split(',')[i])/10e-9)))
print(SRES_FRONT_ARR)
for i in range(len(lines[4].split(','))):
    TTF_DAB_ARR.append(int(round(float(lines[4].replace('[','').replace(']','').split(',')[i])/0.01)))
print(TTF_DAB_ARR)
for i in range(len(lines[5].split(','))):
    TTF_PAB_ARR.append(int(round(float(lines[5].replace('[','').replace(']','').split(',')[i])/0.01)))
print(TTF_PAB_ARR)
file.close()
os.chdir("..")
