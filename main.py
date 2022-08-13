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
    collection_of_images = {}

    def __init__(self, files):
        self.collection_of_images = {'images': [
            files['KNOWN_EXT']['JPEG'],
            files['KNOWN_EXT']['BMP'],
            files['KNOWN_EXT']['PNG'],
            files['KNOWN_EXT']['JPG'],
            files['KNOWN_EXT']['SVG'],
        ]}

    def thread_image_loop(self, folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for collection, values in self.collection_of_images.items():
                for ext in values:
                    for file in ext:
                        executor.submit(handle_media, file, folder / collection)


...


class Audio:
    collection_of_audio = {}

    def __init__(self, files):
        self.collection_of_audio = {'audio': [
            files['KNOWN_EXT']['MP3'],
            files['KNOWN_EXT']['WAV'],
            files['KNOWN_EXT']['AMR'],
            files['KNOWN_EXT']['OGG'],
            files['KNOWN_EXT']['FLAC'],
        ]}

    def thread_audio_loop(self, folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for collection, values in self.collection_of_audio.items():
                for ext in values:
                    for file in ext:
                        executor.submit(handle_media, file, folder / collection)


...


class Video:
    collection_of_video = {}

    def __init__(self, files):
        self.collection_of_video = {'video': [
            files['KNOWN_EXT']['3GP'],
            files['KNOWN_EXT']['MP4'],
            files['KNOWN_EXT']['MOV'],
            files['KNOWN_EXT']['MKV'],
            files['KNOWN_EXT']['AVI'],
        ]}

    def thread_video_loop(self, folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for collection, values in self.collection_of_video.items():
                for ext in values:
                    for file in ext:
                        executor.submit(handle_media, file, folder / collection)


class Documents:
    collection_of_documents = {}

    def __init__(self, files):
        self.collection_of_documents = {'documents': [
            files['KNOWN_EXT']['DOC'],
            files['KNOWN_EXT']['DOCX'],
            files['KNOWN_EXT']['MPP'],
            files['KNOWN_EXT']['TXT'],
            files['KNOWN_EXT']['XLSX'],
            files['KNOWN_EXT']['PPTX'],
            files['KNOWN_EXT']['PDF'],
        ]}

    def thread_documents_loop(self, folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for collection, values in self.collection_of_documents.items():
                for ext in values:
                    for file in ext:
                        executor.submit(handle_media, file, folder / collection)


class TorrentPythonExe:
    collection_of_torrent_python_exe = {}

    def __init__(self, files):
        self.collection_of_torrent_python_exe = {
            'torrents':
                files['KNOWN_EXT']['TORRENT'],
            'python_scripts':
                files['KNOWN_EXT']['PY'],
            'applications':
                files['KNOWN_EXT']['EXE']
        }

    def thread_tpe_loop(self, folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for collection, values in self.collection_of_torrent_python_exe.items():
                for file in values:
                    executor.submit(handle_media, file, folder / collection)


class AnotherTypes:
    def __init__(self, files):
        self.unknown_files = files['UNKNOWN_EXT']

    def thread_unknown_loop(self, folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for file in self.unknown_files:
                executor.submit(handle_media, file, folder / 'uncertain_types')


class Archives:
    collection_of_archives = {}

    def __init__(self, files):
        self.collection_of_archives = {'archives': [
            files['KNOWN_EXT']['GZ'],
            files['KNOWN_EXT']['RAR'],
            files['KNOWN_EXT']['ZIP'],
            files['KNOWN_EXT']['ISO'],
            files['KNOWN_EXT']['TAR'],

        ]}

    def thread_archive_loop(self, folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for collection, values in self.collection_of_archives.items():
                for ext in values:
                    for file in ext:
                        executor.submit(handle_archives, file, folder / collection)


...


class Folders:
    def __init__(self, files):
        self.folders = files['FOLDERS'][::-1]

    def thread_for_folders(self, folder: Path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for folder in self.folders:
                executor.submit(handle_folders, folder)


def main(folder: Path):

    files = collector.sorter(folder)

    images_object = Images(files)
    thread_images = Thread(target=images_object.thread_image_loop, args=(folder,))
    thread_images.start()

    ...
    audio_object = Audio(files)
    thread_audio = Thread(target=audio_object.thread_audio_loop, args=(folder,))
    thread_audio.start()

    ...
    video_object = Video(files)
    thread_video = Thread(target=video_object.thread_video_loop, args=(folder,))
    thread_video.start()

    ...
    documents_object = Documents(files)
    thread_documents = Thread(target=documents_object.thread_documents_loop, args=(folder,))
    thread_documents.start()

    ...
    three_in_one_object = TorrentPythonExe(files)
    thread_3in1 = Thread(target=three_in_one_object.thread_tpe_loop, args=(folder,))
    thread_3in1.start()

    ...
    unknown_type_object = AnotherTypes(files)
    thread_unknown_type = Thread(target=unknown_type_object.thread_unknown_loop, args=(folder,))
    thread_unknown_type.start()
    ...
    archives_object = Archives(files)
    thread_archives = Thread(target=archives_object.thread_archive_loop, args=(folder,))
    thread_archives.start()
    ...
    thread_images.join()
    thread_audio.join()
    thread_documents.join()
    thread_video.join()
    thread_archives.join()
    thread_3in1.join()
    thread_unknown_type.join()
    ...
    folders_object = Folders(files)
    thread_folders = Thread(target=folders_object.thread_for_folders, args=(folder,))
    thread_folders.start()
    ...
    return files


if __name__ == '__main__':
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        print(f'Sorting will start in folder -- {folder_for_scan.resolve()}')
        data = main(folder_for_scan.resolve())

        print('Names of all files was changed from cyrillic to latin.')
        for i in tqdm(data, desc="Sorting progress", colour='green'):
            time.sleep(0.5)
        for j in tqdm(data['KNOWN_EXT'], desc="Sorting known files", colour="blue"):
            time.sleep(0.1)
        for k in tqdm(data['UNKNOWN_EXT'], desc="Sorting unknown files", colour="magenta"):
            time.sleep(0.1)

        time.sleep(2)
        # print(f'And so we have these extensions in this folder:\n{collector.EXTENSIONS}\nThose files was '
        #       f'removed to correspond folders.')
        # time.sleep(1)
        # print(f'And files with these extensions we couldn\'t sort:\n{collector.UNKNOWN}\nYou can find '
        #       f'them in folder "uncertain_types".')
        time.sleep(1)
        print('Sorting finished!')
