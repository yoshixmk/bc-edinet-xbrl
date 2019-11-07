def get_edinet_code_list():
    return [line.rstrip('\n') for line in open("config/edinet_code_list.txt")]


def get_download_file_dir(edinet_code):
    return "C:\\edinet_xbrl\\xbrl\\{}\\".format(edinet_code)


def get_output_dir(edinet_code):
    return "C:\\edinet_xbrl\\issues\\{}\\".format(edinet_code)