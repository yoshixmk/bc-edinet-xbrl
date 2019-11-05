import os

from downloader import Downloader
from extract_parser import ExtractParser

if __name__ == '__main__':
    downloader = Downloader("6758")
    downloader.execute()

    parser = ExtractParser("BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock")
    parser.execute()

    # new_dir_path = 'data/temp/new-dir'
    # os.mkdir(new_dir_path)

