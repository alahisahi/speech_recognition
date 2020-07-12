import  speech_recognition as sr
import webbrowser as wb 
import time

r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()

with sr.Microphone() as source:
    print('search')
    time.sleep(2)
    print('speak now')
    audio=r3.listen(source)

if 'google' in r2.recognize_google(audio):
    r2=sr.Recognizer()
    url='https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('search the querry')
        audio=r2.listen(source)

    try:
        get=r2.recognize_google(audio)
        print(get)
        wb.get().open_new_tab(url+get)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed to get the result'.format(e))

            

