from gophy import wrap
import platform
# Entrance module


def img2gif(img, out, fps=4):
    os = platform.system()
    arch = platform.architecture()[0]

    dll = None
    if os == "Linux":
        if arch == "64bit":
            dll = "../build/linux_x64/img2gif.so"

    if dll is None:
        raise Exception("This operation system or architecture is not supported")


    w = wrap.Wrapper(dll)
    w.lib.Build(wrap.paths_to_go(img), fps, wrap.create_go_string(out))

img2gif(["../res/g1.gif", "../res/g2.gif", "../res/g3.gif"], "gopher.gif")

print(platform.architecture(), platform.system(), platform.release())