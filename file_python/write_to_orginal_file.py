#If the file is too large to fit into memory,
# then write the lines to a temporary file 
#and then rename the file when you are done


# w 模式 如果文件已存在，那么返回文件对象前会清空文件
# o 添加模式 不会清空
import tempfile

def find_and_write(sstring,newstring,pathname):

	with open(pathname,'r') as fp, tempfile.TemporaryFile() as temp:
		count = 0
		for line in fp:
			if sstring  in line:
				count += 1
				line=line.replace(sstring,newstring)
				temp.write(line.encode())
		if count == 0:
			print ("%s is not found" % sstring)
			return 0
                #rewind temp to beginnig
		temp.seek(0)
		with  open(pathname,'w') as fp:

			for line in temp:
				fp.write(line.decode())
		print ("it is done")
		return 1
