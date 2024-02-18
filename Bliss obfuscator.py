import subprocess
from pystyle import *
from time import sleep, time
import os
from termcolor import colored

try:
    import base64
except ImportError:
    print("Installing base64 package...")
    subprocess.call(["pip", "install", "base64"])

    # Import base64 after installation
    import base64
# Print the ASCII art

# made by bliss, idk why i made this shit, but ok
dark_gray = colored("DARK GRAY", "grey")
purple = colored("PURPLE", "magenta")
text = r"""

 __        __  __                     
|  \      |  \|  \                    
| $$____  | $$ \$$  _______   _______ 
| $$    \ | $$|  \ /       \ /       \
| $$$$$$$\| $$| $$|  $$$$$$$|  $$$$$$$
| $$  | $$| $$| $$ \$$    \  \$$    \ 
| $$__/ $$| $$| $$ _\$$$$$$\ _\$$$$$$\
| $$    $$| $$| $$|       $$|       $$
 \$$$$$$$  \$$ \$$ \$$$$$$$  \$$$$$$$ 


"""[:-1]

banner = """
                         .                          
                         M                          
                        dM                          
                        MMr                         
                       4MMML                  .     
                       MMMMM.                xf     
       .              "MMMMM               .MM-     
        Mh..          +MMMMMM            .MMMM      
        .MMM.         .MMMMML.          MMMMMh      
         )MMMh.        MMMMMM         MMMMMMM       
          3MMMMx.     'MMMMMMf      xnMMMMMM"       
          '*MMMMM      MMMMMM.     nMMMMMMP"        
            *MMMMMx    "MMMMM\    .MMMMMMM=         
             *MMMMMh   "MMMMM"   JMMMMMMP           
               MMMMMM   3MMMM.  dMMMMMM            .
                MMMMMM  "MMMM  .MMMMM(        .nnMP"
    =..          *MMMMx  MMM"  dMMMM"    .nnMMMMM*  
      "MMn...     'MMMMr 'MM   MMM"   .nMMMMMMM*"   
       "4MMMMnn..   *MMM  MM  MMP"  .dMMMMMMM""     
         ^MMMMMMMMx.  *ML "M .M*  .MMMMMM**"        
            *PMMMMMMhn. *x > M  .MMMM**""           
               ""**MMMMhx/.h/ .=*"                  
                        .3P"%....                   
                      nP"     "*MMnx       
                  
                  
                  
                  
                  """[1:]

banner = Add.Add(text, banner, center=True)

dark = Col.dark_gray
light = Col.light_gray
purple = Colors.StaticMIX((Col.purple, Col.blue))
bpurple = Colors.StaticMIX((Col.purple, Col.blue, Col.blue))


def p(text):
    # sleep(0.05)
    return print(stage(text))

def stage(text: str, symbol: str = '...', col1 = light, col2 = None) -> str:
    if col2 is None:
        col2 = light if symbol == '...' else purple
    return f""" {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""


def obfuscate_file():
    current_folder = os.path.dirname(os.path.abspath(__file__))
    System.Size(150, 47)
    System.Title("Bliss [SIMPLE] obfuscator")
    Cursor.HideCursor()
    print()
    print(Colorate.Diagonal(Colors.DynamicMIX((purple, dark)), Center.XCenter(banner)))
    print('\n')
    file_path = input(stage("Drag the file you want to obfuscate ", symbol="->", col2=bpurple)).replace('"', '').replace("'", "")
    try:
        with open(file_path, 'r') as file:
            code = file.read()

        obfuscated_code = base64.b64encode(code.encode()).decode()

        file_name = input(stage("Name for the obfuscated file ", symbol="->", col2=bpurple))
        if not file_name.endswith(".py"):
            file_name += ".py"
        obfuscated_filepath = os.path.join(current_folder, file_name)

        with open(obfuscated_filepath, 'w') as file:
            file.write("import base64\n\n")
            file.write("exec(base64.b64decode('''" + obfuscated_code + "'''.encode()).decode())")

        print("File obfuscated and saved successfully!")
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")

obfuscate_file()