# To automate job application process on linkedin
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from linkedin_credentials import *
import time
timeout = time.time() + 60*4
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
s = Service("A:\Webservices ML\chromedriver (2).exe")
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.NAME, "session_key").send_keys(username)
driver.find_element(By.NAME, "session_password").send_keys(password)
driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
time.sleep(5)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3005830512&f_JT"
           "=I&geoId=102713980&keywords=data%20science&location=India")
time.sleep(5)
# driver.find_element_by_class_name("jobs-search-box__submit-button").click()
all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")
# For applying in the first job listing
# for listing in all_listings:
#     print(f"called, {listing.text}")
#     listing.click()
#     time.sleep(2)
#
#     # Try to locate the apply button, if can't locate then skip the job.
#     try:
#         apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
#         apply_button.click()
#         time.sleep(5)
#
#         # If phone field is empty, then fill your phone number.
#         phone = driver.find_element_by_class_name("fb-single-line-text__input")
#         if phone.text == "":
#             phone.send_keys(username)
#
#         submit_button = driver.find_element_by_css_selector("footer button")
#
#         # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
#         if submit_button.get_attribute("data-control-name") == "continue_unify":
#             close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
#             close_button.click()
#             time.sleep(2)
#             discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
#             discard_button.click()
#             print("Complex application, skipped.")
#             continue
#         else:
#             submit_button.click()
#
#         # Once application completed, close the pop-up window.
#         time.sleep(2)
#         close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
#         close_button.click()
#
#     # If already applied to job or job is no longer accepting applications, then skip.
#     except NoSuchElementException:
#         print("No application button, skipped.")
#         continue

# For saving all the job listings in a file
with open("job_listings.txt", "w") as f:
    for listing in all_listings:
        f.write(listing.text + "\n")

# For saving all the job listings in linkedin
for listing in all_listings:
    print(f"called, {listing.text.strip().split(' ')[0:3]}")
    listing.click()
    time.sleep(2)
    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-save-button")
        apply_button.click()
        time.sleep(5)
    except NoSuchElementException:
        print("No save button, skipped.")
        continue
