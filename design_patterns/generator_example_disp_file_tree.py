import sys

class File:
    def __init__(self, name):
        self.name = name


class Folder(File):
    def __init__(self, name):
        super().__init__(name)
        self.children = []


class TreeWalker:
    def __init__(self, root):
        self.root = root

    def walk(self, file):
        if isinstance(file, Folder):
            yield file.name + "/"
            for f in file.children:
                yield from self.walk(f)
        else:
            yield file.name


def build_tree():
    root = Folder("")
    etc = Folder("etc")
    root.children.append(etc)
    etc.children.append(File("passwd"))
    etc.children.append(File("groups"))
    httpd = Folder("httpd")
    etc.children.append(httpd)
    httpd.children.append(File("http.conf"))
    var = Folder("var")
    log = Folder("log")
    var.children.append(log)
    log.children.append(File("messages"))
    log.children.append(File("kernel"))
    return root


if __name__ == '__main__':
    root = build_tree()
    walker = TreeWalker(root)
    tree = walker.walk(walker.root)
    for item in tree:
        print(item)