from gophy import wrap
import os
import platform
# Entrance module


def img2gif(img, out, fps=4):
    """
    Create a GIF file from images.

    :param img: (list) With paths to source images.
    :param out: (str) Out file.
    :param fps: (int) Frames per second.
    :return:
    """
    _os = platform.system()
    arch = platform.architecture()[0]

    dll = None
    if _os == "Linux":
        if arch == "64bit":
            dll = "GOPHY-linux-amd64.so"
        else:
            dll = "GOPHY-linux-386.so"
    elif _os == "Windows":
        raise Exception("Windows not yet supported")
    elif _os == "Darwin":
        if arch == "64bit":
            dll = "GOPHY-darwin-10.6-amd64.dylib"
        else:
            dll = "GOPHY-darwin-10.6-386.dylib"

    if dll is None:
        raise Exception("This operation system or architecture is not supported")

    w = wrap.Wrapper("{}/build/{}".format(os.path.dirname(__file__), dll))
    w.lib.Build(wrap.paths_to_go(img), fps, wrap.create_go_string(out))



