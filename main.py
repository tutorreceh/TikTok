import requests
import time

def print_colored_text(text, color_code):
    print(f"{color_code}{text}\033[0m")

def main():
    required_prefix = "https://www.tiktok.com/aweme/v2/aweme/"
    green_color = "\033[92m"
    blue_color = "\033[94m"
    red_color = "\033[91m"  # Menambahkan kode warna merah
    reset_color = "\033[0m"

    # Print big colored text
    big_text = r""" 
  _____ _   _ _____ ___  ___   ___ ___ ___ ___ _  _ 
 |_   _| | | |_   _/ _ \| _ \ | _ \ __/ __| __| || |
   | | | |_| | | || (_) |   / |   / _| (__| _|| __ |
   |_|  \___/  |_| \___/|_|_\ |_|_\___\___|___|_||_|
                                                     
                                                              
"""
    print_colored_text(big_text, green_color)

    report_count = 0

    while True:
        url = input("Please enter the Report URL from inspect: ")

        # Check if the URL starts with the required prefix
        if not url.startswith(required_prefix):
            print_colored_text("Wrong URL, please enter the Report URL from inspect!", blue_color)
            continue  # Ask for the URL again

        while True:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    report_count += 1
                    print_colored_text(f"Successfully Reported | Reports count: {report_count}", green_color)
                elif response.status_code == 400:
                    print_colored_text("Report Error", red_color)
                    break  # Exit the inner loop if there's an error (status code 400)
                else:
                    print_colored_text(f"Unexpected status code: {response.status_code}", blue_color)
                    break  # Exit the loop for unexpected status codes
                
                time.sleep(1)  # Wait for 1 second before making the next request
            except requests.exceptions.RequestException as e:
                print_colored_text(f"An error occurred: {e}", red_color)
                break  # Exit the inner loop if there's an error

if __name__ == "__main__":
    main()
