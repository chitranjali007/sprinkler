import sys
sys.path.insert(1, 'C:/Users/CyberSec COE OL-2/Documents/DocumentLibrary/file_ops_lib')
import save_filestorage

AWS_BUCKET_NAME="bucket_name"
AWS_ACCESS_KEY="PUT AWS Access Key"
AWS_SECRET_ACCESS_KEY="Put AWS Secret"
AWS_DOMAIN="http://bucket_name.s3.amazonaws.com/"
TO_FOLDER="C:/Users/CyberSec COE OL-2/Documents/DocumentLibrary/UploadedDoc" #change this

print ("*****************************************************\n")
print ("Testing for save file in local storage")
print ("*****************************************************\n")
def test_save_localfile():
	print ("Test for ideal scenario i.e. Valid directory and non existing file")
	fr=open('testchitra.txt','rb')
	val=save_filestorage.save_localfile(fr,TO_FOLDER)
	if(val==0):
		print ("something went wrong")
	else:
		print ("File saved successfully")
	fr.close
	print ("Test for non ideal scenario i.e. In Valid directory")
	fr=open('testchitra.txt','rb')
	val=save_filestorage.save_localfile(fr,"C:/Non-Existing")
	if(val==0):
		print ("something went wrong")
	else:
		print ("File saved successfully")
	fr.close
	print ("Test for non ideal scenario i.e. ALready Existing file")
	fr=open('testchitra.txt','rb')
	val=save_filestorage.save_localfile(fr,TO_FOLDER)
	fr.close

#test_save_localfile()
print ("*****************************************************\n")
print ("Testing for Modify file in local storage")
print ("*****************************************************\n")
def test_modify_localfile():
	print ("Test for ideal scenario i.e. Valid directory and existing/non existing file")
	fr=open('testchitra.txt','rb')
	val=save_filestorage.modify_localfile(fr,TO_FOLDER)
	if(val==0):
		print ("something went wrong")
	else:
		print ("File modified successfully")
	fr.close
	print ("Test for non ideal scenario i.e. InValid directory")
	fr=open('testchitra.txt','rb')
	val=save_filestorage.modify_localfile(fr,"C:/Non-Existing")
	fr.close
#test_modify_localfile()

print ("*****************************************************\n")
print ("Testing for Rename file in local storage")
print ("*****************************************************\n")
def test_rename_localfile():
	print ("Test for ideal scenario i.e file and folder exist and file with new name does not already exist")
	save_filestorage.rename_localfile('testchitra.txt',"chitratest.txt",TO_FOLDER)
	print ("Test for non ideal scenario i.e file to be renamed does not exist")
	save_filestorage.rename_localfile('testchitra.txt',"chitratest.txt",TO_FOLDER)

#test_rename_localfile()
print ("*****************************************************\n")
print ("Testing for Delete file in local storage")
print ("*****************************************************\n")
def test_del_localfile():
	print ("Ideal Scenario.File to be deleted exists")
	save_filestorage.del_localfile("24-https.pptx",TO_FOLDER)
	print ("Non Ideal Scenario. File to be deleted does not exist")
	save_filestorage.del_localfile("24-https.pptx",TO_FOLDER)

#test_del_localfile()
print ("*****************************************************\n")
print ("Testing for Get attributes of file in local storage")
print ("*****************************************************\n")
def test_get_localfile_att():
	print ("Ideal Scenario.File exists")
	save_filestorage.get_localfile_att('chitratest.txt',TO_FOLDER)
	print ("Non Ideal Scenario.File doesnt exists")
	save_filestorage.get_localfile_att('chitra2.txt',TO_FOLDER)

#test_get_localfile_att()
print ("*****************************************************\n")
print ("Testing for upload file in s3 bucket")
print ("*****************************************************\n")
def test_save_s3_bucket():
	print ("Ideal Scenario.File does not exist in s3 bucket")
	fr=open('testchitra.txt','rb')
	save_filestorage.save_s3_bucket(fr,AWS_BUCKET_NAME,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)
	fr.close()
	print ("Non Ideal Scenario.File already exist in s3 bucket")
	fr=open('testchitra.txt','rb')
	save_filestorage.save_s3_bucket(fr,AWS_BUCKET_NAME,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)
	fr.close()
