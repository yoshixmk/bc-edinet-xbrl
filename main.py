from downloader import Downloader
from extract_parser import ExtractParser
from models import workspace

if __name__ == '__main__':
    target_ticker = "6758"

    workspace = workspace.Workspace(
        "C:\\edinet_xbrl\\xbrl\\" + target_ticker,
        "C:\\edinet_xbrl\\issues\\" + target_ticker
    )

    workspace.mkdir()

    downloader = Downloader(target_ticker, workspace)
    downloader.execute()

    parser = ExtractParser("BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock", workspace)
    parser.execute()

