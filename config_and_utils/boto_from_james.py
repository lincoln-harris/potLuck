client = boto3.client('s3')

paginator = client.get_paginator('list_objects')
response_iterator = paginator.paginate(
	Bucket='lincoln.harris-work',
	Prefix='whatever/directory/structure/')

# this is the list of file names in that bucket starting with that prefix
file_set = {r['Key'] for result in response_iterator
			for r in result.get('Contents', [])}
