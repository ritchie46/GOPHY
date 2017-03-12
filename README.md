# GOPHY

![](./res/gopher.gif)

Python binding to the GIF module in Golang. Create an animated GIF from an array of image locations.

Supported image types are:

* PNG
* JPEG
* GIF





```go
	files := []string {"./picture_1.png",
	"./picture_2.png"}

	fps := 2
	out := "./out.gif"

	img2gif.BuildGif(&files, fps, out)
```