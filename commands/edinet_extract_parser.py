from commands.command import Command
from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser
from os import listdir
from os.path import isfile, join
from string import Template


class EdinetExtractParser(Command):
    def __init__(self, target_text, workspace):
        self.parser = EdinetXbrlParser()
        self.xbrl_dir_path = workspace.download_file_dir
        self.issues_dir_path = workspace.output_dir
        self.target_text = target_text.lower()

    # fontが気になる場合は、font-family: &apos;MS Mincho&apos;; 消す
    def execute(self):
        super().execute()
        only_files = [f for f in listdir(self.xbrl_dir_path) if isfile(join(self.xbrl_dir_path, f))]

        template_file = open('public/template.html')
        template = Template(template_file.read())

        for f in only_files:
            edinet_xbrl_object = self.parser.parse_file(self.xbrl_dir_path + f)
            issue_keys = {key for key in edinet_xbrl_object.get_keys() if str(key).__contains__(self.target_text)}
            for key in issue_keys:
                for edinet_data in edinet_xbrl_object.get_data_list(key):
                    html_file = open(self.issues_dir_path + f + "_issue.html", "w", encoding='UTF-8')
                    html_file.write(self.generateHtml(template, edinet_data))

    @staticmethod
    def generateHtml(template, value):
        return template.substitute({'main_contents': value.get_value()})
