import csv
import shutil
from tempfile import NamedTemporaryFile

ORIGINAL = 'original.csv'
ORIGINAL_KEY_FIELDNAME = 'Price Seq'
ORIGINAL_VAL_FIELDNAME = 'Price'

CHANGES = 'changes.csv'


DICT_KEY_FIELDNAME = 'Price Seq'
DICT_VAL_FIELDNAME = 'Price'

OUTPUT_FILE = 'my.csv'

tempfile = NamedTemporaryFile(mode='w', delete=False)

memory_dict = dict()

# Create a memory dictionary where the item key is price_sec
# and value is the updated price value
with open(CHANGES, newline='', encoding='utf8') as changes:
    reader = csv.DictReader(changes, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        memory_dict[int(row[DICT_KEY_FIELDNAME])] = row[DICT_VAL_FIELDNAME]

with open(
    ORIGINAL,
    'r',
    newline='',
    encoding='utf-8',
) as csvfile:
    reader = csv.DictReader(csvfile, quoting=csv.QUOTE_MINIMAL)
    writer = csv.DictWriter(
        tempfile,
        fieldnames=reader.fieldnames,
        quoting=csv.QUOTE_MINIMAL,
    )

    for row in reader:
        row[ORIGINAL_VAL_FIELDNAME] = memory_dict[int(row[ORIGINAL_KEY_FIELDNAME])]
        writer.writerow(row)

shutil.move(tempfile.name, OUTPUT_FILE)
