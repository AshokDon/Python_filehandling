import csv
import os
import pandas
with open('tech1.csv','r') as f1:
    data=list(csv.reader(f1))
result=0
result1=0
result2=0
def Count_Student():
    global result
    result=ACOE()
    print('ACOE->',result)
    global result1
    result1=AEC()
    print('AEC->',result1)
    global result2
    result2=ACET()
    print('ACET->',result2)
def ACOE():
    acoe_c_count=0
    acoe_p_count=0
    acoe_j_count=0
    for i in range(len(data)):
        if data[i][4]=="Aditya College of Engineering" and data[i][7]=="C programing":
            acoe_c_count+=1
        elif data[i][4]=="Aditya College of Engineering" and data[i][7]=="Python":
            acoe_p_count+=1
        elif data[i][4]=="Aditya College of Engineering" and data[i][7]=="Java":
            acoe_j_count+=1
    return acoe_c_count,acoe_p_count,acoe_j_count
            
def AEC():
    ace_c_count=0
    ace_p_count=0
    ace_j_count=0
    for i in range(len(data)):
        if data[i][4]=="Aditya Engineering College" and data[i][7]=="C programing":
            ace_c_count+=1
        elif data[i][4]=="Aditya Engineering College" and data[i][7]=="Python":
            ace_p_count+=1
        elif data[i][4]=="Aditya Engineering College" and data[i][7]=="Java":
            ace_j_count+=1
    return ace_c_count,ace_p_count,ace_j_count
def ACET():
    acet_c_count=0
    acet_p_count=0
    acet_j_count=0
    for i in range(len(data)):
        if data[i][4]=="Aditya College of Engineering and Technology" and data[i][7]=="C programing":
            acet_c_count+=1
        elif data[i][4]=="Aditya College of Engineering and Technology" and data[i][7]=="Python":
            acet_p_count+=1
        elif data[i][4]=="Aditya College of Engineering and Technology" and data[i][7]=="Java":
            acet_j_count+=1
    return acet_c_count,acet_p_count,acet_j_count
Count_Student()

df=pandas.DataFrame({})
