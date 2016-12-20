# KiCad off line fp

Using KiCad footprint offline!

**updated: work with kicad 4.0.4**

ADD pretty footprint (StefanHamminga and KiCad) all in one folder for offline usage.

- stefan https://github.com/StefanHamminga/
- official https://github.com/KiCad/

Require **python**, **git** to run under windows

## all-in-one

You can use the following steps,

```bash
$ # modify overwrite-fp.py, change username to your own user name
$ git submodule update --init --recursive
$ python overwrite-fp.py
$ # change KIGITHUB in your KiCad
```

That's all!

You can go further, customize your offline kicad footprint using the methods described below.

## step 1. locate `fp-lib-table` in KiCad

This file are usually placed at the `C:\Users\username\AppData\Roaming\kicad` folder. Replace `username` with your own user name.

## step 2. clone all pretty footprint into a local folder

Create a local folder, say `C:/kicad_offline`.

Put `fp-lib-table` into `./kicad` and rename this file with a suffix `.orig`.

Calling `clone-kicad-official.py` using python (code modified from `codeboy2k`). Clone (`git clone x`) pretty modules specified by `fp-lib-table.orig` into `./kicad`.

## step 3. regenerate the `fp-lib-table` file

Use `overwrite-fp.py`. It will:

  1. Generate `fp-lib-table` for all the modules in the folder specified by `localdir`. It will generate a new footprint table using `KIGITHUB` environment variable.
  2. copy the regenerating `fp-lib-table` to KiCad data folder. This folder is usually placed at `C:\Users\username\AppData\Roaming\kicad`. Change all the line with `(type github)` to `(type KiCad)` in this file.

## step 4. modify `KIGITHUB`

Open KiCad, pointing `KIGITHUB` to the localdir.

## Appendix A. update-fp.py

**(deprecated) use `git submodule update --recursive` instead**

Update. (`git pull x`) all the subfolders under `localdir`.
code modified from `codeboy2k`

## Appendix B. kicad2submodule.py

Make submodules (`git submodule add x`) specified by `fp-lib-table` in `kicad/share/template` folder, and make them as the submodule in current folder.

Should run `only once` under your git repo.

## Appendix C. add other repos

you may try `clone-kicad-sh.py` to clone the footprint made by stefan.
