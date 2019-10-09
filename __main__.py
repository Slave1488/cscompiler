import re

f = open("content.txt", 'r')

content = f.read().split('\n')

doc_content = [r.group(1)
               for r in [re.match(r'\s*///\s*(.*\S)\s*', c)
                         for c in content]
               if r]

doc_content = [w
               for s in doc_content
               for w in re.findall(r'(<.*?>)', s)]

print(doc_content)
