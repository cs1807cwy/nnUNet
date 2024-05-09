import glob
import os
import shutil
from pathlib import Path
from typing import List
import SimpleITK as sitk
import argparse


def copy_image(src: str, dst: str) -> None:
    img_itk = sitk.ReadImage(src)
    sitk.WriteImage(img_itk, dst)


def copy_folder(src: str, dst: str) -> None:
    dirs = Path(src).rglob('**')
    for dir in dirs:
        fdst = dst / dir.relative_to(src)
        fdst.mkdir(parents=True, exist_ok=True)
    files = Path(src).rglob('*.nii*')
    for file in files:
        fdst = dst / file.relative_to(src)
        basename = os.path.basename(fdst).split('.')[0]
        fdst = fdst.with_name(f'{basename}.nii.gz')
        copy_image(str(file), str(fdst))
        print(f'Copying {file} to {fdst}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type=str, default='F:/CBIBF3/storage/Dataset/Esophagus_1_20240314')
    parser.add_argument('--dst', type=str, default='F:/CBIBF3/storage/Dataset/Esophagus_1_niigz_20240314')
    args = parser.parse_args()
    print(args)
    copy_folder(args.src, args.dst)
