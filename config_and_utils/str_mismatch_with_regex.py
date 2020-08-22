### 2.2.18
### To allow for mismatch in python string searches
###     This might work for find_barcodes_and_UMIs.py script

import regex
pm=regex.findall("(AA){e<=1}", "CAAG", overlapped=True)


