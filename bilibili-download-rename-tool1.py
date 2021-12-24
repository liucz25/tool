# -*- coding: utf-8 -*-
import sys
from pathlib import Path
import json


class DirectionTree(object):
    """生成目录树
    @ pathname: 目标目录
    @ filename: 要保存成文件的名称
    """

    def __init__(self, pathname='.', filename='tree.txt'):
        super(DirectionTree, self).__init__()
        self.pathname = Path(pathname)
        self.filename = filename
        self.tree = ''

    def set_path(self, pathname):
        self.pathname = Path(pathname)

    def set_filename(self, filename):
        self.filename = filename

    def generate_tree(self, n=0):
        # print("gt1")
        # if self.pathname.is_file():
        # print("gt2")
        # pass
        # self.tree += '    |' * n + '-' * 4 + self.pathname.name + '\n'
        if self.pathname.is_dir():
            # if self.pathname[0] == 'c':
            #    print("rrrrr")
            # 找到要用的东西
            # print(self.pathname.parts[-1][0] == 'c')
            # if self.pathname.parts[-1][0] == 'c':
            #     self.doRename()
            newname = self.doRename()
            # 以上  我添加的
            self.tree += '    |' * n + '-' * 4 + \
                str(self.pathname.relative_to(self.pathname.parent)) + \
                '\\' + str(newname)+'\n'
            # print("gt4")
            for cp in self.pathname.iterdir():

                # print("gt5")
                self.pathname = Path(cp)
                self.generate_tree(n + 1)

    def doRename(self):
        if self.pathname.parts[-1][0] == 'c':
            # print(self.pathname.parts[-1])

            file = str(self.pathname)+"\\entry.json"
            newname = self.rename(file)
            print(newname)
            return newname

    def rename(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data['page_data']['download_subtitle']

    def save_file(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(self.tree)


if __name__ == '__main__':
    print("dayinkaishi,,,,")
    dirtree = DirectionTree()
    # 命令参数个数为1，生成当前目录的目录树
    print("dayinkaishi,,,,")
    if len(sys.argv) == 1:
        print("11111111,,,")
        print(Path.cwd())
        dirtree.set_path(Path.cwd())
        print("dfsa")
        dirtree.generate_tree()
        dirtree.save_file()
        print("321")
        print(dirtree.tree)
    # 命令参数个数为2并且目录存在存在
    elif len(sys.argv) == 2 and Path(sys.argv[1]).exists():
        print("22222211111111,,,")
        dirtree.set_path(sys.argv[1])
        dirtree.generate_tree()
        print(dirtree.tree)
    # 命令参数个数为3并且目录存在存在
    elif len(sys.argv) == 3 and Path(sys.argv[1]).exists():
        print("333333333322222211111111,,,")
        dirtree.set_path(sys.argv[1])
        dirtree.generate_tree()
        dirtree.set_filename(sys.argv[2])
        dirtree.save_file()
    else:  # 参数个数太多，无法解析
        print('命令行参数太多，请检查！   使用方法：到都是数字的目录，运行文件 python file-tree-rename.py  即可生成tree。txt 文件，文件内容为目录')
