# Exif

## Description

If only the password were in the image?

![Target Image](https://github.com/Pawat49/CTFlearn/blob/eb84e9be982996dcec03b00889be7f29cfefe6d9/exif/c3158790-353b-4bec-9af2-9ba62a6d6b4f.jfif)

[Download Image](https://mega.nz/#!SDpF0aYC!fkkhBJuBBtBKGsLTDiF2NuLihP2WRd97Iynd3PhWqRw)

## Solution

The title and description strongly suggest the flag is hidden in the EXIF metadata of the image.

1. Download the image from the provided link.
2. Upload the image to an EXIF metadata viewer such as [exifinfo.org](https://exifinfo.org/).
3. Look through the output properties to find the hidden flag.

![EXIF Viewer Output](https://github.com/Pawat49/CTFlearn/blob/80e479956b2cd8399e54dc793910413319f94ff2/exif/Screenshot%202026-05-26%20131310.png)

## Flag

`flag{3l1t3_3x1f_4uth0r1ty_dud3br0}`