
file = open("namelist_of_No_hand_in.TXT", "r")  # 以只读模式读取文件
lines = []
for i in file:
    lines.append(i)  # 逐行将文本存入列表lines中
file.close()
new = []
for line in lines:  # 逐行遍历
    p = 0  # 定义计数指针
    for bit in line:  # 对每行进行逐个字遍历
        if bit == ".":  # 遇到空格时进行处理
            new.append(line[0:p])  # 将line中的0：p字段存入新列表new中，用于写入新的.txt中
            break  # 处理完一行后跳出当前循环
        else:
            p = p + 1  # 如果bit不是空格，指针加一
 
# 以写的方式打开文件，如果文件不存在，就会自动创建，如果存在就会覆盖原文件
file_write_obj = open("namelist_of_No_hand_in.TXT", 'w')
for var in new:
    file_write_obj.writelines(var)
    file_write_obj.writelines('\n')
file_write_obj.close()


file = open("namelist_of_No_hand_in.TXT", "r")  # 以只读模式读取文件
lines = []
for i in file:
    lines.append(i)  # 逐行将文本存入列表lines中
file.close()
# print(lines)
all_class = [
"陈广振\n",
"李方苏\n",
"黄小睿\n",
"陈涛铭\n",
"许依青\n",
"刘琳琳\n",
"何思桦\n",
"潘鑫城\n",
"方晶晶\n",
"王梓洋\n",
"王心昊\n",
"李浩楠\n",
"张译文\n",
"邓朝琳\n",
"刘锦江\n",
"王嘉诚\n",
"张艺馨\n",

"刘子琦\n",
"张艺凡\n",
"蒋佳桐\n",
"朱江鸿\n",
"向婷婷\n",
"王思慧\n",
"陈泽润\n",
"韩良栋\n",

"韩珊\n",
"蔡文\n",

"朱丹\n",
"张驰\n",
"张宇\n"
]
file_write_obj = open("namelist_of_No_hand_in.TXT", 'w')
for var in all_class:
    if var not in lines:
        file_write_obj.writelines(var)
        file_write_obj.writelines('\n')

file_write_obj.close()