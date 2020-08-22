##########################################################################################
##########################################################################################

import boto3, itertools
s3r = boto3.resource('s3')
bucket = s3r.Bucket('czbiohub-seqbot')

for obj_sum in itertools.islice(bucket.objects.filter(Prefix='fastqs/171120_A00111_0085_AH57YYDMXX/rawdata'), None, None, 1000):
    obj = s3r.Object(obj_sum.bucket_name, obj_sum.key)
    storage_class = obj.storage_class
    restore = obj.restore
    print(obj.key, obj.storage_class, obj.restore)

##########################################################################################
##########################################################################################
