from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser

# 資料
## 1e：タクソノミ要素リスト
## https://www.fsa.go.jp/search/20190228.html

# parse

## init parser
parser = EdinetXbrlParser()

## target
# xbrl_file_path = "C:\\edinet_xbrl\\xbrl\\jpcrp030000-asr-001_E01777-000_2019-03-31_02_2019-08-01.xbrl"
# edinet_xbrl_object = parser.parse_file(xbrl_file_path)

## parse xbrl file and get data container

# パターン1
# for key in edinet_xbrl_object.get_keys():
#     for value in edinet_xbrl_object.get_data_list(key):
#         v_str = value.get_value()
#         if "対処すべき課題" in str(v_str):
#             print(key, v_str)

# パターン２
# targetText = "BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock".lower()
# issueKeys = {key for key in edinet_xbrl_object.get_keys() if str(key).__contains__(targetText)}
#
# for key in issueKeys:
#     for value in edinet_xbrl_object.get_data_list(key):
#         print(value.get_value())

# ディレクトリ内のファイル一覧
xbrl_dir_path = "C:\\edinet_xbrl\\xbrl\\"
#
# import os
# files = []
# # r=root, d=directories, f = files
# for r, d, f in os.walk(xbrl_dir_path):
#     for file in f:
#         files.append(os.path.join(r, file))

issues_dir_path = "C:\\edinet_xbrl\\issues\\"

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(xbrl_dir_path) if isfile(join(xbrl_dir_path, f))]

targetText = "BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock".lower()

for f in onlyfiles:
    edinet_xbrl_object = parser.parse_file(xbrl_dir_path + f)
    issueKeys = {key for key in edinet_xbrl_object.get_keys() if str(key).__contains__(targetText)}
    for key in issueKeys:
        for value in edinet_xbrl_object.get_data_list(key):
            text_file = open(issues_dir_path + f + "_issue.html", "w", encoding='UTF-8')
            text_file.write(value.get_value())

# TODO
# 2. font-family: &apos;MS Mincho&apos;; 消す
# 3. html, head周りを付与する
