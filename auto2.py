import time
import os
import pyautogui
import webbrowser
def sendmsg_with_photo(message , mobile , imgpath):
    pyautogui.FAILSAFE =True
    webbrowser.open('https://web.whatsapp.com')
    time.sleep(10)
    for phone_no in mobile:
        if "+" not in phone_no:
            raise CountryCodeException("Country code missing from phone_no")
        url = 'https://web.whatsapp.com/send?phone='+phone_no+'&text='+message
        pyautogui.click(x=878,y=74)
        pyautogui.write(url)
        time.sleep(1)
        pyautogui.press(['delete','enter'])
        time.sleep(5)
        xy = None 
        while xy is None:
            xy=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'attach.png'),grayscale=True)
        pyautogui.click(xy)
        xy1= None 
        while xy1 is None:
            xy1=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'photo.png'),grayscale=True)
        pyautogui.click(xy1)
        time.sleep(1)
        pyautogui.write(imgpath)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)

def sendmsg_with_doc(message , mobile , filepath ,post = 0):
    pyautogui.FAILSAFE =True
    webbrowser.open('https://web.whatsapp.com')
    time.sleep(10)
    for phone_no in mobile:
        if "+" not in phone_no:
            raise CountryCodeException("Country code missing from phone_no")
        url = 'https://web.whatsapp.com/send?phone='+phone_no+'&text='+message
        pyautogui.click(x=878,y=74)
        pyautogui.write(url)
        time.sleep(1)
        pyautogui.press(['delete','enter'])
        time.sleep(6)
        if post == 0:
            pyautogui.press('enter')
            time.sleep(1)
        xy = None 
        while xy is None:
            xy=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'attach.png'),grayscale=True)
        pyautogui.click(xy)
        xy1= None 
        while xy1 is None:
            xy1=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'doc.png'),grayscale=True)
        pyautogui.click(xy1)
        time.sleep(1)
        pyautogui.write(filepath)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        if post == 1:
            pyautogui.press('enter')
        time.sleep(5)

if __name__ == '__main__':
    mobile = ['+916371134028' , '+918337925359']
    message = 'Hi! I am a bot'
    filepath = os.path.join(os.getcwd(),'pythonislove.jpg')
    sendmsg_with_photo(message, mobile , filepath)


