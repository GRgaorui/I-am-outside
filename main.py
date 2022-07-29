import win32con
import win32gui
import pyautogui
import time
import win32clipboard as wincld

def set_text(info):
    wincld.OpenClipboard()
    wincld.EmptyClipboard()
    wincld.SetClipboardData(win32con.CF_UNICODETEXT, info)
    wincld.CloseClipboard()

def open_in_school():
    hwnd = win32gui.FindWindow("WeChatMainWndForPC", u"微信")
    if hwnd != 0:
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWMAXIMIZED)
        win32gui.SetForegroundWindow(hwnd)
        pyautogui.moveTo(200 ,200)
        inschool_location = pyautogui.locateCenterOnScreen('data/inschool.png',confidence=0.9)
        while inschool_location is None:
            pyautogui.scroll(100)
            inschool_location = pyautogui.locateCenterOnScreen('data/inschool.png',confidence=0.9)
        if inschool_location is not None:
            pyautogui.click(inschool_location.x,inschool_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
            print("check  inschool.png  image")
            time.sleep(5)
            students_location = pyautogui.locateCenterOnScreen('data/students.png',confidence=0.9)
            if students_location is not None:
                pyautogui.click(students_location.x,students_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                print("check  students.png  image")
                time.sleep(10)
                allow_location = pyautogui.locateCenterOnScreen('data/allow.png',confidence=0.9)
                if allow_location is not None:
                    pyautogui.click(allow_location.x,allow_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                    print("check  allow.png  image")
                    time.sleep(5)
            else:
                print('erro')

def check_in(temperature):
    hwnd = win32gui.FindWindow("Chrome_WidgetWin_0", u"我在校园")
    if hwnd != 0:
        win32gui.SetForegroundWindow(hwnd)
        location = pyautogui.locateCenterOnScreen('data/checkin.png',confidence=0.9)
        while location is None:
            pyautogui.scroll(-8)
            location = pyautogui.locateCenterOnScreen('data/checkin.png',confidence=0.9)
        if location is not None:
            pyautogui.click(location.x,location.y,clicks=1,interval=0.2,duration=0.2,button='left')
            print("check  checkin.png  image")
            time.sleep(5)
            health_location=pyautogui.locateCenterOnScreen('data/check_health.png',confidence=0.9)
            if health_location is None:
                health_location=pyautogui.locateCenterOnScreen('data/health.png',confidence=0.9)
                if health_location is not None:
                    pyautogui.click(health_location.x,health_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                    print("check  health.png  image")
            no_location = pyautogui.locateCenterOnScreen('data/no.png',confidence=0.9)
            while no_location is None:
                pyautogui.scroll(-10)
                no_location=pyautogui.locateCenterOnScreen('data/no.png',confidence=0.9)
            if no_location is not None:
                pyautogui.click(no_location.x,no_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                print("check  no.png  image")
                temperature_location = pyautogui.locateCenterOnScreen('data/temperature.png',confidence=0.9)
                while temperature_location is None:
                    pyautogui.scroll(-10)            
                    temperature_location=pyautogui.locateCenterOnScreen('data/temperature.png',confidence=0.9)
                if temperature_location is not None:
                    pyautogui.click(temperature_location.x,temperature_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                    print("check  temperature_location.png  image")
                    pyautogui.press(['backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'])
                    pyautogui.typewrite(str(temperature))
                    pos_location = pyautogui.locateCenterOnScreen('data/location.png',confidence=0.90)
                    while pos_location is None:
                        pyautogui.scroll(-10)
                        pos_location = pyautogui.locateCenterOnScreen('data/location.png',confidence=0.90)
                    if pos_location is not None:
                        pyautogui.click(pos_location.x,pos_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                        print("check  location.png  image")
                        time.sleep(1) 
                        submit_location = pyautogui.locateCenterOnScreen('data/check_in_submit.png',confidence=0.90)
                        while submit_location is None:
                            pyautogui.scroll(-10)            
                            submit_location = pyautogui.locateCenterOnScreen('data/check_in_submit.png',confidence=0.90)
                        if submit_location is not None:
                            pyautogui.click(submit_location.x,submit_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                            print("check  check_in_submit.png  image")
                            ok_location = pyautogui.locateCenterOnScreen('data/check_in_ok.png',confidence=0.90)
                            if ok_location is not None:
                                pyautogui.click(ok_location.x,ok_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                                print("check  check_in_ok.png  image")
                                win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
    pass

def select_list(list_img,target_img,ok_img,x=0,y=0):
    location = pyautogui.locateCenterOnScreen('data/' + list_img,confidence=0.9)
    if location is not None:
        pyautogui.click(location.x,location.y,clicks=1,button='left')
        print('check '+list_img+' image')
        pyautogui.moveTo(location.x + x,location.y + y)
        time.sleep(0.1)
        report_location_reason = pyautogui.locateCenterOnScreen('data/' + target_img,confidence=0.90)
        while report_location_reason is None:
            pyautogui.scroll(-70)
            report_location_reason = pyautogui.locateCenterOnScreen('data/' + target_img,confidence=0.90)
        if report_location_reason is not None:
            pyautogui.click(report_location_reason.x,report_location_reason.y,clicks=1,button='left')
            print("check  "+ target_img +"  image")
            report_ok = pyautogui.locateCenterOnScreen('data/'+ ok_img,confidence=0.90)
            pyautogui.click(report_ok.x,report_ok.y,clicks=1,button='left')
            time.sleep(5)
    pass

def report(phone_number,reason,direction):
    hwnd = win32gui.FindWindow("Chrome_WidgetWin_0", u"我在校园")
    if hwnd != 0:
        win32gui.SetForegroundWindow(hwnd)
        location = pyautogui.locateCenterOnScreen('data/report.png',confidence=0.9)
        while location is None:
            pyautogui.scroll(-50)
            location = pyautogui.locateCenterOnScreen('data/report.png',confidence=0.9)
        if location is not None:
            pyautogui.click(location.x,location.y,clicks=1,interval=0.2,duration=0.2,button='left')
            print("check  checkin.png  image")
            time.sleep(2)
            report1_location = pyautogui.locateCenterOnScreen('data/report1.png',confidence=0.9)
            if report1_location is not None:
                pyautogui.click(report1_location.x,report1_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                print("check  report1.png  image")
                time.sleep(2)
                select_list('report2.png','report2_5.png','report2_ok.png',y = 500)
                time_location = pyautogui.locateCenterOnScreen('data/report3.png',confidence=0.9)
                if time_location is not None:
                    pyautogui.click(time_location.x,time_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                    print("check  report3.png  image")
                    time_ok_location = pyautogui.locateCenterOnScreen('data/report2_ok.png',confidence=0.9)
                    if time_ok_location is not None:
                        pyautogui.click(time_ok_location.x,time_ok_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                        print("check  report3_ok.png  image")
                        select_list('report4.png','report4_end.png','report2_ok.png',x = -80 ,y = 350)
                        phone_number_location = pyautogui.locateCenterOnScreen('data/report5.png',confidence=0.9)
                        if phone_number_location is not None:
                            pyautogui.click(phone_number_location.x,phone_number_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                            pyautogui.typewrite(str(phone_number))
                            print("check  report5.png  image")
                            reason_location = pyautogui.locateCenterOnScreen('data/report6.png',confidence=0.9)
                            if reason_location is not None:
                                pyautogui.click(reason_location.x,reason_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                                set_text(reason)
                                pyautogui.hotkey('ctrl', 'v')
                                print("check  report6.png  image")
                                pyautogui.scroll(-500)
                                time.sleep(1)
                                direction_location = pyautogui.locateCenterOnScreen('data/report7.png',confidence=0.9)
                                if direction_location is not None:
                                    pyautogui.click(direction_location.x,direction_location.y - 10 ,clicks=1,interval=0.2,duration=0.2,button='left')
                                    print("check  report7.png  image")
                                    set_text(direction)
                                    pyautogui.hotkey('ctrl', 'v')
                                    time.sleep(2)
                                    letter_of_commitment_location = pyautogui.locateCenterOnScreen('data/report8.png',confidence=0.9)
                                    if letter_of_commitment_location is not None:
                                        pyautogui.click(letter_of_commitment_location.x,letter_of_commitment_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                                        print("check  report8.png  image")
                                        time.sleep(2)
                                        pyautogui.scroll(-1000)  
                                        time.sleep(2)  
                                        letter_of_commitment_check_location = pyautogui.locateCenterOnScreen('data/report_letter_of_commitment_check_location.png',confidence=0.9)
                                        if letter_of_commitment_check_location is not None:
                                            pyautogui.click(letter_of_commitment_check_location.x,letter_of_commitment_check_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                                            print("check  report_letter_of_commitment_check_location.png  image")
                                            read_location = pyautogui.locateCenterOnScreen('data/report_read.png',confidence=0.9)
                                            if read_location is not None:
                                                pyautogui.click(read_location.x,read_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                                                print("check  report_read.png  image")
                                                time.sleep(2)
                                                pyautogui.scroll(-1000)
                                                time.sleep(2)
                                                out_submit_location = pyautogui.locateCenterOnScreen('data/report_submit.png',confidence=0.9)
                                                if out_submit_location is not None:
                                                    pyautogui.click(out_submit_location.x,out_submit_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                                                    print("check  report_submit.png  image")
                                                    time.sleep(2)
                                                    out_ok_location = pyautogui.locateCenterOnScreen('data/report_ok.png',confidence=0.9)
                                                    if out_ok_location is not None:
                                                        pyautogui.click(out_ok_location.x,out_ok_location.y,clicks=1,interval=0.2,duration=0.2,button='left')
                                                        print("check  report_ok.png  image")
                                                        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
    pass