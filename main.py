from command.edinetdownloader import EdinetDownloader
from command.edinet_extract_parser import EdinetExtractParser
from models import workspace


def getEdinetCodeList():
    return [line.rstrip('\n') for line in open("public\\edinet_code_list.txt")]


if __name__ == '__main__':

    for edinet_code in getEdinetCodeList():

        print("Start By Edinet Code: ", edinet_code)
        w = workspace.Workspace(
            "C:\\edinet_xbrl\\xbrl\\{}\\".format(edinet_code),
            "C:\\edinet_xbrl\\issues\\{}\\".format(edinet_code)
        )

        w.mkdir()

        downloader = EdinetDownloader(edinet_code, w)
        downloader.execute()

        parser = EdinetExtractParser("BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock", w)
        parser.execute()
