import json,os,asyncio,codecs
from pathlib import Path
from googletrans import Translator
from time import sleep
from requests import get
translator = Translator()


def getJson():
    file_path = 'input.json'
    if Path(file_path).is_file():
        print("[*] DONE: "+file_path+" File is Reading..")
        try:
            jsonData = json.loads(Path(file_path).read_text())
            print("[*] DONE: File Reading Complite! Your message is: "+ str(jsonData))
            return jsonData
        except ValueError as e:
            print("[*] ERROR: "+file_path+" File text is not json format!")
            return None
    
    else:
        print("[*] ERROR: "+file_path+" File not Found!")
        return None
    
def getLanguage(LANG = 'en'):
    print('')
    LANG = input("Enter Translate Language Code: ")
    if LANG =='' or LANG ==None or len(LANG) > 2:
        print("[*] ERROR: Pls Enter Valid Language not: "+ LANG)
        return None
    else:
        print("[*] DONE:Language is: "+ LANG)
        return LANG


def check_internet():
    try:
        get("http://google.com", timeout=1)
    except Exception:
        print("[*] No internet connection!")
        sleep(1)
        main()
    return


async def main():
    check_internet()
    DATA = getJson()
    LANG = getLanguage()
    if DATA!=None and LANG!=None:
        for item in DATA:
            text = DATA[item]["message"]
            translations = translator.translate(text, dest=LANG)
            print(str(item)+": "+ str(translations.text))
            DATA[item]["message"] = translations.text

        ROW_Translations = str(DATA).replace("'", '"')    
        print("[*] DONE: Translations "+ROW_Translations)
        jsonData = json.loads(ROW_Translations)

        filepath = os.path.join("_locales/"+LANG, 'messages.json')
        folder_path = "_locales/"+LANG
        if not os.path.exists(folder_path):
            print("[*] DONE: "+folder_path+" does not exist. Create "+folder_path)
            os.makedirs(folder_path)
        else:
            print("[*] ERROR: "+folder_path+" folder exists.")
            os.remove(folder_path)
            print("[*] DONE: "+folder_path+" folder is delete")
            os.remove(folder_path)
            print("[*] DONE: Recreate "+folder_path)

        with open(filepath, 'wb') as f:
            json.dump(jsonData, codecs.getwriter('utf-8')(f), ensure_ascii=False, indent=4)
            print("[*] SAVE FILE: "+filepath)

asyncio.run(main())
