import os


class Workspace(object):
    def __init__(self, downloader_output_dir, parser_output_dir):
        self.downloader_output_dir = downloader_output_dir
        self.parser_output_dir = parser_output_dir

    def mkdir(self):
        if not os.path.exists(self.downloader_output_dir):
            os.mkdir(self.downloader_output_dir)
        if not os.path.exists(self.parser_output_dir):
            os.mkdir(self.parser_output_dir)
