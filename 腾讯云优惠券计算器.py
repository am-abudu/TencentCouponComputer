
"""
     腾讯云优惠券计算器 by Abudu 
           _               _       
     /\   | |             | |      
    /  \  | |__  _   _  __| |_   _ 
   / /\ \ | '_ \| | | |/ _` | | | |
  / ____ \| |_) | |_| | (_| | |_| |
 /_/    \_\_.__/ \__,_|\__,_|\__,_|   

"""



from math import ceil,floor
from os import system

p = floor(float(input("需续费价格(人民币):")))
w = floor(float(input("最低付费:")))
count = 0

saver = input("是否保存结果至LightHouse.txt?(y/n):")
if saver == "y":
    f = open('LightHouse.txt', 'w')
    f.write("需续费价格(人民币):" + str(p) + "\n")
    f.write("最低付费:" + str(w) + "\n")

prices = [
    [24, "非大陆24元"],
    [34, "非大陆34元"],
    [40, "大陆40元"],
    [48, "非大陆Windows48元"],
    [50, "大陆50元"],
    [67, "非大陆67"],
    [68, "非大陆Windows68元"],
    [70, "大陆储存型70元"],
    [90, "大陆90元"],
    [105, "大陆储存型105元"],
    [121, "非大陆Windows121元"],
    [133, "非大陆133元"],
    [140, "大陆140元"],
    [150, "大陆储存型150元"],
    [239, "非大陆Windows239元"],
    [255, "大陆255元"],
    [266, "非大陆266元"],
    [300, "大陆储存型300元"],
    [350, "大陆350元"],
    [465, "非大陆Windows465元"],
    [532, "非大陆532元"],
    [788, "非大陆Windows788元"],
]

need = w - p
if need < 0:
    if saver == "y":
        f.write("错误，请检查数值")
    print("错误，请检查数值")
    system("pause")
    exit()
if need == 0:
    if saver == "y":
        f.write("无需计算，请直接使用")
    print("无需计算，请直接购买")
    system("pause")
    exit()

print("需计算" + str(need) + "元")

answer = ceil(need / 24) * 24 + p - w

List = list()


def out(data, t):
    dic = dict()
    for item in data:
        if dic.get(item):
            dic[item] = dic[item] + 1
        else:
            dic[item] = 1
    if saver == "y":
        f.write("- 需补充" + str(int(t)) + "元,方案: 购买")
    print("- 需补充" + str(int(t)) + "元,方案:", end=" 购买")
    for item in dic.keys():
        if saver == "y":
            f.write(str(dic[item]) + "月" + item)
        print(str(dic[item]) + "月" + item, end=" ")
    print()
    if saver == "y":
        f.write("\n")


def compute(n):
    global answer, count
    if n <= 0:
        return - n
    for price in prices:
        List.append(price[1])
        t = compute(n - price[0])
        if t is not None:
            if t <= answer:
                out(List, t)
                answer = t
                count += 1
        del List[-1]


compute(need)
print("计算完毕，共" + str(count) + "种优化方案")
if saver == "y":
    f.write("共" + str(count) + "种优化方案")
    f.close()
system("pause")
