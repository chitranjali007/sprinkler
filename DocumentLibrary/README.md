This API helps in following:

1. Save file in filesystem manner
2. Save file in s3 bucket
3. Save file in sqlite
4. get files from filesystem
5. get file from s3 bucket
6. get file from sqlite
7. Perform operations such as rename, modify, delete, get file attribute etc.

How to install
Step 1: Go to dist folder
Step 2: pip install file_ops_lib-0.1.0-py3-none-any.whl
How To Use:
>> from file_ops_lib import file_filestorage
>> fr=open('test.txt','rb') #test.txt should be in the current working directory
>> save_filestorage.save_localfile(fr,Any folder location)
>> fr.close()

similary use for other functions

Following are descriptions of the methods defined in the library:- 
************************************************************************
>> save_localfile(file, to_folder)
It stores the files in current directory to the 'to_folder'
Arguments:
1. file - requires binary data. takes argument in Binary format. (eg: open('filename','rb'))
2. to_folder - destination folder where you wish to store 'file' (eg: "C:\Program Files")
************************************************************************
>> modify_localfile(file, to_folder)
It modifies/replaces the current file in 'to_folder'. Suppose you have made changes in 'file' and wish to replace the old version of 'file' in to_folder you may use this function
Arguments:
1. file - requires binary data of new file version. takes argument in Binary format.  i.e. open('filename','rb')
2. to_folder - destination folder where you wish to modify/replace'file' . takes argument in STRING format (eg: "C:\Program Files")
************************************************************************
>> rename_localfile(oldfname,newfname,src):
It renames the 'file' in location 'src'.
Arguments:
1. oldfname - current filename of file to be renamed. takes argument in STRING format (Eg: 'test.txt' or 'image.jpg')
2. newfname -   New filename . takes argument in STRING format (Eg: 'test.txt' or 'image.jpg')
3. src - Folder path of oldfname file . takes argument in STRING format (eg: "C:\Program Files")
************************************************************************
>> del_localfile(fname,src):
It deletes the file with name 'fname' in location 'src'.
Arguments:
1. fname - Name of file to be deleted. STRING format (Eg: 'test.txt' or 'image.jpg')
2. src - Folder path of file. STRING format (eg: "C:\Program Files")
************************************************************************
>> get_localfile_att(filename,to_folder):
It gets the attributes of file with name 'filename' such as size, creation time, last modification time.
Arguments:
1. filename: Name of file. Takes argument in STRING format (Eg: 'test.txt' or 'image.jpg')
2. to_folder: Folder path of current location of file. Takes argument in STRING format (eg: "C:\Program Files")
************************************************************************
>> save_s3_bucket(file,bucket_name,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)
Saves/Uploads file in current folder to s3 bucket with name 'bucket_name'
Arguments:
1. file - requires binary data. takes argument in Binary format. (eg: open('filename','rb'))
2. bucket_name - Name of your s3 bucket where you wish to store the file. takes argument in STRING format (Eg: chitrabucket)
3. AWS_ACCESS_KEY - AWS access key
4. AWS_SECRET_ACCESS_KEY - AWS secret access key
************************************************************************
>> get_s3_bucket(filename, bucket_name,dst,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)
Downloads the file with name 'filename' in current directory
Arguments:
1. filename - Name of file to be downloaded from s3 bucket. Takes argument in STRING format (Eg: 'test.txt' or 'image.jpg')
2. bucket_name - Name of your s3 bucket where you wish to store the file. takes argument in STRING format (Eg: chitrabucket)
3. AWS_ACCESS_KEY - AWS access key. Takes argument in STRING format 
4. AWS_SECRET_ACCESS_KEY - AWS secret access key. Takes argument in STRING format 
************************************************************************
>> rename_s3file(oldfname,newfname,bucket_name,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)
Renames the file with name 'oldfname' to 'newfname' in s3 bucket
Arguments:
1. oldfname - current filename of file to be renamed. takes argument in STRING format (Eg: 'test.txt' or 'image.jpg')
2. newfname -   New filename . takes argument in STRING format (Eg: 'test.txt' or 'image.jpg')
3. bucket_name - Name of your s3 bucket where you wish to store the file. takes argument in STRING format (Eg: chitrabucket)
4. AWS_ACCESS_KEY - AWS access key. Takes argument in STRING format 
5. AWS_SECRET_ACCESS_KEY - AWS secret access key. Takes argument in STRING format 
************************************************************************
>> del_s3file(fname,bucket_name,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)
Deletes file with name 'fname' in s3 bucket
Arguments:
1. fname: Name of file to be deleted. STRING format (Eg: 'test.txt' or 'image.jpg')
2. bucket_name - Name of your s3 bucket where you wish to store the file. takes argument in STRING format (Eg: chitrabucket)
3. AWS_ACCESS_KEY - AWS access key. Takes argument in STRING format 
4. AWS_SECRET_ACCESS_KEY - AWS secret access key. Takes argument in STRING format 
************************************************************************
>> get_s3file_att(filename,bucket_name,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)
It gets the attributes of file in s3 bucket with name 'filename' such as size, creation time, last modification time.
Arguments:
1. filename: Name of file. Takes argument in STRING format (Eg: 'test.txt' or 'image.jpg')
2. bucket_name - Name of your s3 bucket where you wish to store the file. takes argument in STRING format (Eg: chitrabucket)
3. AWS_ACCESS_KEY - AWS access key. Takes argument in STRING format 
4. AWS_SECRET_ACCESS_KEY - AWS secret access key. Takes argument in STRING format 
************************************************************************
>> modify_s3_bucket(file,bucket_name,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)
It modifies/replaces the current file in s3 bucket. It uploads the new version of 'file'
Arguments:
1. file: Modifies file. requires binary data. takes argument in Binary format. (eg: open('filename','rb'))
2. bucket_name - Name of your s3 bucket where you wish to store the file. takes argument in STRING format (Eg: chitrabucket)
3. AWS_ACCESS_KEY - AWS access key. Takes argument in STRING format 
4. AWS_SECRET_ACCESS_KEY - AWS secret access key. Takes argument in STRING format 
************************************************************************
>> save_sqlitee(file)
Stores file in sqlite DB. It creates DB and table in current folder where the library is being utilized.
Arguments:
1. file : File to be stored in DB. takes argument in Binary format. (eg: open('filename','rb'))
************************************************************************
>> get_sqlitee(filename,src):
Extracts file with name 'filename' from DB into folder with path 'src'
Arguments:
1. filename: Name of file to be extracted. Takes argument in STRING format (Eg: 'test.txt' or 'image.jpg')
2. src: destination folder where you wish to store 'file' (eg: "C:\Program Files")
************************************************************************
>> get_sqlitee_attr(filename)
It gets the attributes of file in sqlite DB with name 'filename' such as size, creation time, last modification time.
Arguments:
1. filename: Name of file. Takes argument in STRING format (Eg: 'test.txt' or 'image.jpg')
************************************************************************
>> del_sqlitee(filename)
It deletes the file with name 'filename' in sqlite DB.
Arguments:
1. filename: Name of file to be deleted. Takes argument in STRING format (Eg: 'test.txt' or 'image.jpg')