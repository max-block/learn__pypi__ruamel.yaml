import sys

from ruamel.yaml import YAML

ORIGINAL_DATA = """
    a: 1
    b: bla bla
    c: 2019-12-23 09:33:25.943138
    d:
    - 1
    - 2
    - 3
    - 4
    e: true # comment is saved
    f: null
    """


def load():
    yaml = YAML(typ="safe")
    res = yaml.load(ORIGINAL_DATA)
    print(res)


def dump():
    data = {"name": "n1", "value": 17}
    yaml = YAML()
    yaml.dump(data, sys.stdout)


load()
dump()
