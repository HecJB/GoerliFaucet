
# GoerliFaucet

Automate QuickNode Goerli Faucet requests using Python and Playwright.

---

## Overview

This project provides a Python script to automate the process of requesting Goerli testnet ETH from the [QuickNode Goerli Faucet](https://faucet.quicknode.com/ethereum/goerli). It uses Playwright to control a Chromium browser, fill in your Goerli wallet address, and submit the faucet request.

> **Note:** The faucet requires connecting a wallet (e.g., MetaMask), and may include CAPTCHA challenges that require manual intervention.

---

## Features

- Automates browser interaction with QuickNode Goerli faucet.
- Fills in wallet address and submits request.
- Uses Playwright, a modern browser automation library.
- Easy to customize with your Goerli wallet address.

---

## Requirements

- Python 3.7 or higher
- [Playwright for Python](https://playwright.dev/python/)

---

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/HecJB/GoerliFaucet.git
   cd GoerliFaucet
   ```

2. Install dependencies:

   ```
   pip install playwright
   playwright install
   ```

---

## Usage

1. Open `goerli.py` and replace the placeholder with your Goerli wallet address:

   ```
   WALLET_ADDRESS = "0xYourGoerliWalletAddressHere"
   ```

2. Run the script:

   ```
   python goerli.py
   ```

3. The script will open a Chromium browser window, navigate to the QuickNode Goerli faucet page, and attempt to automate the request process.

4. You may need to manually connect your wallet and solve any CAPTCHA challenges.

---

## Example Script Snippet

```
from playwright.sync_api import sync_playwright
import time

WALLET_ADDRESS = "0xYourGoerliWalletAddressHere"

def request_goerli_eth():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://faucet.quicknode.com/ethereum/goerli")

        # Wait for page to load
        page.wait_for_timeout(5000)

        # TODO: Automate wallet connection if possible
        # Fill wallet address if input available (some faucets require wallet connection instead)
        wallet_input_selector = "input[placeholder*='wallet address']"
        if page.query_selector(wallet_input_selector):
            page.fill(wallet_input_selector, WALLET_ADDRESS)
            page.click("button:has-text('Request')")
            print("Request submitted.")
        else:
            print("Wallet connection required. Please connect manually.")

        # Wait to observe results or complete CAPTCHA
        time.sleep(30)
        browser.close()

if __name__ == "__main__":
    request_goerli_eth()
```

---

## Important Notes

- The faucet requires a wallet connection (MetaMask or other) and may not allow fully automated requests.
- CAPTCHA challenges may require manual solving.
- Faucet tokens have no real monetary value and are for testing purposes only.
- Use responsibly and do not abuse the faucet.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
