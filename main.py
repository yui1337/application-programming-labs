import argparse
import csv
import os

from icrawler.builtin import BingImageCrawler


def get_args() -> argparse.Namespace:
    """
    Reads arguments from terminal
    :return: Arguments

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="Keyword of search request")
    parser.add_argument("-n", "--number", type=int, help="Number of images that you want to download")
    parser.add_argument("-d", "--imgdir", type=str, help="Path to the folder, where you want to save images")
    parser.add_argument("-f", "--annotation_file", type=str, help="Path to the annotation file")
    arguments = parser.parse_args()
    return arguments


def download_images(keyword: str, number: int, imgdir: str) -> None:
    """
    This function downloads images from Bing using given keyword and directory. Also, it clears the directory every time you launch script.
    :param keyword: Search keyword
    :param number: Number of images that you want to download
    :param imgdir: Directory to save images
    """
    if not(os.path.isdir(imgdir)):
        os.mkdir(imgdir)
    for filename in os.listdir(imgdir):
        os.remove(os.path.join(imgdir, filename))
    my_crawler = BingImageCrawler(
        storage={"root_dir": imgdir, "backend": "FileSystem"},
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4)
    my_crawler.crawl(keyword=keyword, max_num=number)


def create_annotation(imgdir: str, csv_path: str) -> None:
    """
    Creates annotation (.csv file) with absolute and relative paths to images
    :param imgdir: Directory with images
    :param csv_path: .csv file that is used to write annotation
    """
    with open(csv_path, mode='w', newline='', encoding='utf-8') as annotation_file:
        writer = csv.writer(annotation_file)
        headers = ['Relative path', 'Absolute path']
        writer.writerow(headers)

        for file in os.listdir(imgdir):
            relative_path = os.path.relpath(file, start=imgdir)
            absolute_path = os.path.abspath(file)
            writer.writerow([relative_path, absolute_path])


class ImageIterator:
    def __init__(self, csv_path) -> None:
        self.csv_path = csv_path
        self.path_list = self.load_csv()
        self.limit = len(self.path_list)  # ограничение
        self.counter = 0  # счётчик

    def __iter__(self) -> 'ImageIterator':
        return self

    def __next__(self) -> str:
        if self.counter < self.limit:
            next_element = self.path_list[self.counter]
            self.counter += 1
            return next_element
        else:
            raise StopIteration

    def load_csv(self) -> list:
        with open(self.csv_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader) # skip the header
            path_list = list(row[1] for row in reader)
            return path_list


def main() -> None:
    args = get_args()
    download_images(args.keyword, args.number, args.imgdir)
    create_annotation(args.imgdir,args.annotation_file)
    my_iterator = ImageIterator(args.annotation_file)
    for item in my_iterator:
        print(item)

if __name__ == "__main__":
    main()
