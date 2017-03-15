for GOOS in darwin linux windows; do
    for GOARCH in 386 amd64; do
	GOOS=$GOOS GOARCH=$GOARCH go build -o img2gif-$GOOS-$GOARCH.so -buildmode=c-shared ../../main.go
    done
done
