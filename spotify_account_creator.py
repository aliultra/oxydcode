import requests #کتابخانه ریکوئست پیش نیاز اجرا
import string 
import random #ماژوال رندوم برای تولید اعداد و حروف تصادفی
import pyperclip #پیش نیاز کپی و دسترسی به کلیپ برد

def getRandomString(length): #تولید اعداد و حروف
    pool=string.ascii_lowercase+string.digits
    return "".join(random.choice(pool) for i in range(length))

def getRandomText(length): #Chars
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))

def main():
    print("[+] Spotify Account Creator - اکانت ساز اسپاتیفای [+]")
    import time; time.sleep(2)
    print('''

 ██████╗ ██╗  ██╗██╗   ██╗██████╗ ██╗███████╗██╗   ██╗
██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝██╔══██╗██║██╔════╝╚██╗ ██╔╝
██║   ██║ ╚███╔╝  ╚████╔╝ ██║  ██║██║█████╗   ╚████╔╝ 
██║   ██║ ██╔██╗   ╚██╔╝  ██║  ██║██║██╔══╝    ╚██╔╝  
╚██████╔╝██╔╝ ██╗   ██║   ██████╔╝██║██║        ██║   
 ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝╚═╝        ╚═╝   
   By OxydCode (Shaemi - Ghandi | Koochi - Talaee)
                                                                  
     ''')
    import time; time.sleep(1)
    print("[!] Connecting...")
    import time; time.sleep(1)
    
    nick = getRandomText(8) #یوزرنیم رندوم
    passw = getRandomString(8) #پسورد رندوم
    email = nick+"@"+getRandomText(5)+".com" #ایمیل رندوم
    
    payload = {"creation_point": "client_mobile", #مشخصاتی که در صفحه ثبت نام ثبت میشوند
            "gender": "male", #ثبت جنسیت
            "birth_year": 1995, #ثبت تاریخ تولد
            "displayname": nick, #ثبت یوزرنیم
            "iagree": "true", #ثبت موافقت با قوانین ثبت نام
            "birth_month": 4, #ثبت ماه تولد
            "password_repeat": passw, #ثبت تکرار پسورد رندوم
            "password": passw, #ثبت پسورد رندوم
            "key": "142b583129b2df829de3656f9eb484e6",
            "platform": "Android-ARM", #مدل دستگاه
            "email": email, #ثبت ایمیل فیک تعریف شده
            "birth_day": 9} #روز تولد
    
    headers={"Accept-Encoding": "gzip", 
             "Accept-Language": "en-US", #صفحه انگلیسی ثبت نام
             "Connection": "Keep-Alive", #ثبت ایپی خودمون (هندوراس)
             "Content-Type": "application/x-www-form-urlencoded", 
             "Host": "spclient.wg.spotify.com",
             "User-Agent": "Spotify/8.6.16 Android/22 (SM-N976N)",
             "Spotify-App-Version": "8.6.16",
             "App-Platform": "Android", #سیستم عامل (OS)
             "X-Client-Id": getRandomString(32)}

    print("[-] Requesting...\n") #درخواست ورود به صفحه ثبت نام
    r = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account/', headers=headers, data=payload)
    if r.status_code==200:
        if r.json()['status']==1: #وضعیت 1 یعنی موفقیت آمیز
            print("[!] Account created successfully!") #اکانت ساخته شد
            print("[-] Nickname: "+nick) #خروجی مشخصات اکانت ساخته شده
            print("[-] Email: "+email)
            print("[-] Password: "+passw)
            print("[-] Username: "+r.json()["username"])
            import time; time.sleep(1)
            print("\n[+] Profile copied!")
            dash = " - "
            sp = " "
            dote = ":"
            mtext = "Email"
            ptext = "Password"
            pyperclip.copy(mtext +dote +sp +email +dash +ptext + dote +sp +passw) #کپی مشخصات

            import time; time.sleep(10)
            print("\n\n[✖] Closing...") #اعلان بسته شدن نرم افزار
            import time; time.sleep(10)

        else: #در صورت ناموفق بودن (در غیر این صورت)
            print("Could not create the account - اکانت ساخته نشد") #پیغام ناموفق 
            print("Response error:")  
            print(r.json()['errors']) #نمایش نوع ارور
    else:
        print("Could not load the page, some errors occurred - صفحه بارگیری نشد ، خطایی روی داد. Response code:", r.status_code) #و اگر سایت درخواست ورود را تایید نکرد (در غیر این صورت) پیام... را بنویس

if __name__ == "__main__":
    main()