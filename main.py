import csv
import shutil
from tempfile import NamedTemporaryFile

ORIGINAL = 'juicer file output 9-29.csv'
ORIGINAL_KEY_FIELDNAME = 'Price Seq'
ORIGINAL_VAL_FIELDNAME = 'Price 1'

CHANGES = 'price_change_THURSDAY_17hr.csv'


DICT_KEY_FIELDNAME = 'Price Seq'
DICT_VAL_FIELDNAME = 'Price 1'

OUTPUT_FILE = 'my.csv'


tempfile = NamedTemporaryFile(mode='w', delete=False)

memory_dict = dict()

# Create a memory dictionary where the item key is price_sec
# and value is the updated price value
with open(CHANGES, newline='', encoding='utf8') as changes:
    reader = csv.DictReader(changes)    
    for row in reader:        
        memory_dict[int(row[DICT_KEY_FIELDNAME])] = row[DICT_VAL_FIELDNAME]


with open(
    ORIGINAL,
    'r',
    newline='',
    encoding='utf-8',
) as csvfile:
    reader = csv.DictReader(csvfile)    
    writer = csv.DictWriter(
        tempfile,
        fieldnames=reader.fieldnames,
        quoting=csv.QUOTE_NONE,
        quotechar='/'
    )
    writer.writeheader()
    writer.fieldnames.append(None)
    for row in reader: 
                
        for field in ('Item name','Price Group','Price Tier', 'Cross Reference 1','Cross Reference 2','Combo Group'):    
            row[field]='"'+row[field]+'"'
                   
        
        row[ORIGINAL_VAL_FIELDNAME] = memory_dict[int(row[ORIGINAL_KEY_FIELDNAME])]
        writer.writerow(row)

shutil.move(tempfile.name, OUTPUT_FILE)
