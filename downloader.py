from edinet_xbrl.edinet_xbrl_downloader import EdinetXbrlDownloader


class Downloader(object):
    def __init__(self, ticker_or_edinet_code, workspace):
        self.xbrl_downloader = EdinetXbrlDownloader()
        self.ticker_or_edinet_code = ticker_or_edinet_code  # sony "6758" or Edinet Code
        self.target_dir = workspace.downloader_output_dir

    def execute(self):
        self.xbrl_downloader.download_by_ticker(self.ticker_or_edinet_code, self.target_dir)
