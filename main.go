package main

import "C"

import (
	"github.com/ritchie46/GOPHY/img2gif"
)

//export Build
func Build(f []string, fps int, p string) {
	err := img2gif.BuildGif(&f, fps, p)

	if err != nil {
		println(err)
	}
}

func main() {

}