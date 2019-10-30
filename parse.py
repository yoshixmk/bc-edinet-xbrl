from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser

## init parser
parser = EdinetXbrlParser()

## parse xbrl file and get data container
# xbrl_file_path = "C:\\edinet_xbrl\\xbrl\\jpcrp040300-q1r-001_E01777-000_2019-06-30_01_2019-08-05.xbrl"

# key = "jpcrp_cor:TotalAssetsUSGAAPSummaryOfBusinessResults"
# context_ref = "Prior1QuarterInstant"
# current_q1_assets = edinet_xbrl_object.get_data_by_context_ref(key, context_ref).get_value()

# 1e
# https://www.fsa.go.jp/search/20190228.html
# for key in edinet_xbrl_object.get_keys():
#     values = []
#     for value in edinet_xbrl_object.get_data_list(key):
#         values.append(value.get_value())
#     print(key, values)

# for key in edinet_xbrl_object.get_keys():
#     for value in edinet_xbrl_object.get_data_list(key):
#         v_str = value.get_value()
#         if "対処すべき課題" in str(v_str):
#             print(key, v_str)

xbrl_file_path = "C:\\edinet_xbrl\\xbrl\\jpcrp030000-asr-001_E01777-000_2019-03-31_02_2019-08-01.xbrl"
edinet_xbrl_object = parser.parse_file(xbrl_file_path)

targetText = "BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock".lower()
issueKeys = {key for key in edinet_xbrl_object.get_keys() if str(key).__contains__(targetText)}

for key in issueKeys:
    for value in edinet_xbrl_object.get_data_list(key):
        print(value.get_value())

# TODO
# 1. fileに書き出す。html形式
# 2. font-family: &apos;MS Mincho&apos;; 消す
# 3. html, head周りを付与する
