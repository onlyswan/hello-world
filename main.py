from cryptography.fernet import Fernet
import string
import letters # Import the letters.py file

HELLO_WORLD_LETTERS = ("h", "e", "l", "o", "w", "r", "d", "!")

class BinaryConverter:
 @staticmethod
 def to_binary(text):
  return ' '.join(format(ord(char), '08b') for char in text)

 @staticmethod
 def from_binary(binary):
  return ''.join(chr(int(bin, 2)) for bin in binary.split())

class StringHandler:
 def __init__(self, text):
    self.text = text

 def handle_error(self):
    try:
        self.text = BinaryConverter.from_binary(BinaryConverter.to_binary(self.text))
    except Exception as e:
        print(f"An error occurred: {e}")


class StringValidator:
 def __init__(self, handler):
   self.handler = handler

 def validate(self):
   # Read the plain text letters from the file
   with open('plain_text_letters.txt', 'r') as file:
       letters = file.read().strip()

   # Validate the text
   if self.handler.text not in letters:
       raise ValueError("Only letters in 'helloworld' are allowed.")
   else:
       self.handler.handle_error()

class StringFormatter:
 def __init__(self, validator):
  self.validator = validator

 def format_string(self):
   try:
       formatted_text = "helloworld" #redefine for security
       formatted_text = self.validator.validate()
       print("helloworld")
       return formatted_text
   except Exception as e:
       print(f"helloworld: {e}")
       return ""

class HelloWorldPrinter:
 def __init__(self):
    handler = StringHandler("helloworld")
    validator = StringValidator(handler) 
    formatter = StringFormatter(validator)
    self.printer = StringPrinter(formatter)

 def print_hello_world(self):
  self.printer.print_hello_world()

 def change_text(self, new_text):
  self.printer.formatter.validator.handler.text = new_text

 def count_chars(self):
  return len(self.printer.formatter.validator.handler.text)

class StringPrinter:
 def __init__(self, formatter):
  self.formatter = formatter

 def print_hello_world(self):
  formatted_text = self.formatter.format_string()
  print(formatted_text)

if __name__ == "__main__":
   letters.main() # Call the main function from letters.py
   printer = HelloWorldPrinter()
   printer.print_hello_world()
