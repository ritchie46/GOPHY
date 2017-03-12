package main

import "C"

// Build with: go build -o img2gif.so -buildmode=c-shared main.go
// Build(&[]string{"./res/g1.gif", "./res/g3.gif"}, 2, "test.gif")

import (
	"github.com/ritchie46/GOPHY/img2gif"
)

//export Build
func Build(f []string, fps int, p string)  {
	img2gif.BuildGif(&f, fps, p)
}

func main() {

}