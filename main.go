package main

import (
	"github.com/ritchie46/GOPHY/img2gif"
)

func main() {
	files := []string {"./src/github.com/ritchie46/GOPHY/test/1.png", "./src/github.com/ritchie46/GOPHY/test/3.png"}
	img2gif.BuildGif(&files, "./src/github.com/ritchie46/GOPHY/test/out.gif")
}