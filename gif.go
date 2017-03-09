package main

import (
	"fmt"
	"os"
	"image"
	"image/gif"
	_ "image/png"
	_ "image/jpeg"

	"bytes"

)

// Read images from a slice with file locations.
func readImages(files *[]string) []image.Image {
	im := []image.Image{}

	for _, s := range *files {
		fmt.Println("Paths to images", s)
		f, err := os.Open(s)

		if err != nil {
			fmt.Println(err)
		}

		img, _, err := image.Decode(f)

		if err != nil {
			fmt.Println(err)
		}

		im = append(im, img)
		f.Close()
	}
	return im
}

// Encode images in *image.Paletted by encoding and decoding to gif and image.
// Encode and decode is necessary to convert jpeg and png to gif.
func encodeImgPaletted(images *[]image.Image) []*image.Paletted {
	// Gif options
	opt := gif.Options{}
	g := []*image.Paletted{}

	for _, im := range *images {
		b := bytes.Buffer{}
		// Write gif file to buffer.
		err := gif.Encode(&b, im, &opt)

		if err != nil {
			println(err)
		}
		// Decode gif file from buffer to img.
		img, err := gif.Decode(&b)

		if err != nil {
			println(err)
		}

		// Cast img.
		i, ok := img.(*image.Paletted)
		println(i, ok)
		if ok {
			g = append(g, i)
		}
	}
	return g
}

// Write a gif file from an paletted image slice
// d = delay in 100ths of a second per frame.
func writeGif(im *[]*image.Paletted, d int, path string) {
	//
	g := &gif.GIF{}

	for _, i := range *im {
		g.Image = append(g.Image, i)
		g.Delay = append(g.Delay, d)
	}
	f, err := os.Create(path)

	if err != nil {
		println(err)
	}
	defer f.Close()
	gif.EncodeAll(f, g)
}

func main() {
	files := []string {"./src/github.com/ritchie46/imagesGoGif/test/1.png", "./src/github.com/ritchie46/imagesGoGif/test/2.png"}
	img := readImages(&files)
	im_p := encodeImgPaletted(&img)
	writeGif(&im_p, 5, "./src/github.com/ritchie46/imagesGoGif/test/out.gif")




}
