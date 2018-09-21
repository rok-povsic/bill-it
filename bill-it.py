import configparser
import os


class BillIt:
    SUBDIR = 'latex-template'

    def run(self):
        settings = configparser.ConfigParser()
        settings.read('settings.ini')

        template_file_path = os.path.join(self.SUBDIR, 'invoice-template.tex')
        file_path = os.path.join(self.SUBDIR, 'main.tex')

        replacements = (
            ('[[YOUR-SHORT-NAME]]', settings['YourFirm']['short-name']),
            ('[[YOUR-FULL-NAME]]', settings['YourFirm']['full-name']),
            ('[[YOUR-STREET-LINE]]', settings['YourFirm']['street-line']),
            ('[[YOUR-CITY-LINE]]', settings['YourFirm']['city-line']),
        )

        with open(template_file_path) as f_in:
            with open(file_path, 'w') as f_out:
                for line in f_in:
                    updated_line = line
                    for from_str, to_str in replacements:
                        updated_line = updated_line.replace(from_str, to_str)
                    f_out.write(updated_line)

        os.chdir(self.SUBDIR)
        os.system('./latexdockercmd.sh xelatex main.tex')
        os.chdir('..')

        os.remove(file_path)


if __name__ == '__main__':
    BillIt().run()
