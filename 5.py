import colorama
from colorama import Fore, Back, Style

# Initialize colorama to enable colored text
colorama.init(autoreset=True)

# Display some key features of the colorama library
print("Colorama Key Features:")
print(Fore.RED + "This text is red.")  # Change text color to red
print(Back.YELLOW + "This text has a yellow background.")  # Change background to yellow
print(Style.BRIGHT + "This text is bright.")  # Make text bright
print(Style.RESET_ALL + "Style reset to default.")  # Reset styles

# Clean up by deinitializing colorama
colorama.deinit()
