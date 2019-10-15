import json


#Ask user for a path to the json file
file = input("input the path and name of the json file:")
filename=file
data_s=open(file)
data =json.load(data_s)
data_s.close()
print(data)

#Serialization and Deserialization 

def serialize(data):
    data_type = type(data)
    if data_type is list:
        res = "list|"
        for item in data:
            res = res + str(item)
            res = res + ","
            res = res + str(type(item))
            res = res + "|"
        return res[:-1]

    elif data_type is dict:
        res = "dict|"
        for item in data:
            res = res + str(item)
            res = res + ":"
            res = res + str(data[item])
            res = res + ","
            res = res + str(type(data[item]))
            res = res + "|"
        return res[:-1]

def deserialize(data1):
    list_of_str = data1.split("|")
    data_type = list_of_str[0]
    list_of_str = list_of_str[1:]
    if data_type == 'list':
        res = list()
        for string in list_of_str:
            item = string.split(",")
            value = item[0]
            value1 = item[1]

            if value1 == "<class 'int'>":
                res.append(int(value))
            elif value1 == "<class 'float'>":
                res.append(float(value))
            elif value1 == "<class 'str'>":
                res.append(value)
        return res

    elif data_type == 'dict':
        res = dict()
        for string in list_of_str:
            s_split = string.split(":")
            key = s_split[0]
            item = s_split[1]
            item = item.split(",")
            value = item[0]
            value1 = item[1]
            if value1 == "<class 'int'>":
                res[key] = int(value)
            elif value1 == "<class 'float'>":
                res[key] = float(value)
            elif value1 == "<class 'str'>":
                res[key] = value
        return res

 
#comparsion

def compare(d1,d2):
    if type(d1)!=type(d2):
        return False
    else:
        if isinstance(d1,list):
            if d1 == d2:
                return True
            else:
                return False
        if isinstance(d1,dict):
            if len(d1)!=len(d2):
                return False
            for key in d1:
                if key not in d2:
                    return False
                if d1[key]!=d2[key]:
                    return False
            return True


#convert data structure to string then write string to file
data1=serialize(data)
file_name=input("input the file name of the json file:")
f= open(file_name,'w')
f.write(data1)
f.close()


#read string back from file
f1 = open(file_name)
s_file=f1.read()
f1.close()


#pass to deserialization
deserialization_data = deserialize(s_file)


#compare data structure
if compare(data,deserialization_data):
    print('success!')
else:
    print('not success!')