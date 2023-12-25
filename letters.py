import os
import string
from pathlib import Path

def generate_word_letters(word):
  """Generate a string containing only the letters of the word"""
  return ''.join([char for char in word if char in string.ascii_letters])

def create_file(filename, content):
  """Create a file with the given filename and content"""
  try:
      with open(filename, 'w') as file:
          file.write(content)
  except IOError:
      print(f"Failed to create file {filename}")
      return False
  else:
      print(f"File {filename} created successfully")
      return True

def verify_file(filename):
  """Check if the file exists"""
  path = Path(filename)
  if path.is_file():
      print(f"The file {filename} exists")
      return True
  else:
      print(f"The file {filename} does not exist")
      return False

def main():
  # Generate a string containing only the letters of the word
  word_letters = generate_word_letters("helloworld")

  # Create a file in the current directory
  success = create_file('plain_text_letters.txt', word_letters)

  # Verify the file was created
  if success:
      verify_file('plain_text_letters.txt')

if __name__ == "__main__":
  main()
