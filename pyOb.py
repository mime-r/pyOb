""" Title: Python Code Obfuscation v1.0
Author: Samuel Cheng
Date: 14/5/2021
Project Description: If you're here you probably want to make your code UNREADABLE TO THE CASUAL OBSERVER/BEGINNER AT PYTHON
Disclaimers: If you pass this to an average python coder they can probably decrypt it.
Usage:

# Important note: For this program to work, a node .py file must be made in the same working directory as the target file

from pyOb import Obfuscate

# Function 1: encode_base64
# Parameters:            CompletedCode, Filename (Point to another file or leave blank for the current file)
Obfuscate().encode_base64(True, "helloworld.py")

[completedcode]
if completedcode is true, this program will write a complete set of code for the encrypted program to be run
else if completedcode is false, this program will just leave the encrypted code in a .txt file which you can decode it later

[*args (filename)]
leave blank to convert the current code that uses this function
if not, put a filename in the current working directory (e.g. helloworld.py, test.py)

# Function 2: decode_base64
# Parameters:              Filename (Point to another file or leave blank for the current file)
Obfuscate().decode_base64("encoded_pyOb_encoded_pyOb_5109A1.txt")

[Filename]
Put a filename in the current working directory (e.g. helloworld.py, test.py) to convert

# Function 3: run
# Parameters:   Filename, visible
Obfuscate().run("encoded_pyOb_27657D.txt", False)

[Filename]
Put a filename in the current working directory (MUST BE A .txt FILE WITH ONLY THE ENCRYPTED CODE IN IT)

[visible]
If you want your decrypted code to be displayed when showing your friends, if not set visible to False

----
Example (from node file):

from pyOb import Obfuscate

Obfuscate().encode_base64(True, "helloworld.py")
----

Updates:
I am currently planning to add more encryption types but ofc you must wait. The current base64 type works. so deal with it.

----
"""


import base64, os, uuid, sys
import inspect
import datetime


class Obfuscate:
    
    
    def __init__(self):
        self.callFilename = ""
        self.logger = Logger
        self.encoded = ""
        self.decoded = ""
        self.newfilename = ""
    
    
    def encode_base64(self, completedCode, *args):
        if len(args) > 0:
            self.callFilename = f"""{os.getcwd()}\\{args[0]}"""
        else:
            self.callFilename = inspect.stack()[1].filename
        
        self.logger.log(f"Extracting from {self.callFilename}")
        with open(self.callFilename, "r") as file:
            data = file.read()
        #print(f"\n--- Before ---\n{data}")
        
        self.encoded = base64.b64encode(data.encode())
        #print(f"\n--- After ---\n{self.encoded}")
    
        self.logger.log("Checking the integrity of the encoded text...")
        self.decoded = base64.b64decode(self.encoded).decode()
        if self.decoded == data:
            self.logger.log("Passed integrity checks.")
            self.logger.log("Writing to file...")
        else:
            self.logger.fatal("Failed integrity checks. Try again.")
            sys.exit(-1)
        if completedCode:
            extension = "py"
        else:
            extension = "txt"
        self.newfilename = f"encoded_pyOb_{uuid.uuid4().hex.upper()[0:6]}.{extension}"
        with open(self.newfilename, "a") as file:
            encoded_finished = str(self.encoded)[2:-1]
            if completedCode:
                # you're lazy aren't you
                fullcode = f"""# Code written by pyOb.py at {datetime.datetime.now()} (c) Samuel Cheng
# Don't remove these comments because I made this code >:(
import base64
encrypted = "{encoded_finished}"
exec(base64.b64decode(encrypted).decode())
"""
                file.write(fullcode)
            else:
                file.write(encoded_finished)
            file.close()
            
        self.logger.log(f"Success! Saved to: {os.getcwd()}\\{self.newfilename}")
 
        
    def decode_base64(self, filename):
        self.callFilename = f"""{os.getcwd()}\\{filename}"""

        self.logger.log(f"Extracting from {self.callFilename}")
        with open(self.callFilename, "r") as file:
            data = file.read()
        #print(f"\n--- Before ---\n{data}")
        self.decoded = base64.b64decode(data).decode()

        #print(f"\n--- After ---\n{self.decoded}")
        self.logger.log("Checking the integrity of the encoded text...")
        self.encoded = base64.b64encode(self.decoded)
        if self.encoded == data:
            self.logger.log("Passed integrity checks.")
            self.logger.log("Writing to file...")
        else:
            self.logger.fatal("Failed integrity checks. Try again.")
            sys.exit(-1)
        self.newfilename = f"decoded_pyOb_{uuid.uuid4().hex.upper()[0:6]}.py"
        with open(self.newfilename, "a") as file:
            file.write(self.decoded)
            file.close()
        self.logger.log(f"Success! Saved to: {os.getcwd()}\\{self.newfilename}")
        
    
    def run(self, filename, visible):
        self.callFilename = f"""{os.getcwd()}\\{filename}"""
        self.logger.log(f"Extracting from {self.callFilename}")
        with open(self.callFilename, "r") as file:
            data = file.read()
        self.logger.log("Attempting to decode...")
        self.decoded = base64.b64decode(data).decode()
        self.logger.log("Done decoding.")
        if visible:
            print(f"\n--- {self.callFilename} ---\n{self.decoded}\n")
        self.logger.log("Running file...")
        print("\n"*100)
        exec(self.decoded)
        
        
class Logger:
    def log(this):
        print(f"[LOG] {this}")
    def fatal(this):
        print(f"[FATAL] {this}")


print("I see you are trying to run this module. Yes it's a module. Go read the comments at the top of this code for how to use it. Thank you and good bye.")
