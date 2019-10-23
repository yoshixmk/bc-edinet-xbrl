from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser

## init parser
parser = EdinetXbrlParser()

## parse xbrl file and get data container
xbrl_file_path = "C:\\edinet_xbrl\\xbrl\\jpcrp040300-q1r-001_E01777-000_2019-06-30_01_2019-08-05.xbrl"
edinet_xbrl_object = parser.parse_file(xbrl_file_path)

# key = "jpcrp_cor:TotalAssetsUSGAAPSummaryOfBusinessResults"
# context_ref = "Prior1QuarterInstant"
# current_q1_assets = edinet_xbrl_object.get_data_by_context_ref(key, context_ref).get_value()

# 1e
# https://www.fsa.go.jp/search/20190228.html
for key in edinet_xbrl_object.get_keys():
    values = []
    for value in edinet_xbrl_object.get_data_list(key):
        values.append(value.get_value())
    print(key, values)
