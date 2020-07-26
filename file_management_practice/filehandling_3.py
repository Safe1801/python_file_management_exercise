cities=['Karachi,\n','Kabul\n']

fileObj=open('cities.txt','a+') # append at the end of the file plus reading rights

fileObj.writelines(cities)

fileObj.close()





