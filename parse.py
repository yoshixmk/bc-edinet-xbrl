from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser

## init parser
parser = EdinetXbrlParser()

## parse xbrl file and get data container
xbrl_file_path = "C:\\edinet_xbrl\\xbrl\\jpctl010000-icr-001_E01777-000_2019-06-18_01_2019-06-18.xbrl"
edinet_xbrl_object = parser.parse_file(xbrl_file_path)

## get value from container
key = "jppfs_cor:Assets"
context_ref = "CurrentYearInstant"
current_year_assets = edinet_xbrl_object.get_data_by_context_ref(key, context_ref).get_value()

#print(current_year_assets)
