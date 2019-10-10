import re

f = open("content.txt", 'r')

content = f.read()

namespace = re.search(r'namespace ([^{/s]*)', content).group(1)

need_data = [(re.search(r'(?:\S.*\S)|(?:\S)', d[1]).group(),
              re.findall(r'(?:<.*?>)|(?:[^<\s/][^<\n/]*[^<\s])|(?:[^<\s/])',
                         d[0]))
             for d in re.findall(r'([ \t\r\f\v]*///.*(?:\s*///.*)+)\n(.*)',
                                 content)]
