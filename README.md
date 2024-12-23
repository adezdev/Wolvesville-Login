Wolvesville Login Script
This Python script automates the login process to the Wolvesville website. It performs the following tasks:

Bypasses the Cloudflare Turnstile verification.
Obtains a JWT token.
Logs into the Wolvesville account using the provided credentials.
Prerequisites
Python 3.x
Required Python packages: requests, pytz, colorama
Installation
Before running the script, you need to install the required Python packages. You can do this by running:

pip install requests pytz colorama
Usage
Clone the repository or download the script file.
bash
git clone <repository-url>
cd <repository-directory>
Open the script file and replace the email and password in the login method with your Wolvesville account credentials.
Python
data = {
    'email': 'your_email@example.com',
    'password': 'your_password',
}
Run the script.
python login_script.py
Script Explanation
Functions
getTime(): Returns the current time in the Asia/Ho_Chi_Minh timezone.
getUtcTime(): Returns the current UTC time.
Classes
Login: Handles the login process.

__init__(self, key): Initializes the Login class with the provided API key.
turnstile(self): Bypasses the Cloudflare Turnstile verification and obtains the turnstile token.
getToken(self): Uses the turnstile token to get a JWT token.
login(self): Logs into the Wolvesville account using the provided credentials and JWT token.
Main Function
main(): Clears the console, prints the starting process message, initializes the Login class with the API key, and performs the login process.
Example
bash
$ python login_script.py
[09:00:00] ➩ Starting process...
[09:00:00] ➩ UTC Time: 2024-12-23 02:50:00
Task ID: 123456
[09:00:10] ➩ Bypass Turnstile Done!
[09:00:20] ➩ JWT Token obtained!
[09:00:30] ➩ Login response: {'idToken': 'abc123', ...}
[09:00:30] ➩ Login successful!
Notes
Ensure you have the correct API key and account credentials.
This script is for educational purposes only. Use it responsibly.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to customize the README file as per your needs. If you encounter any issues or have any questions, please open an issue in the repository.
