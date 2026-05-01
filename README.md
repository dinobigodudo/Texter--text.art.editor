**Texter is in its alpha stage, so unexpected behavior may occur. Since the code is simple, there shouldn't be any major problems, but expect a few bugs.**

# Texter 🎨

A text art editor built in Python. Currently, Texter is a fully local, Python-based terminal application that lets you create, edit, and manage text art. Artworks are saved in a JSON file, providing a[...]  

## Features

- ➕ Create: Create new text art easily* (the creation part is a bit buggy; I'm currently working on a fix).  
- ✨ Viewer: View your artworks in a list-based view.  
- 📝 Editor: Edit the name and content of the artworks in your gallery.  
- ⚙️ Settings: Customize the application's behavior.  
- 💾 Persistence: All artworks are automatically saved to JSON* (I'm not sure if it will keep working after uploading).  

## How to Use

1. Run the following program in the Texter folder location:

```bash
python Texter.py
```

2. In the main menu, you will see the following options:  
    - `ver` - View existing artworks  
    - `edt` - Edit or delete artworks  
    - `new` - Create a new artwork  
    - `cfg` - Access settings  
    - `exit` - Exit the program

3. Just type the command for the action you want to perform.

## File Structure

- `Texter.py` - Main application file  
- `artworks.json` - Database of created artworks  
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
- The program automatically creates the JSON files on the first run* (this is the part I'm still not sure if it works)


---
*Author: dinobigodudo*

*License: This project is licensed under the MIT License. See the LICENSE file for more details.*

*Be aware that this project has AI-generated code in it, but I plan on remaking it from the ground up when I trust my coding skills; sorry for using AI :*