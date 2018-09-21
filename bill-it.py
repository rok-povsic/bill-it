import os


class BillIt:

    def run(self):
        os.chdir('latex-template')
        os.system('./latexdockercmd.sh xelatex main.tex')


if __name__ == '__main__':
    BillIt().run()
