from edinet_xbrl.edinet_xbrl_downloader import EdinetXbrlDownloader

## init downloader
xbrl_downloader = EdinetXbrlDownloader()

## set a ticker you want to download xbrl file

ticker = "6758" ## test sony

target_dir = "C:\\edinet_xbrl\\xbrl"

xbrl_downloader.download_by_ticker(ticker, target_dir)
