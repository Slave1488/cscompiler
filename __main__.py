import re

f = open("content.txt", 'r')

content = f.read().split('\n')

doc_content = [r.group(1)
               for r in [re.match(r'///\s*(?:)\s*', c)
                         for c in content]
               if r]

print(doc_content)
