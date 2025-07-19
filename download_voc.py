from pathlib import Path
from ultralytics.utils.downloads import download

def download_voc():
    dir = Path('datasets/VOC/images')
    urls = [
        "https://github.com/ultralytics/assets/releases/download/v0.0.0/VOCtrainval_06-Nov-2007.zip",
        "https://github.com/ultralytics/assets/releases/download/v0.0.0/VOCtest_06-Nov-2007.zip",
        "https://github.com/ultralytics/assets/releases/download/v0.0.0/VOCtrainval_11-May-2012.zip",
    ]
    download(urls, dir=dir, curl=True, threads=3, exist_ok=True)

if __name__ == "__main__":
    download_voc()
