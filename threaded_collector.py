import sys
from pathlib import Path
import concurrent.futures

MP3_AUDIO = []
WAV_AUDIO = []
FLAC_AUDIO = []
OGG_AUDIO = []
AMR_AUDIO = []
...
JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
BMP_IMAGES = []
SVG_IMAGES = []
...
AVI_VIDEOS = []
MP4_VIDEOS = []
VIDEOS_IN_3GP = []
MOV_VIDEOS = []
MKV_VIDEOS = []
...
DOC_DOCS = []
DOCX_DOCS = []
TXT_DOCS = []
PDF_DOCS = []
XLSX_DOCS = []
PPTX_DOCS = []
MPP_DOCS = []
...
ZIP_ARCHIVES = []
RAR_ARCHIVES = []
ISO_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []
...
APP_TYPE = []
...
TORRENT_TYPE = []
...
PYTHON_TYPE = []
...
ANOTHER_TYPES = []

KNOWN_EXT = {
    'EXE': APP_TYPE,
    'TORRENT': TORRENT_TYPE,
    'PY': PYTHON_TYPE,
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'BMP': BMP_IMAGES,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'FLAC': FLAC_AUDIO,
    'AMR': AMR_AUDIO,
    'MKV': MKV_VIDEOS,
    '3GP': VIDEOS_IN_3GP,
    'MP4': MP4_VIDEOS,
    'MOV': MOV_VIDEOS,
    'AVI': AVI_VIDEOS,
    'DOC': DOC_DOCS,
    'DOCX': DOCX_DOCS,
    'TXT': TXT_DOCS,
    'PDF': PDF_DOCS,
    'XLSX': XLSX_DOCS,
    'PPTX': PPTX_DOCS,
    'MPP': MPP_DOCS,
    'ZIP': ZIP_ARCHIVES,
    'RAR': RAR_ARCHIVES,
    'ISO': ISO_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()
ALL_THAT_I_FOUND = []


def extract_extension(filename: str) -> str:

    return Path(filename).suffix[1:].upper()


def searcher(folder_for_scan: Path) -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        feature = list(executor.submit(ext_handler, item, folder_for_scan) for item in folder_for_scan.iterdir())


def ext_handler(item, folder):
    if item.is_dir():
        if item.name not in ('archives', 'audio', 'video', 'documents', 'images',
                             'uncertain_types', 'torrents', 'applications',
                             'python_files(scripts'):
            FOLDERS.append(item)
            searcher(item)
    else:
        ext = extract_extension(item.name)
        fullname = folder / item.name
        if not ext:
            ANOTHER_TYPES.append(fullname)
            ALL_THAT_I_FOUND.append(item.name)
        else:
            try:
                the_box = KNOWN_EXT[ext]
                EXTENSIONS.add(ext)
                the_box.append(fullname)
                ALL_THAT_I_FOUND.append(item.name)
            except KeyError:
                UNKNOWN.add(ext)
                ANOTHER_TYPES.append(fullname)
                ALL_THAT_I_FOUND.append(item.name)


if __name__ == '__main__':
    folder_for_sort = sys.argv[1]
    print(f'The process will start in folder {folder_for_sort}.')

    searcher(Path(folder_for_sort))