#test_save_s3_bucket()

print ("*****************************************************\n")
print ("Testing for modify file in s3 bucket")
print ("*****************************************************\n")
def test_modify_s3_bucket():
	fr=open('testchitra.txt','rb')
	save_filestorage.modify_s3_bucket(fr,AWS_BUCKET_NAME,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)
	fr.close()

#test_modify_s3_bucket()
print ("*****************************************************\n")
print ("Testing for download file from s3 bucket")
print ("*****************************************************\n")
def test_get_s3_bucket():
	print ("Ideal Scenario. File exist")
	save_filestorage.get_s3_bucket("testchitra.txt", AWS_BUCKET_NAME,TO_FOLDER,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)
	print ("Non Ideal Scenario. File does not exist")
	save_filestorage.get_s3_bucket("testchitra1.txt", AWS_BUCKET_NAME,TO_FOLDER,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)

#test_get_s3_bucket()
print ("*****************************************************\n")
print ("Testing for get attributes of file in s3 bucket")
print ("*****************************************************\n")
def test_get_s3file_att():
	print ("Ideal Scenario. File exist")
	save_filestorage.get_s3file_att("test.txt",AWS_BUCKET_NAME,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)
	print ("Non Ideal Scenario. File does not exist")
	save_filestorage.get_s3file_att("test33.txt",AWS_BUCKET_NAME,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)

#test_get_s3file_att()
print ("*****************************************************\n")
print ("Testing for delete file in s3 bucket")
print ("*****************************************************\n")
def test_del_s3file():
	print ("Ideal Scenario.File Exists")
	save_filestorage.del_s3file("test.txt",AWS_BUCKET_NAME,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)
	print ("Non Ideal Scenario.File Does Not Exists")
	save_filestorage.del_s3file("test.txt",AWS_BUCKET_NAME,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)

#test_del_s3file()
print ("*****************************************************\n")
print ("Testing for rename file in s3 bucket")
print ("*****************************************************\n")
def test_rename_s3file():
	print ("Ideal Scenario.File Exists")
	save_filestorage.rename_s3file("testchitra.txt","chitra.txt",AWS_BUCKET_NAME,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)
	print ("Non Ideal Scenario.File Does Not Exists")
	save_filestorage.rename_s3file("testchitra.txt","chitra.txt",AWS_BUCKET_NAME,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)
#test_rename_s3file()

print ("*****************************************************\n")
print ("Testing for upload file in sqlite DB")
print ("*****************************************************\n")
def test_save_sqlitee():
	print ("Ideal scenario. File does not exist")
	fr=open('24-https.pptx','rb')
	save_filestorage.save_sqlitee(fr)
	fr.close()
	print ("Non ideal scenario. File already exist")
	fr=open('24-https.pptx','rb')
	save_filestorage.save_sqlitee(fr)
	fr.close()
#test_save_sqlitee()

print ("*****************************************************\n")
print ("Testing for get file from sqlite DB")
print ("*****************************************************\n")
def test_get_sqlitee():
	print ("Ideal Scenario.File Exists")
	save_filestorage.get_sqlitee('24-https.pptx',TO_FOLDER)
	print ("Non Ideal. File does not exist")
	save_filestorage.get_sqlitee('24-http.pptx',TO_FOLDER)

#test_get_sqlitee()
print ("*****************************************************\n")
print ("Testing for get file attr from sqlite DB")
print ("*****************************************************\n")
def test_get_sqlitee_attr():
	save_filestorage.get_sqlitee_attr('24-https.pptx')

test_get_sqlitee_attr()
print ("*****************************************************\n")
print ("Testing for delete file from sqlite DB")
print ("*****************************************************\n")
def test_del_sqlitee():
	save_filestorage.del_sqlitee_attr('24-https.pptx')

#test_del_sqlitee_attr()