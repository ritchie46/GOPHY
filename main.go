package main

import "C"

// Build with: go build -o img2gif.so -buildmode=c-shared main.go

import (
	"github.com/ritchie46/GOPHY/img2gif"
)

//export Build
func Build(f []string, fps int, p string) error  {
	return img2gif.BuildGif(&f, fps, p)
}

func main() {

}