from playwright.sync_api import sync_playwright
import time

def request_goerli_eth(wallet_address: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True to run without UI
        page = browser.new_page()

        # Navigate to QuickNode Goerli faucet
        page.goto("https://faucet.quicknode.com/ethereum/goerli")

        # Wait for the wallet address input field (update selector if needed)
        # NOTE: The actual faucet UI might require connecting wallet via popup, so this is a simplified example
        page.wait_for_timeout(5000)  # Wait for page to load

        # Try to find input field for wallet address (if exists)
        # This faucet primarily wants wallet connection, so this might not be present
        # If no input, you might need to manually connect wallet or automate extension (complex)
        wallet_input_selector = "input[placeholder*='wallet address']"
        if page.query_selector(wallet_input_selector):
            page.fill(wallet_input_selector, wallet_address)
            print(f"Filled wallet address: {wallet_address}")

            # Click request button
            request_button_selector = "button:has-text('Request')"
            page.click(request_button_selector)
            print("Clicked Request button")

            # Wait to observe result
            time.sleep(10)
        else:
            print("Wallet address input not found. This faucet likely requires wallet connection.")

        # Close browser
        browser.close()

if __name__ == "__main__":
    # Replace with your Goerli wallet address
    my_wallet_address = "0xYourGoerliWalletAddressHere"
    request_goerli_eth(my_wallet_address)
