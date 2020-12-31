import os,time
import boto3
import botocore
from os import path
import datetime
import sqlite3
import sys

def save_localfile(file, to_folder):
	if os.path.isdir(to_folder):
		floc=os.path.join(to_folder,file.name)
		if path.exists(floc):
			print ("File of name %s already exists, please choose different filename or use method modify_localfile" % file.name)
			return 0
		fw=open(floc,'wb')
		fw.write(file.read())
		fw.close()
		return 1
	else:
		print ('%s does not exist. Please check...' % to_folder)
		return 0

def modify_localfile(file, to_folder):
	if os.path.isdir(to_folder):
		floc=os.path.join(to_folder,file.name)
		fw=open(floc,'wb')
		fw.write(file.read())
		fw.close()
		return 1
	else:
		print ('%s does not exist. Please check...' % to_folder)
		return 0

def rename_localfile(oldfname,newfname,src):
	oldloc=os.path.join(src,oldfname)
	newloc=os.path.join(src,newfname)
	if path.exists(newloc):
		print('File of this name already exists. Please choose different name')
		return 0
	if path.exists(oldloc):
		os.rename(oldloc,newloc)
		print("Rename Successfull...")
		return 1	
	else:
		print("file or folder does not exist")
		return 0

def del_localfile(fname,src):
	floc=os.path.join(src,fname)
	if path.exists(floc):
		os.remove(floc)
		print("File %s removed" % fname)
		return 1
	else:
		print("file or folder does not exist")
		return 0

def get_localfile_att(filename,to_folder):
	fullpath=os.path.join(to_folder,filename)
	if path.exists(fullpath):
		print("Attributes of: %s" %filename)
		print("Creation Time: %s" % time.ctime(os.path.getctime(fullpath)))
		print("Last Modification Time: %s" % time.ctime(os.path.getmtime(fullpath)))
		print("Size: %s" % os.stat(fullpath).st_size)
		return 1
	else:
		print ("File %s does not exists" % filename)
		return 0
	
