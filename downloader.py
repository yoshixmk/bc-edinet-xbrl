from edinet_xbrl.edinet_xbrl_downloader import EdinetXbrlDownloader


class Downloader(object):
    def __init__(self, ticker, workspace):
        self.xbrl_downloader = EdinetXbrlDownloader()
        # set a ticker you want to download xbrl file
        self.ticker = ticker  # test sony "6758"
        self.target_dir = workspace.downloader_output_dir

    def execute(self):
        self.xbrl_downloader.download_by_ticker(self.ticker, self.target_dir)
