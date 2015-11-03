print("Loading file")
f = open('output_3.csv','r')
filedata = f.read()
f.close()
print("Finished loading file")
print("Replacing strings")
i = 0
newdata = filedata
while i <16:
	newdata = newdata.replace(" ; ;"," ;")
	i = i +1
newdata = newdata.replace("; ;",";")
newdata = newdata.replace(" ;","")
newdata=  newdata.replace('; "','"')

print("Finished replacing strings")
print("Printing file")
f = open('output_4.csv','w')
f.write(newdata)
f.close()
print("Finished printing file")
