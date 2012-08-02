import fileinput
import re
import subprocess
import sys

url_regex = re.compile("(((https?|ftp|gopher)://|(mailto|file|news):)[^' <>\"]+|(www|web|w3).[-a-z0-9.]+)[^' .,;<>\":]")

def run(filenames):
    results = []
    for line in fileinput.input(filenames):
        for idx, m in enumerate(re.finditer(url_regex, line)):
            results.append(line[m.start(): m.end()])

    print('== URLS ==')
    for i, s in enumerate(results):
        print('{}\t{}'.format(i, s))

    rslt = raw_input('Selection? ')
    idx = int(rslt)
    subprocess.Popen(['google-chrome', results[idx]])

if __name__ == '__main__':
    run(sys.argv[1:])