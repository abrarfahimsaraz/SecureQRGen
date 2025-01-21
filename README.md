# SecureQRGen

**SecureQRGen** is a Python-based application that simplifies QR code creation while ensuring secure data transmission. This tool combines user-friendly graphical interfaces with robust encryption mechanisms, allowing users to generate and decrypt QR codes with enhanced data integrity and confidentiality.

## Features

- **Secure QR Code Generation:** Encodes user-provided messages into QR codes with encryption.
- **QR Code Scanning and Decryption:** Extracts and decodes encrypted messages from QR codes.
- **User-Friendly Interface:** A graphical interface built with PyQt5 for intuitive usage.
- **Image Import and Export:** Supports loading images for QR code generation and saving QR codes as PNG files.

## Technologies Used

- **Python** for backend logic and encryption.
- **PyQt5** for the graphical user interface.
- **qrcode** library for QR code generation.
- **OpenCV** for QR code scanning and image processing.
- **Base64** for message encryption and decryption.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abrarfahimsaraz/SecureQRGen.git
   cd SecureQRGen
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   > **Note:** If the `requirements.txt` file is not provided, manually install the dependencies:
   ```bash
   pip install PyQt5 qrcode opencv-python
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. Launch the application.
2. Use the **QR Code Generator** to input text, encrypt it, and generate a QR code.
3. Save the generated QR code as a PNG file for sharing or storage.
4. Use the **QR Code Scanner** to load a QR code image and retrieve the encrypted message.

## Project Structure

- `encryption.py` - Base64 encoding and decoding logic.
- `main.py` - Main application with GUI for QR code generation and scanning.
- `withEncryption.py` - Extended version with Base64 encryption integrated.
- `ORcodeUI.ui` - Qt Designer file for the graphical interface.

## Contribution

Contributions are welcome! Feel free to fork the repository, submit pull requests, or raise issues.

## Authors

- Abrar Fahim: GUI Design and Report Writing
- Muhammed Ahnaf Khan: Main Code Implementation and Troubleshooting
- Md. Ahasanul Adib: Encryption Implementation

## License

This project is licensed under the MIT License. See the LICENSE file for details.
