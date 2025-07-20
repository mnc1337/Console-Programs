# Console-Programs

Package of console programs written in Python programming language. There are 4 programs that are used for different tasks. Every program is standalone and consists of executable file (.exe) and sources (files on which program is based). Programs will be also named as `tools`.  
`P.S.` **File creator** and **Temp cleaner** programs are connected with each other (one program creates files, another deletes them).

---

## Programs in package

- File creator: a tool that creates file (in `TEMP` directory) for `Temp cleaner` (is described below) to clean a directory if there is not any available for deleting file (or all files in directory are taken by other processes).

- Password generator: a tool that generates passwords based on 2 parameters:
    - length (8-32 chars);
    - charset (4 variants, only 1 can be chosen):
        - only numbers;
        - only uppercase chars;
        - only lowercase chars;
        - all variants.
    All parameters are inclusive (both points are taken into account).

- Soundwave generator: a tool that generates sound wave based on parameters:
    - sample rate (1-768000 Hz);
    - duration (1-60 seconds);
    - amplitude (float in range 0-1);
    - start (usually lowest) frequency point (≥ 1 Hz);
    - end (usually highest) frequncy point (≤ 384000 Hz).
    All parameters are inclusive.

- Temp cleaner: a tool that cleans the `TEMP` directory on your computer. Only free (not taken by other processes) files will be deleted from directory.

## Security

There is a security folder in projects structure. It contains an archive with a nested archive and an .asc file - digital signature. To check archive originality, you can download archive, extract nested archive (.7z) and .asc file from it to directory selected by you and use there the next command in Bash/WSL console: gpg --verify console_programs_archive.7z.asc console_programs_archive.7z - first parameter is a digital signature (.asc file), second parameter is an archive.

## License

This project is licensed under the MIT license. See the LICENSE file in root directory for details.

---

*2025, author: mnc1337*