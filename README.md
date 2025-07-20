# Console-Programs

Package of console programs written in Python programming language. There are 4 programs that are used for different tasks. Every program is standalone and consists of executable file (.exe) and sources (files on which program is based). Programs will be also named as `tools`.  
`P.S.` **File creator** and **Temp cleaner** programs are connected with each other (one program creates files, another deletes them).

---

## Programs in package

- File creator: a tool that creates file (in `TEMP` directory) for `Temp cleaner` (is described below) to clean a directory if there is not any available for deleting file (or all files in directory are taken by other processes). It supports creating any number of files in the next range: 1-1000. Every program running rewrites files that were created earlier using this program or that have the same name as new-generated files.


- Password generator: a tool that generates passwords based on 2 parameters (all parameters ranges are inclusive - both points are taken into account):
    - length (8-32 chars);
    - charset (4 variants, only 1 can be chosen):
        - only numbers;
        - only uppercase chars;
        - only lowercase chars;
        - all variants.


- Soundwave generator: a tool that generates sound wave based on parameters (all parameters ranges are inclusive):
    - sample rate (1-768000 Hz);
    - duration (1-60 seconds);
    - amplitude (float, range: 0-1);
    - start (usually lowest) frequency point (≥ 1 Hz);
    - end (usually highest) frequncy point (≤ 384000 Hz).

    The generated sound wave is saved as a `.wav` file (raw, uncompressed audio). Optionally, you can save a `.log` file with all file parameters, which will be created in the same directory as the sound file.


- Temp cleaner: a tool that cleans the `TEMP` directory on your computer. Usually, it's C:\Users`{User}`\Appdata\Local\Temp (User - your username in system). Only free (not taken by other processes) files will be deleted from directory. You can use one of next commands in CMD to see directory for temporary files on your computer: echo %TEMP% or echo %TMP%. Also you can choose an easier way and write temp after using the next combination: Win + R.

## Security

There is a security folder in projects structure. It contains an archive with a nested archive and an .asc file - digital signature. To check archive originality, you can download archive, extract nested archive (.7z) and .asc file from it to directory selected by you and use there the next command in Bash/WSL console: gpg --verify console_programs_archive.7z.asc console_programs_archive.7z - first parameter is a digital signature (.asc file), second parameter is an archive.

## License

This project is licensed under the MIT license. See the LICENSE file in root directory for details.

---

*2025, author: mnc1337*