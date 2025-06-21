# Pyfuzz
a python fuzzy finder for the CLI

--- 

## Table Of Contents:
[General Use](#general-use)
  [current-dir option](#current-dir-option)
  [folders option](#folders-option)
  [both option](#both-option)
  [show-hidden option](#show-hidden-option)
[setup](#setup)

---

## General Use:
the command takes one addition the text to look for so for example `pyfuzz to` it will look for anything that has to in it 
even if it isn't the first appearance of it there are multiple options tho:
- `--current-dir` is to choose specifically which direcotry to look in since by default it looks at the directory you are in
- `--folders` is used to list folders too since by default it looks at files only
- `--both` use this to look at everything files and directories
- `--show-hidden` is to list hidden folders too because by default it shows only non-hidden items not hidden

---

## current-dir option:
use this option to choose which directory to look at because by default it looks at the directory you are currently in
it needs to be a directory nothing else and its syntax is `pyfuzz <keyWord> --current-dir <full/path/to/direcotry>`

--- 

## folders option:
use this options to show folders too because by default it shows only files its syntax is `pyfuzz <keyWord> --folders`

--- 

## both option:
use this option to show everything files and folders and its syntax is `pyfuzz <keyWord> --both`

---

## show-hidden option:
use this option to show hidden items because by default it shows non-hidden only its syntax is `pyfuzz <keyWord> --show-hidden`

---

## setup
- install the program from [this link](https://github.com/Omar-Arabi1/Pyfuzz/releases/download/V1.0/pyfuzz.tar.xz)
- extract it
- move it to /usr/local/bin through `sudo mv <path_to_installed_file> /usr/local/bin`
- add this to the path `export PATH=$PATH:/usr/local/bin/pyfuzz` to ~/.bashrc
- run `source ~/.bashrc`

---

that is it dumbass