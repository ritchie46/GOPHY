from ctypes import *
# thanks to https://dev.to/vladimirvivien/calling-go-functions-from-other-languages
# Build with: go build -o img2gif.so -buildmode=c-shared main.go

"""
Creating a c array:
(type * x)(val_1, val_2)

x = length

or:

(type * x)(*list_variable

Points to list location.

##############################

# Example:
# Create a c array with go strings.
a = "./res/g1.gif"
c_arr = (GoString * 1)(create_go_string("a"))
print(c_arr)

GoSlice points to the starting index from that C array.

Structure of a c type GoSlice of integers.

# c_void_p = int
class GoSliceInt(Structure):
    _fields_ = [("data", POINTER(c_void_p)),
                ("len", c_longlong), ("cap", c_longlong)]

Usage:

py_arr = ["./res/g1.gif", "./res/g3.gif"]
c_arr = (GoString * 2)(create_go_string(py_arr[0]), create_go_string(py_arr[1]))
go_slice = GoSliceGoString(c_arr, 2, 2)

lib.Build(go_slice, 2, create_go_string("test.gif"))
"""


class Wrapper:
    def __init__(self, dll):
        # Load dll
        self.lib = cdll.LoadLibrary(dll)
        # Define the required argument types. Does not seem to be mandatory.
        self.lib.Build.argtypes = [GoSliceGoString, c_uint, GoString]
        self.a = None


# Go strings consist of a pointer to the first byte and the total length in bytes.
class GoString(Structure):
    _fields_ = [("p", c_char_p), ("n", c_longlong)]


class GoSliceGoString(Structure):
    """
    General description of what this structures data is. It uses C data types to imitate a Go Slice.

    :param data: (Pointer) to first value in the slice. Type of the value must be specified. This is done by passing
                 a C array.
    :param len: (int, c_longlong) Length of the slice.
    :param cap: (int, c_longlong) Capacity of the slice.
    """
    _fields_ = [("data", POINTER(GoString)),
                ("len", c_longlong), ("cap", c_longlong)]


def create_go_string(s):
    b = s.encode("ascii")
    return GoString(b, len(b))


def paths_to_go(p):
    """
    Convert Python list with string to Go.

    :param p: (list) Containing Python strings of path names.
    :return: Go slice containing Go type strings.
    """
    sl = []
    l = len(p)
    for i in p:
        sl.append(create_go_string(i))
    c_arr = (GoString * l)(*sl)
    return GoSliceGoString(c_arr, l, l)



