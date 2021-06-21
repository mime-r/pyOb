# pyOb
python obfuscator

Title: Python Code Obfuscation v1.0

Author: Samuel Cheng

Date: 14/5/2021

Project Description: If you're here you probably want to make your code UNREADABLE TO THE CASUAL OBSERVER/BEGINNER AT PYTHON
Disclaimers: If you pass this to an average python coder they can probably decrypt it.

Usage:
#Important note: For this program to work, a node .py file must be made in the same working directory as the target file
from pyOb import Obfuscate
#Function 1: encode_base64
#Parameters:            CompletedCode, Filename (Point to another file or leave blank for the current file)
```python
Obfuscate().encode_base64(True, "helloworld.py")
```
[completedcode]
if completedcode is true, this program will write a complete set of code for the encrypted program to be run
else if completedcode is false, this program will just leave the encrypted code in a .txt file which you can decode it later
[*args (filename)]
leave blank to convert the current code that uses this function
if not, put a filename in the current working directory (e.g. helloworld.py, test.py)
#Function 2: decode_base64
#Parameters:              Filename (Point to another file or leave blank for the current file)
```python
Obfuscate().decode_base64("encoded_pyOb_encoded_pyOb_5109A1.txt")
```
[Filename]
Put a filename in the current working directory (e.g. helloworld.py, test.py) to convert
#Function 3: run
#Parameters:   Filename, visible
```python
Obfuscate().run("encoded_pyOb_27657D.txt", False)
```
[Filename]
Put a filename in the current working directory (MUST BE A .txt FILE WITH ONLY THE ENCRYPTED CODE IN IT)
[visible]
If you want your decrypted code to be displayed when showing your friends, if not set visible to False
----
Example (from node file):
```python
from pyOb import Obfuscate
Obfuscate().encode_base64(True, "helloworld.py")
```
----
