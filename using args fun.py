def compine (*args):
    totalList=list()
    for li in args:
        if isinstance(li,list):
            totalList += li
    return totalList 

print(compine([1,2],[3,4,5],[6,7,8,9]))