# Educational Ransomware
This is an educational project to demonstrate the creation of a basic ransomware using Python. The goal is to learn and understand how encryption works in a controlled environment. This code is strictly for educational purposes and should not be used maliciously.

## Ethical Warning
This project should only be used for educational purposes, such as controlled experiments in lab environments or for portfolio demonstrations. Improper use may result in serious legal and ethical consequences.

## Features
- Encryption: The encrypter.py script encrypts files in a specified directory.
- Decryption: The decrypter.py script decrypts the files using the generated key.
- Security: Uses the cryptography library to implement secure symmetric encryption with Fernet.

# How to Use
1. Prerequisites
- Python: Make sure Python 3.x is installed. Download it here.
- cryptography library: Install the library with the following command:
```bash
pip install cryptography
```

2. Project Setup
Clone the repository:
```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```
Create a directory called target_files and add files for testing.

3. Usage
- To Encrypt
Run the encrypter.py script:
```bash
python encrypter.py
```
This will:
- Encrypt all files in target_files.
- Save the decryption key in the key.key file.
- To Decrypt
Run the decrypter.py script:
```bash
python decrypter.py
```
This will decrypt the files in target_files using the saved key.

## Project Structure
```
EducationalRansomware/
├── target_files/       # Directory with test files for encryption
├── encrypter.py        # Script to encrypt files
├── decrypter.py        # Script to decrypt files
├── key.key             # Generated decryption key (created automatically)
└── README.md           # Project documentation
```
## Technologies Used
- Python 3.x
- cryptography

## Learning
This project helps understand:
- How to implement symmetric encryption in Python.
- The logic of encrypting and decrypting files.
- How to create functional scripts for educational and portfolio purposes.

## Contributions
Contributions are welcome! To contribute:
1. Fork the project.
2. Create a branch for your changes:
```bash
git checkout -b my-branch
```
Commit your changes:
```bash
git commit -m "Educational Ransomware Project"
```
Push the changes:
```bash
git push origin my-branch
```
5. Open a Pull Request.

## Contact
If you have questions or suggestions, feel free to contact me:

- Email: nicco.dinittis@gmail.com
- GitHub: AlucinoX

## Final Note
**The purpose of this project is purely educational. Using this code for malicious activities is strictly prohibited and goes against ethical principles.**
