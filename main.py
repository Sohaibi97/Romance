from tkinter import *
from email.message import EmailMessage
import ssl
import time
import smtplib

screen = Tk()
screen.title('Hi Hana')

email_sender='python.python.dyali@gmail.com'
email_password='wtrvuyimjkrumryw'
email_receiver='cherkaouiyassin29@gmail.com'
subject='Hana'
body='she just started'
em =EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)
context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


print("hello Hana i am Love and i am going to be asking you some questions today")
print("believe me, i am not doing this for fun because i rather have a calm evening but i love Sohayb and he is a good friend of mine and i wanna help him")
print("he is a really nice guy and sometimes he is smart but apparently he is not smart enough to understand you. and in his defence; you are not an open book either, \ntherefore i decided to play the role of a communication channel between you two")
answer=input("is that okay for you? and please answer all the questions using 'yes' or 'no' you can write your answer here->")
while True:
    if "yes" in answer:
        print("Ooooh great, i would love to talk to you")
        break
    elif "no" in answer:
        print("Thank you anyway beautiful for your time and wish you a happy life")
        body = 'i couldnt help amigo, Sorry:( mais hadxi kay3ni maxi 3i tina li ma9dartixi tehdar m3aha, you see:)'
        em.set_content(body)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        exit()
    else:
        print("No Hana i cannot understand sentences:( i am only able to understand the answers 'yes' or 'no'")
        answer = input("so please click here and write your answer. Here->")

print("so Sohayb told me, that you two met in a party and that you were the most beutiful in the party.\nHe also told me you both have danced together for a while and for some reason he thought you liked him, but did you really like him?")
answer=input("answer with 'yes' or 'no' here ->")
while True:
    if "no" in answer:
        answer2=input("do you think, he can change your mind?")
        if "no" in answer2:
            print("Okay Hana, thank you for honesty and much love")
            body = 'She never liked you, you Habibi ... i really cannot believe how silly you are but remember that i love you because of your stupidity alghzal dyali'
            em.set_content(body)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            exit()
        elif "yes" in answer2:
            how=input("how can he change your mind?  answer using a sentence not yes or no. You answer here here ->")
            print("Okay Love Hana, i wish you the best, you are zina :)")
            body = 'Sara7a a zin walo ma3jebtiha mais te9dar tebdl hadxi! sa9ssita kifax and she said: '+how
            em.set_content(body)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())

            exit()
        else:
            print("No Hana i cannot understand sentences:( i am only able to understand the answers 'yes' or 'no'")
            answer2 = input("so please click here and write your answer. Here->")
    elif "yes" in answer:
        answer2=input("do you still like him?")
        if "yes" in answer2:
            answer3=input("do you have someone else in your life? or do you have feelings for someone else?")
            if "yes" in answer3:
                print("Schade but it was really wonderful to get to know somebody like you:) wish you both all the best :)")
                body = 'it has nothing to do with you al7bib .... kayn li seb9ek liha w safi :( mais matnssaxi the one is just somewhere right there waiting for you'
                em.set_content(body)
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender, email_receiver, em.as_string())

                exit()

            answer3=input("Are you trying some dating strategy?")
            if "yes" in answer3:
                print("ooooh God, you are smarter than this Hana, if you like him, go and tell him, have a date, kiss him and let him love you the way you deserve to be loved. \nWhy playing? why?")
                strategy=input('what type of strategy you are using? what do you wanna achieve? answer with a sentence here->')
                body = 'Leghzal dyali, she is a bit complicated, katjareb chi dating strategy, sa9ssita chno w 9atli hadxi: '+strategy
                em.set_content(body)
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender, email_receiver, em.as_string())

            answer3=input('how could he get your heart? and how could he ask you for a date? Answer using a sentence here ->')
            print('Okay Hana thank you for your time and let me give you an advice; dont play hard to get, you found a nice guy that will really love you\na guy that will bring you flowers, kiss you everyday good morning, a guy that will cook for you even that he is not cooking for himself, so give him the chance\nand trust me he will try his best for you to never regret this decision')
            body = 'Sohaybi, ma3arfxi wax 9dart njawb 3la your questions mais sa9ssita xni te9dar te3ml and 9atli hadxi: ' + answer3
            em.set_content(body)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
        if 'no' in answer2:
            mistake=input('what did he do that you changed your mind? write your answer here->')
            print('Hey Hanna i know that he is being foolish sometimes but it is just because he liked you and he is an open book and he is so direct.\nYeah and he knows that sometimes he is too much but his best relationships are based on being too much\nand therefore he is the way he is; if he likes you, he is trying to get you and if not he is removing all the bridges between you.\nand you are amazing so he decided to cross the bridge to you so please, receive him with some love not by destroyng the bridge')
            body = 'i guess you were too much again because she said: ' + mistake
            em.set_content(body)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
    print('kantmenalk nhar zwin a zin')
    time.sleep(40)
    exit()
