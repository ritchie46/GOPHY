package img2gif

import (
	"fmt"
	"os"
	"image"
	_ "image/png"
	_ "image/jpeg"
	"bytes"
	"image/gif"
)

// Read images from a slice with file locations.
func ReadImages(files *[]string) []image.Image {
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

// Encode images in *image.Paletted by encoding and decoding to img2gif and image.
// Encode and decode is necessary to convert jpeg and png to img2gif.
func EncodeImgPaletted(images *[]image.Image) []*image.Paletted {
	// Gif options
	opt := gif.Options{}
	g := []*image.Paletted{}

	for _, im := range *images {
		b := bytes.Buffer{}
		// Write img2gif file to buffer.
		err := gif.Encode(&b, im, &opt)

		if err != nil {
			println(err)
		}
		// Decode img2gif file from buffer to img.
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

// Write a img2gif file from a paletted image slice
// d = delay in 100ths of a second per frame.
func WriteGif(im *[]*image.Paletted, d int, path string) {
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


