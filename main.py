import concurrent.futures
import shutil
import sys
from pathlib import Path
from threading import Thread
import threaded_collector as collector
from normalize import normalize
from tqdm import tqdm
import time


def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_add_on_stuff(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_another_of_types(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_archives(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()), str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'\tDIRECTED BY:')
        print('\tRobert B Weide')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folders(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Oops, the things gone wrong with -- {folder}')


class Images:

    @staticmethod
    def thread_jpeg_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            # feature = list(executor.submit(handle_media, file, folder / 'images') for file in collector.JPEG_IMAGES)

            for file in collector.JPEG_IMAGES:
                executor.submit(handle_media, file, folder / 'images')

    @staticmethod
    def thread_jpg_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.JPG_IMAGES:
                executor.submit(handle_media, file, folder / 'images')

    @staticmethod
    def thread_png_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.PNG_IMAGES:
                executor.submit(handle_media, file, folder / 'images')

    @staticmethod
    def thread_svg_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.SVG_IMAGES:
                executor.submit(handle_media, file, folder / 'images')

    @staticmethod
    def thread_bmp_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.BMP_IMAGES:
                executor.submit(handle_media, file, folder / 'images')


...


class Audio:

    @staticmethod
    def thread_mp3_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.MP3_AUDIO:
                executor.submit(handle_media, file, folder / 'audio')

    @staticmethod
    def thread_wav_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.WAV_AUDIO:
                executor.submit(handle_media, file, folder / 'audio')

    @staticmethod
    def thread_ogg_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.OGG_AUDIO:
                executor.submit(handle_media, file, folder / 'audio')

    @staticmethod
    def thread_amr_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.AMR_AUDIO:
                executor.submit(handle_media, file, folder / 'audio')

    @staticmethod
    def thread_flac_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.FLAC_AUDIO:
                executor.submit(handle_media, file, folder / 'audio')


...


class Video:

    @staticmethod
    def thread_mp4_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.MP4_VIDEOS:
                executor.submit(handle_media, file, folder / 'video')

    @staticmethod
    def thread_3gp_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.VIDEOS_IN_3GP:
                executor.submit(handle_media, file, folder / 'video')

    @staticmethod
    def thread_avi_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.AVI_VIDEOS:
                executor.submit(handle_media, file, folder / 'video')

    @staticmethod
    def thread_mov_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.MOV_VIDEOS:
                executor.submit(handle_media, file, folder / 'video')

    @staticmethod
    def thread_mkv_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.MKV_VIDEOS:
                executor.submit(handle_media, file, folder / 'video')


class Documents:

    @staticmethod
    def thread_txt_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.TXT_DOCS:
                executor.submit(handle_media, file, folder / 'documents')

    @staticmethod
    def thread_doc_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.DOC_DOCS:
                executor.submit(handle_media, file, folder / 'documents')

    @staticmethod
    def thread_docx_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.DOCX_DOCS:
                executor.submit(handle_media, file, folder / 'documents')

    @staticmethod
    def thread_mpp_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.MPP_DOCS:
                executor.submit(handle_media, file, folder / 'documents')

    @staticmethod
    def thread_pdf_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.PDF_DOCS:
                executor.submit(handle_media, file, folder / 'documents')

    @staticmethod
    def thread_pptx_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.PPTX_DOCS:
                executor.submit(handle_media, file, folder / 'documents')

    @staticmethod
    def thread_xlsx_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.XLSX_DOCS:
                executor.submit(handle_media, file, folder / 'documents')


class TorrentPythonExe:
    @staticmethod
    def thread_torrent_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.TORRENT_TYPE:
                executor.submit(handle_media, file, folder / 'torrents')

    @staticmethod
    def thread_application_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.APP_TYPE:
                executor.submit(handle_media, file, folder / 'applications')

    @staticmethod
    def thread_python_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.PYTHON_TYPE:
                executor.submit(handle_media, file, folder / 'python_scripts')


class AnotherTypes:

    @staticmethod
    def thread_unknown_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.ANOTHER_TYPES:
                executor.submit(handle_media, file, folder / 'uncertain_types')


class Archives:

    @staticmethod
    def thread_zip_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.ZIP_ARCHIVES:
                executor.submit(handle_archives, file, folder / 'archives')

    @staticmethod
    def thread_iso_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.ISO_ARCHIVES:
                executor.submit(handle_archives, file, folder / 'archives')

    @staticmethod
    def thread_rar_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.RAR_ARCHIVES:
                executor.submit(handle_archives, file, folder / 'archives')

    @staticmethod
    def thread_gz_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.GZ_ARCHIVES:
                executor.submit(handle_archives, file, folder / 'archives')

    @staticmethod
    def thread_tar_loop(folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in collector.TAR_ARCHIVES:
                executor.submit(handle_archives, file, folder / 'archives')


def thread_for_folders(folder: Path):
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        for folder in collector.FOLDERS[::-1]:
            executor.submit(handle_folders, folder, folder)


def main(folder: Path):
    collector.searcher(folder)
    thread_jpeg = Thread(target=Images.thread_jpeg_loop, args=(folder,))
    thread_jpg = Thread(target=Images.thread_jpg_loop, args=(folder,))
    thread_png = Thread(target=Images.thread_png_loop, args=(folder,))
    thread_svg = Thread(target=Images.thread_svg_loop, args=(folder,))
    thread_bmp = Thread(target=Images.thread_bmp_loop, args=(folder,))
    thread_jpeg.start()
    thread_jpg.start()
    thread_png.start()
    thread_svg.start()
    thread_bmp.start()
    ...
    thread_mp3 = Thread(target=Audio.thread_mp3_loop, args=(folder,))
    thread_wav = Thread(target=Audio.thread_wav_loop, args=(folder,))
    thread_ogg = Thread(target=Audio.thread_ogg_loop, args=(folder,))
    thread_amr = Thread(target=Audio.thread_amr_loop, args=(folder,))
    thread_flac = Thread(target=Audio.thread_flac_loop, args=(folder,))
    thread_mp3.start()
    thread_wav.start()
    thread_ogg.start()
    thread_amr.start()
    thread_flac.start()

    ...

    thread_mp4 = Thread(target=Video.thread_mp4_loop, args=(folder,))
    thread_3gp = Thread(target=Video.thread_3gp_loop, args=(folder,))
    thread_avi = Thread(target=Video.thread_avi_loop, args=(folder,))
    thread_mov = Thread(target=Video.thread_mov_loop, args=(folder,))
    thread_mkv = Thread(target=Video.thread_mkv_loop, args=(folder,))
    thread_mp4.start()
    thread_3gp.start()
    thread_avi.start()
    thread_mov.start()
    thread_mkv.start()

    ...

    thread_txt = Thread(target=Documents.thread_txt_loop, args=(folder,))
    thread_doc = Thread(target=Documents.thread_doc_loop, args=(folder,))
    thread_docx = Thread(target=Documents.thread_docx_loop, args=(folder,))
    thread_mpp = Thread(target=Documents.thread_mpp_loop, args=(folder,))
    thread_pdf = Thread(target=Documents.thread_pdf_loop, args=(folder,))
    thread_xlsx = Thread(target=Documents.thread_xlsx_loop, args=(folder,))
    thread_pptx = Thread(target=Documents.thread_pptx_loop, args=(folder,))
    thread_doc.start()
    thread_docx.start()
    thread_txt.start()
    thread_mpp.start()
    thread_pdf.start()
    thread_xlsx.start()
    thread_pptx.start()

    ...

    thread_torrent = Thread(target=TorrentPythonExe.thread_torrent_loop, args=(folder,))
    thread_app = Thread(target=TorrentPythonExe.thread_application_loop, args=(folder,))
    thread_python_script = Thread(target=TorrentPythonExe.thread_python_loop, args=(folder,))
    thread_torrent.start()
    thread_app.start()
    thread_python_script.start()

    ...

    thread_unknown_type = Thread(target=AnotherTypes.thread_unknown_loop, args=(folder,))
    thread_unknown_type.start()

    ...
    thread_zip = Thread(target=Archives.thread_zip_loop, args=(folder,))
    thread_iso = Thread(target=Archives.thread_iso_loop, args=(folder,))
    thread_rar = Thread(target=Archives.thread_rar_loop, args=(folder,))
    thread_gz = Thread(target=Archives.thread_gz_loop, args=(folder,))
    thread_tar = Thread(target=Archives.thread_tar_loop, args=(folder,))
    thread_zip.start()
    thread_iso.start()
    thread_rar.start()
    thread_gz.start()
    thread_tar.start()
    ...
    thread_folders = Thread(target=thread_for_folders, args=(folder,))
    thread_folders.start()
    ...


if __name__ == '__main__':
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        print(f'Sorting will start in folder -- {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())

        print('Names of all files was changed from cyrillic to latin.')
        for i in tqdm(collector.ALL_THAT_I_FOUND, desc="Sorting progress", colour='green'):
            time.sleep(0.5)
        time.sleep(2)
        print(f'And so we have this extensions in this folder:\n{collector.EXTENSIONS}\nThose files was'
              f'removed to correspond folders.')
        time.sleep(1)
        print(f'And files with this extensions we couldn\'t sort:\n{collector.UNKNOWN}\nYou can find '
              f'them in folder "uncertain_types".')
        print('Sorting finished!')
