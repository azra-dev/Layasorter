# ✨LAYASORTER✧˖°.
A simple Manyland archived world sorter, organizing all items by types from [Area Backup](https://areabackup.com/) website. It also group all the items that belongs in their corresponding holder at HOLDER folder.

<p align="center">
. ݁  ⸰𖥔 ͙ࣳ ⸰ֺ⭑✨
<img src="https://static.wikia.nocookie.net/metamo-ark/images/d/dc/Nbg13_layerzero.png/revision/latest?cb=20180711125216" alt="a layazero" width="128">
✨ˏˋ°•⁀➷
</p>

## How to Use ⋆ˊˎ- °
### **Basics ⊹ˋˏ݁₊**
The application is straightforward as it is, you will be needing:
- the **source folder directory**, which is the extracted backup world
- the **destination folder directory**, which is the folder you would like to have your backup world to be sorted
  - There is also a 📂 icon for you to pick a directory easily with a directory picker, no need to manually type the path!

After which, you may now press the **Sort button** after accomplishing the two text field, given that both directories are valid. There will be an **Error message** in red at the bottom if any of the inputs are invalid path.

<img src="https://raw.githubusercontent.com/azra-dev/Layasorter/main/assets/prototype_1.png" alt="a layazero" width="512">

### **During Sorting ⊹ˋˏ݁₊**
If successful, the sorter starts running and processing all the items into the new directory.
- The sorter is **still running** if the inputs are still disabled/grayed out.
- Otherwise, the sorter is **finished** after the inputs are enabled once again.

<img src="https://raw.githubusercontent.com/azra-dev/Layasorter/main/assets/prototype_2.png" alt="a layazero" width="512">


## Download ⋆ˊˎ- °
### 🪄 [Windows (.exe)](https://github.com/azra-dev/Layasorter/blob/main/dist/layasorter.exe)

## Dependencies ⋆ˊˎ- °
If you decide to clone this repository, here are the following libraries you will be needing in latest version of Python (3.12.x):
- flet
- pillow

## Issues ⋆ˊˎ- °
There are still minor UI inconsistencies can be found around.
Additionally, error handling in directories are not polished, as it may cause exception if the source folder directory exist but it does not contain `creations` and `holders` folders.
