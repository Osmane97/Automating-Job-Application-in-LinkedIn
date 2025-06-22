
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

URL = 'https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'

#Keep chrome open
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(URL)

#Fill below information
email = your_email@example.com
password = your_password
phone_number = your_phone_number
job_type = Job_Search
location = Job_location



sleep(2)
write_email = driver.find_element(By.ID, 'username').send_keys(email)

sleep(2)
write_pwd = driver.find_element(By.ID, 'password').send_keys(password)

sleep(2)
sign_in = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Sign in"]')
sign_in.click()

# CAPTCHA - Solve Puzzle Manually
input("Press Enter when you have solved the Captcha")


sleep(2)
job_window = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a').click()




sleep(2)
job_location = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="City, state, or zip code"]').send_keys(location)
job_search = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search by title, skill, or company"]').send_keys(job_type, Keys.ENTER)


sleep(6)
easy_apply = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Easy Apply filter."]').click()

sleep(3)
expereience_lvl = driver.find_element(By.CSS_SELECTOR, 'button[id="searchFilter_experience"]').click()

sleep(2)
jobs_level = driver.find_element(By.CSS_SELECTOR, 'label[for="experience-2"]').click()


sleep(2)
show_results = driver.find_element(By.XPATH,'/html/body/div[7]/div[3]/div[4]/section/div/section/div/div/div/ul/li[5]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]' ).click()



#Close application function
def Abort_Application():
    cancel_application = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss"]')
    cancel_application.click()
    sleep(1)
    close_application = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[3]/button[1]')
    close_application.click()
    print("Complex application, skipped.")

#Job application function
def Process_job_application():
    job_lists = driver.find_elements(By.CSS_SELECTOR, 'li.ember-view.scaffold-layout__list-item')

    for i in range(len(job_lists)):
        try:
            job_lists = driver.find_elements(By.CSS_SELECTOR, 'li.ember-view.scaffold-layout__list-item')
            job_lists[i].click()
            sleep(2)  # Wait for job details to load

            try:
                apply_button = driver.find_element(By.ID, 'jobs-apply-button-id')
                apply_button.click()
                sleep(2)
                try:
                    phone_input = driver.find_element(By.XPATH,
                                                      '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4251674706-20916309306-phoneNumber-nationalNumber"]')
                    if phone_input.get_attribute('value').strip() == " ":
                        phone_input.send_keys(phone_number)
                        sleep(2)
                except NoSuchElementException:
                    print(f'job {i} phone numebr input not found')

                while True:
                    try:
                        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Submit application"]')
                        submit_button.click()
                        print('Application submitted')
                        break  # exit submission loop important

                    except NoSuchElementException:
                        pass  # move on the next option
                    try:
                        review_button = driver.find_element(By.CSS_SELECTOR,
                                                            'button[aria-label="Review your application"]')
                        if review_button.is_enabled():
                            review_button.click()
                            sleep(2)
                            continue
                        else:
                            print(f"job {i} Review button is disabled. Likely missing info.")
                            Abort_Application()
                            break

                    except NoSuchElementException:
                        pass

                    except Exception as review_error:
                        print(f"[{i}] Cannot proceed: {review_error}")
                        Abort_Application()
                        break

                    try:
                        Next_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Continue to next step"]')
                        if Next_button.is_enabled():
                            Next_button.click()
                            sleep(1)
                            continue
                        else:
                            print(f"job {i} Next button is disabled. Likely missing info.")
                            Abort_Application()
                            break

                    except NoSuchElementException:
                        Abort_Application()
                        break


            except NoSuchElementException:
                print(f'Easy Aplly not found for the job{i}')

        except StaleElementReferenceException:
            print(f"[{i}] Skipping this job — the page updated before I could click it.")
        except Exception as e:
            print(f'error encountered: {e} for the {i} job. Proceeding the next job')

#Apply for all jobs through pages
while True:
    Process_job_application()
    try:
        next_page = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="View next page"]')
        if next_page.is_enabled():
            next_page.click()
            sleep(3)
        else:
            print('No more pages found')
            break
    except NoSuchElementException:
        print('No other job pages found')
        break

