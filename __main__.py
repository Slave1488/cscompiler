import re

f = open("content.txt", 'r')

content = f.read()

need_data = re.findall(r'([ \t\r\f\v]*///.*(?:\s*///.*)+)\n(.*)', content)

temp = [(re.findall(r'(?:<.*?>)|(?:[^<\s/][^<\n/]*[^<\s])|(?:[^<\s/])', d[0]), re.search(r'/S.*/S', d[1]))
        for d in need_data]

check = False
if check:
    print(temp)
else:
    for s in temp:
        print(s)

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
