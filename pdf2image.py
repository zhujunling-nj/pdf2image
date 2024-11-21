""" PDF to images """
import os
from argparse import ArgumentParser
from win32ui import CreateFileDialog
import fitz


def pdf_to_images(filename, dirname, **kwargs):
    """ Convert pdf to images """
    dpi = kwargs.get('dpi')
    start = kwargs.get('first_page') or 1
    stop = kwargs.get('last_page') or -1
    with fitz.open(filename) as pdf:
        page_count = pdf.page_count
        start = page_count + start if start < 0 else start - 1
        stop = page_count + stop + 1 if stop < 0 else stop
        width = 1 if page_count < 10 else \
                2 if page_count < 100 else \
                3 if page_count < 1000 else 4
        for pageno, page in enumerate(pdf.pages(start, stop), start=start+1):
            imagefile = f'{dirname}\\page_{pageno:0{width}d}.png'
            pixmap = page.get_pixmap(dpi=dpi, alpha=False)
            pixmap.save(imagefile)
            print(imagefile)


def file_dialog():
    """ 选择文件 """
    ## 0x1000: FileMustExist
    dialog = CreateFileDialog(
        True, None, None, 0x1000, 'PDF Files (*.pdf)|*.pdf'
    )
    dialog.DoModal()
    return dialog.GetPathName()


def main(args=None):
    """ main function """
    parser = ArgumentParser(usage='%(prog)s [options] <file>')
    parser.add_argument('file', nargs='?', help='The file path')
    parser.add_argument('--outdir', help='output dircetory')
    parser.add_argument('--first', type=int, help='first page')
    parser.add_argument('--last', type=int, help='last page')
    parser.add_argument('--dpi', type=int, help='image dpi')
    options = parser.parse_args(args)

    if not (filename := options.file):
        if not (filename := file_dialog()):
            parser.print_help()
            return

    dirname = options.outdir or os.path.splitext(filename)[0]
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    pdf_to_images(
        filename, dirname, dpi=options.dpi or 144,
        first_page=options.first, last_page=options.last
    )


if __name__ == '__main__':
    main()
