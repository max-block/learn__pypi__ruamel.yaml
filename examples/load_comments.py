import sys
from datetime import datetime

from ruamel.yaml import YAML

ORIGINAL_DATA = """
name: n1
value: 999 # keep this comment!
"""


def main():
    yaml = YAML()
    data = yaml.load(ORIGINAL_DATA)
    print(type(data))  # <class 'ruamel.yaml.comments.CommentedMap'>

    data["new_field"] = datetime.now()

    yaml.dump(data, sys.stdout)

    # name: n1
    # value: 999  # keep this comment!
    # new_field: 2021 - 10 - 25
    # 07: 54:55.699216


if __name__ == "__main__":
    main()
