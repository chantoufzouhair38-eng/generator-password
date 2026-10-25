# Password Generator

A simple Python command-line tool that generates a random password of the length you choose.

## Features

- Asks the user for the password length
- Mixes uppercase letters, lowercase letters, digits and special characters
- Prints the generated password in the terminal

## Requirements

- Python 3.x
- No external libraries (only the built-in `random` and `string` modules)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/chantoufzouhair38-eng/generator-password.git
   cd generator-password
   ```

2. Run the program:

   ```bash
   python generator_passeworde.py
   ```

3. Enter the length you want when prompted.

## Example

```
Entrez la longueur de votre code : 12
Your password is: k#9Tq!vL2@xB
```

## How it works

1. The program builds a pool of characters from `string.ascii_letters`, `string.digits` and `string.punctuation`.
2. It picks one random character from the pool for each position, using `random.choice()`.
3. It joins the characters into a single string and displays it.

## Note

This project is for learning purposes. For real-world security, use Python's `secrets` module instead of `random`, since it is designed for cryptographically secure passwords.

## Possible improvements

- Validate the input (reject negative numbers or non-numeric text)
- Let the user choose which character types to include
- Use the `secrets` module for stronger randomness
- Copy the password to the clipboard

## Author

Zouhair