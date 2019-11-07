from commands.edinetdownloader import EdinetDownloader
from commands.edinet_extract_parser import EdinetExtractParser
from config.config import get_edinet_code_list, get_download_file_dir, get_output_dir
from controllers.EdinetStrategy import EdinetStrategy
from models import workspace

if __name__ == '__main__':

    for edinet_code in get_edinet_code_list():
        print("Start By Edinet Code: ", edinet_code)

        w = workspace.Workspace(
                get_download_file_dir(edinet_code),
                get_output_dir(edinet_code))
        w.mkdir()

        edinet_strategy = EdinetStrategy()
        edinet_strategy.add(EdinetDownloader(edinet_code, w))
        edinet_strategy.add(EdinetExtractParser("BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock", w))
        edinet_strategy.act()
