from selenium import webdriver
from time import sleep
import os
mobile = ["+919013170844","+918584080803","+919521280017","+916204047040","+916204986350",
"+916371134028","+916394043246","+917044927011","+917296015006","+917388037515","+917462865810",
"+917760110589","+917808787907","+918016185675","+918084089103","+918167768266","+918240652038",
"+918529466708","+918594973316","+918676833199","+918709230250","+918874748818","+918902061363",
"+918908053439","+919007506870","+919044373785","+919118064973","+919131722908","+919155128082",
"+919337419297","+919348927700","+919389093657","+919415999269","+919438081126","+919438652311",
"+919439176495","+919439780172","+919453266709","+919504382087","+919552278690","+919570089401",
"+919583243021","+919608353431","+919669445703","+919828647472","+919836348440","+919861870246",
"+919861961648","+919899111199","+919903762004","+919937865256","+919981799644"]

message = "$ git commit -m\"Hello World\" %0a%0aDSC KIIT, Mozilla bbsr AND MSAC KIIT partnered with MAYADATA proudly present to you KIIT\'S very own HACKTOBERFEST 2020.%0a%0aA celebration of Open Source where developers and learners come together to learn, contribute and win amazing swags and prizes.%0a%0aBTW, Registrations are free%0a%0aAll the students are requested to join the Telegram group to receive further communication, registration link, instructions and benefits:%0a%0a https://t.me/joinchat/SObPQR2yfj9bJnAc68izig%0a%0aWhen is it happening?%0a%0a11th of October sharp at 4 PM.%0a%0a%0a\"An event for the learner in you.\""
driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://web.whatsapp.com')
filepath = os.path.join(os.getcwd(),'Hacktober.jpeg')

input('Enter anything after scanning QR code')
print(len(mobile))
for i in range(0,len(mobile)):
    driver.get('https://web.whatsapp.com/send?phone='+mobile[i]+'&text='+message)

    sleep(3)

    attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_box.click()

    image_box = driver.find_element_by_xpath(
        '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(filepath)

    sleep(3)

    send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
    send_button.click()
    sleep(3)