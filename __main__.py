import re

f = open("content.txt", 'r')

content = f.read()

need_data = re.findall(r'([ \t\r\f\v]*///.*(?:\s*///.*)+)\n(.*)', content)

for t in need_data:
    print("{0}\n-----------------------------------\n{1}\n".format(t[0], t[1]))

content = content.split('\n')

doc_content = [r.group(1)
               for r in [re.match(r'\s*///\s*(.*\S)\s*', c)
                         for c in content]
               if r]

doc_content = [
    w
    for s in doc_content
    for w in re.findall(r'(?:<.*?>)|(?:[^<\s][^<]*[^<\s])|(?:[^<\s])', s)
]
