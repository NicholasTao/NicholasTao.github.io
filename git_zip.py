import os
import os.path

GIT_ZIP = "gitzip.txt"
GIT_FILE = open(GIT_ZIP, "w")


def dfs_showdir(path):
    for item in os.listdir(path):
        if item == "__pycache__":
            continue
        newitem = path + '/' + item
        print(newitem)
        if "venv" in newitem or "idea" in newitem:
            continue
        if os.path.isdir(newitem):
            GIT_FILE.write("---FOLDER %s\n" % newitem)
            dfs_showdir(newitem)
        elif newitem.endswith("py") or newitem.endswith("json"):
            GIT_FILE.write("---FILE %s\n" % newitem)
            with open(newitem, "r", encoding="utf-8") as nf:
                # if newitem == "../src/client/dao/db/__init__.py":
                #     a = nf.read()
                #     print(a)
                GIT_FILE.write(nf.read())


if __name__ == '__main__':
    dfs_showdir('../src')
