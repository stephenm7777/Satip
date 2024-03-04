import datasets

s3 = datasets.filesystems.S3FileSystem(anon=True)  
print(s3.ls('noaa-goes16/'))