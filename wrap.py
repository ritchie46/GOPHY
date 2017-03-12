from ctypes import *
# thanks to https://dev.to/vladimirvivien/calling-go-functions-from-other-languages

"""
# Example:
# Create a c array with go strings.
a = "./res/g1.gif"
c_arr = (GoString * 1)(create_go_string("a"))
print(c_arr)
"""

lib = cdll.LoadLibrary("./img2gif.so")


class GoString(Structure):
    _fields_ = [("p", c_char_p), ("n", c_longlong)]


# c_void_p = int
class GoSliceInt(Structure):
    _fields_ = [("data", POINTER(c_void_p)),
                ("len", c_longlong), ("cap", c_longlong)]


class GoSliceGoString(Structure):
    _fields_ = [("data", POINTER(GoString)),
                ("len", c_longlong), ("cap", c_longlong)]


def create_go_string(s):
    b = s.encode("ascii")
    return GoString(b, len(b))

# Define the required argument types. Does not seem to be mandatory.
lib.Build.argtypes = [GoSliceGoString, c_uint, GoString]

py_arr = ["./res/g1.gif", "./res/g3.gif"]
c_arr = (GoString * 2)(create_go_string(py_arr[0]), create_go_string(py_arr[1]))
go_slice = GoSliceGoString(c_arr, 2, 2)


lib.Build(go_slice, 2, create_go_string("test.gif"))