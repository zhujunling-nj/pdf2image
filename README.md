# pdf2image
Convert the PDF file to images.

```
usage: pdf2image.exe [options] <file>

positional arguments:
  file             The file path

optional arguments:
  -h, --help       show this help message and exit
  --outdir OUTDIR  output dircetory
  --first FIRST    first page
  --last LAST      last page
  --dpi DPI        image dpi

  --outdir  图像输出目录，如果未指定，则PDF文件名(删除.pdf)作为输出目录
  --first   起始页(从1开始)，如果未指定，则从首页开始
  --last    截止页，如果未指定，则转换到最后一页
  --dpi     图象DPI(每吋像素)，缩放系数=dpi/72
```

如果要转换目录下的所有PDF文件，执行:
```
pdf2image.bat <src_dir> [<dest_dir>]
  src_dir   PDF文件所在目录
  dest_dir  图像输出目录
```

【注】pdf2image.exe是使用nuitka编译后的可执行程序，杀毒软件有时会误报有病毒。
