package main

import (
	"github.com/ritchie46/GOPHY/img2gif"
)

func main() {
	files := []string {"./src/github.com/ritchie46/GOPHY/test/1.png", "./src/github.com/ritchie46/GOPHY/test/3.png"}
	img := img2gif.ReadImages(&files)
	im_p := img2gif.EncodeImgPaletted(&img)
	img2gif.WriteGif(&im_p, 5, "./src/github.com/ritchie46/GOPHY/test/out.img2gif")
}