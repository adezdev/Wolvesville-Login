# Wolvesville Authentication and Turnstile Bypass Script

This Python script is designed to automate the process of bypassing the Cloudflare Turnstile challenge and logging into the Wolvesville authentication API. It uses several Python libraries for HTTP requests, timezone handling, and colorized console outputs.

---

## Features

- **Turnstile Challenge Bypass**: Automates bypassing the Cloudflare Turnstile using the SCTG API.
- **Token Management**: Retrieves a JSON Web Token (JWT) for secure communication with Wolvesville servers.
- **Automated Login**: Logs into Wolvesville accounts using email and password credentials.
- **Timestamp Logging**: Provides detailed timestamps for every operation.

---

## Requirements

### Prerequisites

Ensure you have the following installed before running the script:

- **Python**: Version 3.6 or higher.
- **Python Libraries**: Install the required libraries using `pip`.

### Installation

Install the required Python libraries by running:
```bash
pip install requests pytz colorama
```

---

## File Structure

The project consists of a single Python script file that performs all functionalities.

### Script Overview

#### Imports
- **`os`**: Used to clear the console for better visibility.
- **`datetime` and `pytz`**: Handle timezone-specific timestamps.
- **`requests`**: Manage HTTP communication with APIs.
- **`time`**: Introduce delays during the Turnstile bypass process.
- **`colorama`**: Provides colorized output for better readability.

#### Functions and Classes

1. **Helper Functions**:
   - `getTime()`: Returns the current time in the `Asia/Ho_Chi_Minh` timezone.
   - `getUtcTime()`: Returns the current UTC time.

2. **Class: `Login`**:
   - `__init__(self, key)`: Initializes a new session and stores the API key.
   - `turnstile()`: Automates the process of bypassing the Turnstile challenge using SCTG API.
   - `getToken()`: Retrieves a JWT token using the bypassed Turnstile token.
   - `login()`: Logs into Wolvesville using email and password credentials.

3. **Main Function**:
   - Clears the console, initializes the `Login` object, and sequentially executes the bypass and login steps.

---

## Setup

1. **Clone or Download**
   Download the repository or clone it using Git:
   ```bash
   git clone https://github.com/adezdev/Wolvesville-Login.git
   ```

2. **Configure the API Key**
   Obtain an API key from the SCTG service. Update the `key` variable in the `main()` function with your key:
   ```python
   key = 'your_api_key_here'
   ```

3. **Update Credentials**
   Replace the placeholder email and password in the `login()` method with your Wolvesville account credentials:
   ```python
   data = {
       'email': 'your_email@example.com',
       'password': 'your_password',
   }
   ```

---

## Usage

1. **Run the Script**
   Execute the script from the terminal:
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the name of the Python file.

2. **Expected Output**
   The script will display step-by-step progress:
   ```plaintext
   [15:30:45] ➩ Starting process...
   [15:30:45] ➩ UTC Time: 2023-04-05 08:30:45
   Task ID: 12345678
   [15:30:55] ➩ Bypass Turnstile Done!
   [15:31:00] ➩ JWT Token obtained!
   [15:31:05] ➩ Login successful!
   ```

---

## Troubleshooting

### Common Errors

1. **API Key Issues**:
   - Ensure the provided API key is valid and correctly entered.
   - If the key is invalid, the script will display an error.

2. **Login Errors**:
   - Verify the email and password credentials.
   - Check if Wolvesville servers are online.

3. **Module Not Found**:
   - Install the required dependencies using `pip`.

### Debugging Tips

- Use print statements to inspect variables at various points in the script.
- Check the API documentation for SCTG and Wolvesville for updates on required parameters.

---

## Notes

- This script is for **educational purposes only**. Ensure you have permission to access and use the services involved.
- Protect sensitive information, such as API keys and account credentials. Do not share them publicly.

---


