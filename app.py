import os
import fire
from termcolor import colored
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def main(website="https://www.google.com/", drivertype="chrome", screen_filename="screenshot.png", do_login=False):
    cwd = os.getcwd() + ":"
    if cwd not in os.environ["PATH"]:
        print(f"Adding {cwd=} to PATH")
        os.environ["PATH"] = os.environ["PATH"] + ":" + cwd
    else:
        print(f"{cwd=} is in {os.environ['PATH']=}")
 
    drv = None

    if drivertype == "chrome":
        chrome_opt = Options()
        chrome_opt.add_argument("--headless")
        chrome_opt.add_argument("--window-size=1920x1080")

        chrome_path = os.path.join(os.getcwd(), "chromedriver")
        print(colored(f"Using {chrome_path=}", "yellow"))

        drv = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_opt)

    elif drivertype == "firefox":
        drv = webdriver.Firefox()
        drv.set_window_size(1920, 1080)

    else:
        print("So sorry, we only support `drivertype` of: `firefox` or `chrome`")
        sys.exit(1)

    drv.get(website)
    drv.save_screenshot(screen_filename.replace(".png", "_1.png"))
    
    if do_login:
        login(drv)
        drv.save_screenshot(screen_filename.replace(".png", "_login.png"))

    drv.close()

    print(f"Done crawling {website=} with {screen_filename=} using {drivertype=}")


def login(drv):
    uname = drv.find_element(By.CSS_SELECTOR, "input[name='entered_login']")
    passw = drv.find_element(By.CSS_SELECTOR, "input[name='entered_password']")
    submt = drv.find_element(By.CSS_SELECTOR, "input[type='submit']")

    print(f"Found {uname=}\n{passw=}\n{submt=}")

    uname.clear()
    uname.send_keys(os.environ["GENTLEWEB_USERNAME"])
    passw.send_keys(os.environ["GENTLEWEB_PASSWORD"])
    submt.click()
    

if __name__ == "__main__":
    fire.Fire(main)
