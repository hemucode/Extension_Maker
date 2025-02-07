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
    return

def getTranslation(TEXT,LANG):
    if LANG and TEXT:
        try:
            translations = translator.translate(TEXT, dest=LANG)
            return translations.text
        except:
            print("[*] ERROR: Translation NOT WORKING..")
            return None
    else:
        return TEXT  
    
def saveFile(DATA,LANG):
    if DATA == "" or DATA==None or LANG == None or LANG == "":
        return
    try:
        filepath = os.path.join("_locales/"+LANG, 'messages.json')
        folder_path = "_locales/"+LANG
        if not os.path.exists(folder_path):
            print("[*] DONE: "+folder_path+" does not exist. Create "+folder_path)
            os.makedirs(folder_path)

        with open(filepath, 'wb') as f:
            json.dump(DATA, codecs.getwriter('utf-8')(f), ensure_ascii=False, indent=4)
            print("[*] SAVE FILE: "+filepath)
    except:
        print("[*] ERROR: Not save the "+LANG+" xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")  
        print("[*] ERROR: Not save the "+LANG+" xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")  
        print("[*] ERROR: Not save the "+LANG+" xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")  
        print("[*] ERROR: Not save the "+LANG+" xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")  
        print("[*] ERROR: Not save the "+LANG+" xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")  



def getExteraName(DATA, LANG):
    extera = "Increase sound"
    try:
        translations = getTranslation(extera, LANG)
        if translations != None:
            appName = DATA+" - "+ translations
            if len(appName) < 75:
                return appName
            else:
                return DATA
        else:
            return DATA    
    except:
        print("[*] ERROR: getExteraName NOT WORKING..")
        return DATA


def containsObject(obj, list):
    for name in list:
        if name == obj:
            return True
    return False   
 
buttonTranslations = ["popup","reset","light","dark"]
LANGUAGES = [
    # 'af',
    # 'sq',
    # 'am',
    # 'ar',
    # 'hy',
    # 'az',
    # 'eu',
    # 'be',
    # 'bn',
    # 'bs',
    # 'bg',
    # 'ca',
    # 'ceb',
    # 'ny',
    # 'zh-cn',
    # 'zh-tw',
    # 'co',
    # 'hr',
    # 'cs',
    # 'da',
    'nl',
    'en',
    'eo',
    'et',
    'tl',
    'fi',
    'fr',
    'fy',
    'gl',
    'ka',
    'de',
    'el',
    'gu',
    'ht',
    'ha',
    'haw',
    'iw',
    'he',
    'hi',
    'hmn',
    'hu',
    'is',
    'ig',
    'id',
    'ga',
    'it',
    'ja',
    'jw',
    'kn',
    'kk',
    'km',
    'ko',
    'ku',
    'ky',
    'lo',
    'la',
    'lv',
    'lt',
    'lb',
    'mk',
    'mg',
    'ms',
    'ml',
    'mt',
    'mi',
    'mr',
    'mn',
    'my',
    'ne',
    'no',
    'or',
    'ps',
    'fa',
    'pl',
    'pt',
    'pa',
    'ro',
    'ru',
    'sm',
    'gd',
    'sr',
    'st',
    'sn',
    'sd',
    'si',
    'sk',
    'sl',
    'so',
    'es',
    'su',
    'sw',
    'sv',
    'tg',
    'ta',
    'te',
    'th',
    'tr',
    'uk',
    'ur',
    'ug',
    'uz',
    'vi',
    'cy',
    'xh',
    'yi',
    'yo',
    'zu']

async def main():
    DATA = getJson()
    # LANG = getLanguage()
    for LANG in LANGUAGES:
        setup(DATA, LANG)
        sleep(5)


def setup(DATA, LANG):
    check_internet()
    JsonData = {}
    if DATA!=None and LANG!=None:
        for item in DATA:
            text = DATA[item]["message"]
            if item == "app_name":
                newData = getExteraName(text, LANG)
                JsonData[item] = {"message": newData}
                print(str(item)+": "+ str(newData))
            else:
                newData = getTranslation(text, LANG)
                if newData !=None:
                    if containsObject(str(item), buttonTranslations):
                        if len(text) > len(newData) or len(text) == len(newData):
                            JsonData[item] = {"message": newData}
                            print(str(item)+": "+ str(newData))
                    else:
                        JsonData[item] = {"message": newData}
                        print(str(item)+": "+ str(newData))

             
        print("[*] DONE: Translations "+str(JsonData))
        # jsonDatas = json.loads(ROW_Translations)
        saveFile(JsonData, LANG)



asyncio.run(main())
