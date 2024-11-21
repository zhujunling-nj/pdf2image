# pdf2image
将PDF文件转换为图像。

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

  --outdir  保存图像的目录，如果未指定，则PDF文件名(删除.pdf后缀)作为输出目录；
  --first   起始页(首页为1)，如果未指定，则从首页开始；
  --last    截止页，如果未指定，则转换到最后一页；
  --dpi     图象DPI(每吋像素)，缩放系数: dpi/72。
```
