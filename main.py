import speech_recognition as sr
import os
import webbrowser as wb
import datetime
import openai
from config import apikey




chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Yuvraj: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]






def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += response["choices"][0]["text"]

    try:
        # print(response["choices"][0]["content"])
        if not os.path.exists("Openai"):
            os.mkdir("Openai")

            # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
        with open(f"Openai/{''.join(prompt.split('ai')[1:]).strip()}.txt", "w") as f:
            f.write(text)
    except Exception as e:
        print("Some error occured")





def say(text):
    os.system(f"say {text}")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            # print(f"User said: {query}")
            return query
        except Exception as e:
            return "Sorry sir, Some Error has Occurred."





if __name__ == '__main__':
    print('PyCharm')
    say("Hello Sir, I am Jarvis. Your personal A.I assistant.")

    while True:
        query = takeCommand()
        sites = [["youtube", "https://youtube.com"],["wikipedia", "https://wikipedia.com"],["gmail", "https://gmail.com"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                wb.open(site[1])
        # say(query)

# todo: add more features
        if "play song" in query:
            musicPath = "/Users/yuvrajanand/Downloads/Music/Do_It.mp3"
            say("Playing song sir....")
            os.system(f"open {musicPath}")

        elif "the time" in query:
            print(query)
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, The time is {strfTime}")

        elif "open music".lower() in query.lower():
            say("Opening music sir")
            os.system("open /System/Applications/Music.app")

        elif "exit" in query:
            say("Always good to see you sir...")
            exit()

        elif "using AI".lower() in query.lower():
            ai(prompt=query)
        elif "reset chat".lower() in query.lower():
            chatStr = ""
        else:
            print("Chatting....")
            chat(query)