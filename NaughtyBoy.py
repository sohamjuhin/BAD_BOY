import webbrowser
import time

ad_url = "https://example.com/advertisement"
num_ads = 10

def generate_ads():
    for _ in range(num_ads):
        webbrowser.open_new_tab(ad_url)
        time.sleep(1)

if __name__ == "__main__":
    generate_ads()
