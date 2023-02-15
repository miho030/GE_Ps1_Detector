# _*_ coding:utf-8 _*_
import re
import os

def _ScanPs1_Mug(strMalDir):
    list_Infected = []
    list_Benign = []

    arr = os.listdir(strMalDir)
    for i in arr:
        if(str(i).find(".ps1")>0):
            print(i)
            filename = i
            special_chars = ['$', '&', '|', '*', '?', '(', ')', '[', ']', '{', '}', '<', '>', ';', ',', '.', ':', '\'', '\"']

            char_count = {}
            total_chars = 0
            with open(strMalDir+"/"+filename, 'r', encoding="utf-8", errors='ignore') as f:
                for line in f:
                    total_chars += len(line)
                    for char in special_chars:
                        count = len(re.findall(re.escape(char), line))
                        if count > 0:
                            if char in char_count:
                                char_count[char] += count
                            else:
                                char_count[char] = count
            allchar_count=0
            for i in char_count:
                allchar_count += int(char_count[i])

            try:
                result = (allchar_count/total_chars) * 100
            except ZeroDivisionError:
                result = 0
            print(result)

            if(result > 2):
                print("virut ===== "+filename+"\n")
                list_Infected.append(filename)
            else:
                print("not virut (need more function detect) =="+filename)
                list_Benign.append(filename)

    return list_Infected, list_Benign