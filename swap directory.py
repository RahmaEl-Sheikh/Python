# # Python3 code to demonstrate
# # swap of key and value

# # initializing dictionary
# RomaDicectory = {"value1": "key1", "value2": "key2", "value3": "key3", "value4": "key4", "value5": "key5"}

# # Printing original dictionary
# print ("Original dictionary is : ")
# print(RomaDicectory)

# print()
# RomaNewDir = {}
# for key, value in RomaDicectory.items():
#     if value in RomaNewDir:
# 	    RomaNewDir[value].append(key)
# else:
# 	RomaNewDir[value]=[key]

# # Printing new dictionary after swapping
# # keys and values
# print ("Dictionary after swapping is : ")
# print("keys: values")
# for i in RomaNewDir:
# 	print(i, " :", RomaNewDir[i])
# # def swapDir(dir):
# #     for value, key in RomaDicectory.items():
# #         RomaDicectory [key] = value
# #     return RomaDicectory


# # print(f"After swapping:\n{swapDir(RomaDicectory )}")
# RomaDicectory={'val1': 'key1', 'val2': 'key2', 'val3': 'key3'}
# RomaNewDir = {}
# def get_swap_dict(RomaNewDir):
#     for key, value in RomaDicectory.items():
#         return RomaNewDir

# RomaNewDir_swap = get_swap_dict(RomaNewDir)
# print(RomaNewDir_swap)


RomaDicectory= {"key1": "Value1", "key2": "Value2", "key3": "Value3"}
print(f"Original Dictionary is:\n{RomaDicectory}")

RomaNewDir = {}


def swapDictionary(dict):
    for key, value in RomaDicectory.items():
        RomaNewDir[value] = key
    return RomaNewDir


print(f"After swapping:\n{swapDictionary(RomaDicectory)}")