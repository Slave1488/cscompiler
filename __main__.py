import re


def parse_line(line):
    name = re.search(
        r'(?:[^\s()]+(?:\(.*?\S.*?\))?$)|(?:[^\s()]+(?=\(\s*\)$))', line)
    name = name.group() if name else '???'
    sym = '?'
    if re.search(r'(?:class)|(?:delegate)', line):
        sym = 'T'
    elif re.search(r'event', line):
        sym = 'E'
    elif re.search(r'\(.*\)', line):
        sym = 'M'
    else:
        sym = 'F'
    return sym, name

f = open("content.txt", 'r')

content = f.read()

namespace = re.search(r'namespace ([^{/s]*)', content).group(1)

need_data = [(parse_line(re.search(r'(?:[^\s{;=][^{;=]*[^\s{;=])|(?:[^\s{;=])',
                                   d[1]).group()),
              re.findall(r'(?:<.*?>)|(?:[^<\s/][^<\n/]*[^<\s])|(?:[^<\s/])',
                         d[0]))
             for d in re.findall(r'([ \t\r\f\v]*///.*(?:\s*///.*)+)\n(.*)',
                                 content)]


class Name:
    def __init__(self, sym, name):
        self._sym = sym
        self._name = name
        self._parent = None

    def get_name(self):
        return "{}.{}".format(self._parent.get_name(),
                              self._name) if self._parent else self._name

    def __str__(self):
        return "{}:{}".format(self._sym, self.get_name())


class Tag:
    def __init__(self, name):
        self._name = name
        self._content = []

    def __str__(self):
        return "<{0}>{1}\n</{0}>".format(self._name,
                                         '\n'.join(map(str, self._content)))
