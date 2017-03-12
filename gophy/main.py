from gophy import wrap
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
    os = platform.system()
    arch = platform.architecture()[0]

    dll = None
    if os == "Linux":
        if arch == "64bit":
            dll = "img2gif-linux-amd64.so"
        else:
            dll = "img2gif-linux-386.so"
    elif os == "Windows":
        if arch == "64bit":
            dll = "img2gif-windows-amd64.so"
        else:
            dll = "img2gif-windows-386.so"
    elif os == "Darwin":
        if arch == "64bit":
            dll = "img2gif-darwin-amd64.so"
        else:
            dll = "img2gif-darwin-386.so"

    if dll is None:
        raise Exception("This operation system or architecture is not supported")

    w = wrap.Wrapper("./build/" + dll)
    w.lib.Build(wrap.paths_to_go(img), fps, wrap.create_go_string(out))



