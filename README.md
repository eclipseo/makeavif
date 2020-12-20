# makeavif

This tool will bulk encode image files in given directory to [AVIF](https://en.wikipedia.org/wiki/AV1#AV1_Image_File_Format_(AVIF)). It will leave original files intact, creating .avif file next to each original.

## Supported input file formats:

* .jpg/.jpeg
* .png
* .y4m

Supports Windows, Linux, macOS and probably other OSes.

## Linux

```sh
pip install makeavif
makeavif --recursive /home/username/myphotos
```

You will need [avifenc](https://github.com/AOMediaCodec/libavif) in path. You can get it by running build_avif.sh as root

### Windows

You can download and use it as single Windows binary, see [Releases](https://github.com/varnav/makeavif/releases/)

Unfortunately antiviruses [don't like packed Python executables](https://github.com/pyinstaller/pyinstaller/issues?q=is%3Aissue+virus), so expect false positives from them if you go this way. Best way is pip.

You will need `avifenc` in path. You can download it [here](https://ci.appveyor.com/project/louquillio/libavif/build/artifacts) and copy to `%USERPROFILE%\AppData\Local\Microsoft\WindowsApps`

```cmd
./makeavif.exe "c:\\Users\\username\\Pictures\\My Vacation"
```

Remember, you need double slashes in Windows.

To view .avif file in Windows 10 you need [this](https://www.microsoft.com/store/productId/9MVZQVXJBQ9V) installed.

## See also

[makejxl](https://github.com/varnav/makejxl/)
[filmcompress](https://github.com/varnav/filmcompress/)