import os


class Workspace(object):
    def __init__(self, download_file_dir, output_dir):
        self.download_file_dir = download_file_dir
        self.output_dir = output_dir

    def mkdir(self):
        if not os.path.exists(self.download_file_dir):
            os.mkdir(self.download_file_dir)
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)
