#set={1,2,3,4,5,6,}
#print(12 in set)
#print(2 in set)
#print(34 in set)
names={"abc","bdcd","ghtt","abc","ghhutgt","ggutxw","abc","ghtt","bdcd"}
print(set(names))
names.add("ramya")
print(names)
names.remove("ghtt")
print(names)
set2=names.copy()
print(set2)
seta={2,4,6,8,10,12,14,16,18,20}
setb=(1,3,4,5,7,9,11,13,15,17,19)
setc=seta.union(setb)
print(setc)