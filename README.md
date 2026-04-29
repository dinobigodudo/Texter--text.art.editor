**Texter is in its alpha stage, so unexpected behavior may occur. Since the code is simple, there shouldn't be any major problems, but expect a few bugs.**

# Texter 🎨

An text art editor built in Python. Curently, texter is an fully local, python based, terminal apllication, that lets you crate, edit and manege texte arts. The artworks are saved in a JSON file, giving you a persistent library of your creations.

## Features

- ➕ **Create**: Create new text art easily* (te crate part is a bit buggy, working in a way to fix it)
- ✨ **Viewer**: See your artworks in a list based view
- 📝 **Editor**: Edit the name and content of the artworks in your gallery
- ⚙️ **Settings**: Customize the application's behavior
- 💾 **Persistence**: All artworks are automatically saved to JSON* (I not sure if affter uploading it will keep working)

## How to Use

1. Run the folowing program in texter folder location:

```bash
python Texter.py
```

2. In the main menu, you will se the following options:
    - `ver` - View existing artworks
    - `edt` - Edit or delete artworks
    - `new` - Create a new artwork
    - `cfg` - Access settings
    - `exit` - Exit the program

3.just tipe the command for what you want to do

## File Structure

- `Texter.py` - Main application file
- `artes.json` - Database of created artworks
- `configs.json` - Application settings

## Requirements

- Python 3.7+

## Settings

Currently, the application has one setting:

- **Confirm before deleting**: When enabled, it asks for confirmation before deleting an artwork

## Examples

### Creating a new artwork:

```
Enter the name of the text art: Cat
Enter the lines of the art (type 'FIM' when you're done):
                           ╱|、
                         (˚ˎ 。7
                          |、˜〵          
                          じしˍ,)ノ
FIM
```

## Notes

- Artworks are saved in JSON format with UTF-8 encoding
- You can use any Unicode character in your artworks
- The program automatically creates the JSON files on the first run* (this is the part I'm still no shure if it works)


---
*Autor: dinobigodudo*
*Licence: This project is licensed under the (will add) License. See the LICENSE file for more details.*
