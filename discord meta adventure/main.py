from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import subprocess
import time
from time import sleep
a = subprocess.check_output('cd', shell=True)
chromedriver = a[0:len(a)-2].decode()+"\chromedriver.exe"

chat = input('Введите ссылку на чат   ')
message = input('Введите текст сообщения   ')
token = str(input('Введи токен   '))
count = int(input('Сколько раз отправлять сообщения?   '))
delay = int(input('Задержка в секундах    '))
starthour = int(input('Во сколько часов начать    '))
startminute = int(input('Во сколько минут начать    '))


options = Options()
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.set_capability('dom.webdriver.enabled', False)

driver = webdriver.Chrome(options=options, executable_path=chromedriver)

#OTQwNzU5NTI5NTQ3NzcxOTk2.YgMFwA.QQF2FjRFGP-YkEq_rGRMyu7tKeg
#https://discord.com/channels/925786953448824842/945754001658490971
driver.get(chat)
sleep(5)
script = '''function login(token) {
    setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
        location.reload();
    }, 2500);
}
login('%s');''' % (token)
print(script)
driver.execute_script(script)

sleep(10)
while True:
    if time.localtime(time.time()).tm_hour >= starthour:
        if time.localtime(time.time()).tm_min >= startminute:
            break
        else:
            pass
    else:
        pass
for i in range(count):
    try:
        msg_xpath = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[3]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div/div')


        msg_xpath.send_keys(message)
        msg_xpath.send_keys(Keys.ENTER)
        msg_xpath.send_keys(Keys.ENTER)
        sleep(delay)
    except Exception:
        try:
            msg_xpath.clear()
        finally:
            i-=1
            pass