def rename_s3file(oldfname,newfname,bucket_name,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY):
	s3 = boto3.resource('s3',aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
	try:
		s3.Object(bucket_name, oldfname).load()
	except botocore.exceptions.ClientError as e:
		if (e.response['Error']['Code'] == '404'):
			print('Destination file does not exist')
			return
	s3.Object(bucket_name,newfname).copy_from(CopySource=bucket_name+'/'+oldfname)
	s3.Object(bucket_name,oldfname).delete()

def del_s3file(fname,bucket_name,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY):

	s3 = boto3.resource('s3',aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
	try:
		s3.Object(bucket_name, fname).load()
	except botocore.exceptions.ClientError as e:
		if (e.response['Error']['Code'] == '404'):
			print('Destination file does not exist')
			return 0
	s3.Object(bucket_name,fname).delete()
	print ('file deleted successfully')
	return 1

def get_s3file_att(filename,bucket_name,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY):
	try:
		s3 = boto3.client("s3",aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
		metadata=s3.head_object(Bucket=bucket_name, Key=filename)
	except botocore.exceptions.ClientError as e:
		if (e.response['Error']['Code'] == '404'):
			print('File does not exist')
		else:
			raise
	else:
		print("Attributes of: %s" %filename)
		print("Last modified date: %s" % metadata['LastModified'])
		print("Size: %s"  % metadata['ContentLength'])

def get_s3_bucket(filename, bucket_name,dst,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY):
	s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
	try:
		s3.head_object(Bucket=bucket_name, Key=filename)
	except botocore.exceptions.ClientError as e:
		if (e.response['Error']['Code'] == '404'):
			print('File does not exist')
			return 0
		else:
			raise
	else:
		s3.download_file(bucket_name, filename, os.path.join(dst,filename))
		return 1

def save_s3_bucket(file,bucket_name,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY):
	s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
	try:
		s3.head_object(Bucket=bucket_name, Key=file.name)
	except botocore.exceptions.ClientError as e:
		if (e.response['Error']['Code'] == '404'):
			s3.upload_fileobj(file, bucket_name, file.name)
			print ('file uploaded to s3 successfully')
			return 1
		else:
			raise
	else:
		print("The file already exists. Chose different name")
		return 0

def modify_s3_bucket(file,bucket_name,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY):
	s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
	s3.upload_fileobj(file, bucket_name, file.name)
	return 1
		
def save_sqlitee(file):
	doc=file.read()
	doc_name=file.name
	doc_size=os.stat(file.name).st_size
	doc_ctime=os.stat(file.name).st_ctime
	curr_time=datetime.datetime.now()
	print (doc_name)
	sqliteConnection = sqlite3.connect("filedb.db")
	try:
        	
        	cursor = sqliteConnection.cursor()
        	print("Connected to SQLite")
        	sqlite_table_create_query = """CREATE TABLE IF NOT EXISTS docu_store (document_name STRING, document BLOB,ctime STRING,size INTEGER,mtime datetime)"""
        	cursor.execute(sqlite_table_create_query)
        	cursor.execute("SELECT count(*) FROM docu_store WHERE document_name = ?", (doc_name,))
        	data=cursor.fetchone()[0]
        	if data!=0:
        		print('File already exists')
        		return 0
        	sqlite_insert_blob_query = """INSERT INTO docu_store VALUES (?,?,?,?,?)"""
        	cursor.execute(sqlite_insert_blob_query, (doc_name,doc,doc_ctime,doc_size,curr_time))
        	sqliteConnection.commit()
        	cursor.close()
	except sqlite3.Error as error:
        	print("Failed to insert blob data into sqlite table", error)
	finally:
			if (sqliteConnection):
				sqliteConnection.close()
			print("the sqlite connection is closed")

def get_sqlitee(filename,src):
	try:
        	sqliteConnection = sqlite3.connect("filedb.db")
        	cursor = sqliteConnection.cursor()
        	print("Connected to SQLite")
        	sqlite_fetch_blob_query = """SELECT * FROM docu_store WHERE document_name=?"""
        	#print("selected")
        	cursor.execute(sqlite_fetch_blob_query, (filename,))
        	#print("executed")
        	try:
        		record=cursor.fetchall()
        		#print (record)
        	#print (record)
        		
        		if (len(record)==0):
        			print ("File does not exist")
        			return 0
        		for row in record:
        			docu_name=row[0]
        			document=row[1]
        			doc_size=row[2]
        			doc_ctime=row[3]
        			doc_mtime=row[4]
        		#print (docu_name,document)
        			fw=open(os.path.join(src,docu_name),'wb')
        			fw.write(document)
        		#print("written... check location")
        			fw.close()	
        		cursor.close()
        		return 1
        	except:
        		print ("File does not exist")
        		return 0
        	cursor.close()
	except sqlite3.Error as error:
        	print("Failed to fetch blob data from sqlite table", error)
	finally:
		if (sqliteConnection):
            		sqliteConnection.close()
		print("the sqlite connection is closed")

def get_sqlitee_attr(filename):
	try:
        	sqliteConnection = sqlite3.connect("filedb.db")
        	cursor = sqliteConnection.cursor()
        	print("Connected to SQLite")
        	sqlite_fetch_blob_query = """SELECT * FROM docu_store WHERE document_name=?"""
        	print("selected")
        	cursor.execute(sqlite_fetch_blob_query, (filename,))
        	#print("executed")
        	try:
        		record=cursor.fetchall()
        		#print (record)
        	#print (record)
        		
        		if (len(record)==0):
        			print ("File does not exist")
        			return 0
        		for row in record:
        			docu_name=row[0]
        			document=row[1]
        			doc_size=row[3]
        			doc_ctime=row[2]
        			doc_mtime=row[4]
        		#print (docu_name,document)
        			print ('Attributes of file are:')
        			print ('Document Size:%s' % doc_size)
        			#print ('Document Creation Time:%s' % doc_ctime)
        			print ('Document Last Modification Time:%s' % doc_mtime)
        		#print("written... check location")
        			fw.close()	
        		cursor.close()
        		return 1
        	except:
        		print ("File does not exist")
        		return 0
        	cursor.close()
	except sqlite3.Error as error:
        	print("Failed to fetch blob data from sqlite table", error)
	finally:
		if (sqliteConnection):
            		sqliteConnection.close()
		print("the sqlite connection is closed")

def del_sqlitee(filename):
	try:
        	sqliteConnection = sqlite3.connect("filedb.db")
        	cursor = sqliteConnection.cursor()
        	print("Connected to SQLite")
        	sqlite_fetch_blob_query = """SELECT * FROM docu_store WHERE document_name=?"""
        	print("selected")
        	cursor.execute(sqlite_fetch_blob_query, (filename,))
        	record=cursor.fetchall()
        	if (len(record)==0):
        			print ("File does not exist")
        			return 0
        	cursor.execute("DELETE FROM docu_store WHERE document_name = ?", (filename,))
        	sqliteConnection.commit()
        	return 1
        	cursor.close()
	except sqlite3.Error as error:
        	print("Failed to fetch blob data from sqlite table", error)
	finally:
		if (sqliteConnection):
            		sqliteConnection.close()
		print("the sqlite connection is closed")

#fr=open('test.txt','rb')
#save_httpfile(fr,TO_FOLDER)
#save_s3_bucket(fr,AWS_BUCKET_NAME)
#save_sqlitee(fr)
#fr.close
#save_localfile('Passport.jpeg',TO_FOLDER)
#get_localfile_att('README.md',TO_FOLDER)
#get_s3_bucket('test.txt', AWS_BUCKET_NAME,TO_FOLDER)
#get_s3file_att('test.txt',AWS_BUCKET_NAME)
#rename_localfile('test.txt','chitra.txt',TO_FOLDER)
#del_localfile('chitra.txt',TO_FOLDER)
#rename_s3file('test1.txt','chitra.txt',AWS_BUCKET_NAME)
#del_s3file('chitra.txt',AWS_BUCKET_NAME)
#get_sqlitee('test.txt')