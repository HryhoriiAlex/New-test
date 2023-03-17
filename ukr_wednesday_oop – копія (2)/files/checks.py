import keyboard as k, pyautogui as p, webbrowser as wb, random, os, time, pyperclip as pc, datetime, speedtest
import sys, math
import pyttsx3, openai
from files.commands import commands
from files.menu import Menu
from deep_translator import GoogleTranslator


st = None
try:
    st = speedtest.Speedtest()
except:
    pass

class Open:
    def __init__(self, a):
        self.a = a
        if "брауз" in self.a:
            wb.open("https://www.google.com/")
        if "відео" in self.a:
            wb.open("https://www.youtube.com/")
        if "провідн" in self.a:
            k.press_and_release("win + e")
        if "калькул" in self.a:
            os.system("calc")
        if "гені" in self.a:
            wb.open("https://chat.openai.com/chat")


class Check:
    global st
    def __init__(self):

        self.words = {
            "three words": [
                "Я вас слухаю ", 
                "Завжди до ваших послуг ", 
                "Я вас уважно слухаю ",
                "Я завжди готова допомогти ",
                "Я залюбки послухаю вас ",
                "Я завжди радий бути корисним ",
                "Я до ваших послуг ",
                "Я завжди прислухаюсь до ваших потреб ",
                "Я залюбки надам вам допомогу ",
                "Я рада бути корисною ",
                "Я готова допомогти "],

            "more two": [
                "Зараз виконаю ",
                "Виконаю пане ",
                "Негайно зроблю ",
                "Зроблю відразу ", 
                "Виконаю миттєво ", 
                "Зроблю без зволікань ", 
                "Негайно виконаю ", 
                "Відразу виконаю ", 
                "Виконаю швидко ", 
                "Негайно зроблю це "]
        }
        
        self.commands = commands
        self.ser = "пане"
        self.print = True
        self.do = False

        self.sleep_time = 0.5
        self.st = st
        
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Natalia")
        self.engine.setProperty("rate", 150)

        # Змінні нагадування
        self.remind_var = False
        self.remind_message = None
        self.remind_end_time = 0
        self.remind_time = 0

        openai.api_key = "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"
    
    def check(self, a):
        
        self.a = a
        if len(a) == 0:
            l = self.words["three words"]
            self.say_text(random.choice(l)+self.ser)

        if len(self.a) > 2:
            l = self.words["more two"]
            self.say_text(random.choice(l)+self.ser)

        for a in self.a: #перевірки на різні команди
            try:
                # print(a)
                if "(комбінація)" in a:
                    self.do = True
                    k.press_and_release(a[2])
            
                if "(прогамма)" in a:
                    if "відкр" in a[0]:
                        self.do = True
                        os.startfile(a[2])
                if "(сайт)" in a:
                    if "відкр" in a[0]:
                        self.do = True
                        wb.open(a[2])
            except:
                pass
            
            if "пауз" in a:
                self.do = True
                k.press_and_release("space")

            if a == ["змін", "мов"]:
                self.do = True
                k.press_and_release("shift + ctrl")

            if "кладк" in a:
                self.do = True
                self.tab(a)

            if "відкр" in a: 
                self.do = True
                try:
                    Open(a[1])
                except:
                    pass

            if "пошук" in a or "по шук" in a:
                self.do = True
                
                wb.open("https://www.google.com/search?q="+a[1])

            if "напиш" in a or "на пиш" in a:
                self.do = True
                for chair in a[1]:
                    pc.copy(chair)
                    k.press_and_release("ctrl + v")
                    time.sleep(0.05)

            if "нотат" in a:
                self.do = True
                self.notatks(a)

            if "почек" in a:
                time.sleep(2)

            if "котр" in a and "годин" in a:
                self.print2(f'Відповідь: {datetime.datetime.now().strftime("%H:%M")} ' + self.ser)
                self.say_text(f'{datetime.datetime.now().strftime("%H:%M")} ' + self.ser)
            
            if "добр" in a and "день" in a:
                self.print2(f'Добрий день '+self.ser)
                self.say_text(f'Добрий день '+self.ser)
            
            if a == ["до", "побач"]:
                print(f'Відповідь: Допобачення ' + self.ser)
                self.say_text(f'допобачення ' + self.ser)
                sys.exit()
            
            if a == ["відправ"] or a == ["зайд"]:
                self.do = True
                k.press_and_release("enter")
            
            if a == ['видал']:
                self.do = True
                k.press_and_release("delete")
            
            if "звук" in a or "гучн" in a:
                self.do = True
                self.sound(a)

            if a == ["менш", "вікн"] or a == ["більш", "вікн"]:
                self.do = True
                p.moveTo(1920/2, 1080/2)
                p.doubleClick()

            if a == ["швидк", "інтернет"]:
                self.internet_speed()
            
            if a == ["перезапуск"]:
                self.do = True
                os.startfile("friday.py")
                sys.exit()
            
            if a == ["очист"]:
                self.do = True
                k.press_and_release("win + d")

            if a == ["став"]:
                self.do = True
                k.press_and_release("ctrl + v")

            if a == ["береж"]:
                self.do = True
                k.press_and_release("ctrl + s")

            if a == ["копі"]:
                self.do = True
                k.press_and_release("ctrl + c")
            
            if a == ["виділ"]:
                self.do = True
                k.press_and_release("ctrl + a")

            if a == ["сьогод", "дат"]:
                x = datetime.datetime.now()
                self.print2(f"{x.day}.{x.month}.{x.year}")
                self.say_text(f"{x.day}.{x.month}.{x.year}")
            
            if a == ["скрін"]:
                self.do = True
                p.press("printscreen")

            if a == ["консол"]:
                os.system("start cmd")
            
            if "нагад" in a and "хвилин" in a:
                self.remind(a)
            
            if a == ["пуст", "секундомір"]:
                self.secundomer("запусти")
            
            if a == ["зупин", "секундомір"]:
                self.secundomer("зупини")
            
            if "покаж" in a and "карт" in a:
                self.do = True
                wb.open(f"https://www.google.com.ua/maps/place/{a[2].strip()}")
            
            if a == ["кільк", "нагад"]:
                self.ckilk()

            if "меню" in a:
                Menu().open_menu()
            
            if "допомож" in a:
                self.help(a)
            
            if "намал" in a:
                self.paint(a)

            if self.a[-1] != a:
                time.sleep(self.sleep_time)

        if self.do == True:
            l = ["Виконано ", "Готово "]
            self.print2(random.choice(l)+self.ser)
            self.say_text(random.choice(l)+self.ser)
            self.do = False
        
    def print2(self, a):
        if self.print == True:
            print(f"Відповідь: {a}")

    def say_text(self, text):
        
        self.engine.say(text)
        self.engine.runAndWait()
    
    def paint(self, a):
        self.say_text("Створюю "+self.ser)
        translated = GoogleTranslator(source='ukrainian', target='english').translate(a[1]+"у напів-реалістичному стилі")

        try:
            response = openai.Image.create(
                prompt=translated,
                n=1,
                size="512x512"
            )
            image_url = response['data'][0]['url']
            wb.open(image_url)
            self.say_text("Готово "+self.ser)
        except:
            self.say_text("Щось пійшло не так "+self.ser)
    
    def secundomer(self, types):
        if types == "запусти":
            self.time_secundomer = time.time()
            self.say_text("Виконано "+self.ser)
        if types == "зупини":
           timee = int(time.time() - self.time_secundomer)
           self.print2(f"{timee} секунд", self.ser)
           self.say_text(f"{timee} секунд", self.ser)
    
    def ckilk(self):
        with open("files\system_files\\remind.txt", "r", encoding="utf-8") as remind:
            read = remind.readlines()


        if len(read) != 0:
            time_remind = round(float("".join(read[2].split("\n"))) - time.time())

            if time_remind < 60:
                print("До нагадування залишилося "+str(time_remind)+" секунд "+self.ser)
                self.say_text("До нагадування залишилося "+str(time_remind)+" секунд "+self.ser)
            else:
                minuts = time_remind // 60
                seconds = time_remind % 60
                print("До нагадування залишилося "+str(minuts)+" хвилин "+str(seconds)+" секунд "+self.ser)
                self.say_text("До нагадування залишилося "+str(minuts)+" хвилин "+str(seconds)+" секунд "+self.ser)
            
        else:
            print("Ви не просили вам, що небудь нагадати "+self.ser)
            self.say_text("Ви не просили вам, що небудь нагадати "+self.ser)
    
    def help(self, a):
        text = a[1]
        cop = False
        chit = False

        if "копі" in text:
            cop = True
        if "чит" in text:
            chit = True
        
        dele = ["скопіює", "скопіюють", "прочитай", "прочитає", "прочитаю", " оа ", " о "]
        for i in dele:
            text = "".join(text.split(i))
        
        text = text.strip(" ")
        self.say_text("Я думаю")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )
        print(response['choices'][0])
        if cop == False:
            self.print2(f"{response['choices'][0]['text'].encode('utf_16','strict').decode('utf_16', 'strict')}")
            if chit == True:
                self.say_text(" ".join(response['choices'][0]['text'].split(" ")[:40]))
        else:
            pc.copy(response['choices'][0]['text'])
            self.print2(f"{response['choices'][0]['text']}")
            self.say_text("Виконано "+self.ser)

    def remind(self, a):
        if a[2] != "None":
            self.remind_var = True
            self.remind_message = a[2]
            self.remind_time = a[3]
            self.remind_end_time = time.time() + self.remind_time*60

            with open("files\system_files\\remind.txt", "w", encoding="utf-8") as remind:
                remind.writelines([self.remind_message+"\n", str(self.remind_time)+"\n", str(self.remind_end_time)+"\n"])
            
            print(f"Добре, нагадаю вам {self.remind_message} через {self.remind_time} хвилин "+self.ser)
            self.say_text(f"Добре, нагадаю вам {self.remind_message} через {self.remind_time} хвилин "+self.ser)
        else:
            print("Повторіть будьласка")
            self.say_text("Повторіть будьласка")

    def internet_speed(self):
        try:
            self.print2(f"Перевіряю швидкість інтернету "+self.ser)
            self.say_text(f"Перевіряю швидкість інтернету "+self.ser)
            download = self.st.download()
            upload = self.st.upload()
            self.print2(f"середня швидкість інтернету - {round((round(download/1_000_000)+round(upload/1_000_000))/2)} Mbit/s "+self.ser)
            self.say_text(f"середня швидкість інтернету - {round((round(download/1_000_000)+round(upload/1_000_000))/2)} мегобайт в секунду"+self.ser)
        except:
            self.print2(f"У вас немає інтернету "+self.ser)
            self.say_text(f"У вас немає інтернету "+self.ser)
    
    def sound(self, a):
        if a == ["вимкн", "звук"] or a == ["вімкн", "звук"]:
            k.press_and_release("D")
        
        if a == ["більш", "гучн"] or a == ["більш", "звук"]:
            for i in range(5):
                p.press("volumeup")
            
        if a == ["менш", "гучн"] or a == ["менш", "звук"]:
            for i in range(5):
                p.press("volumedown")
        
        elif type(a[1]) == int:
            try:
                if a[1] != 0:
                    p.press('volumedown', presses = 50) #sets volume to zero
                    time.sleep(0.01) #using time.sleep to space the presses 
                    x = math.floor(a[1] / 2) #setting the amount of presses required
                    p.press('volumeup', presses = x) #setting volume
                else:
                    k.press_and_release("D")
            except:
                self.do = False
                self.say_text("Щось пійшло не так!")
    
    def notatks(self, a):
        if "покаж" in a or "відобраз" in a:
            k.press_and_release("alt + x")
        if "схов" in a:
            k.press_and_release("alt + z")
        if "налашт" in a:
            k.press_and_release("alt + c")
        if "створ" in a:
            k.press_and_release("alt + s")

    def tab(self, a):
        if "нов" in a:
            k.press_and_release("ctrl + t")
        if "поперед" in a or "минул" in a:
            k.press_and_release("ctrl + shift + tab")
        if "наступн" in a:
            k.press_and_release("ctrl + tab")
        if "закр" in a:
            k.press_and_release("ctrl + w")
        if "віднов" in a:
            k.press_and_release("ctrl + shift + t")
    
