
APP_NAME = "Extension Maker"
APP_SIZE = "1200x800"
EXTENSION_NAME_MAX_LENGTH = 75
EXTENSION_DESCRIPTION_MAX_LENGTH = 132
EXTENSION_SHORT_NAME_MAX_LENGTH = 12 
MANIFEST_VERSION_LIST = ["2","3"]
EXTENSION_SIZE = [128,64,48,32]

def EXTENSION_ICON():
    icon ={}
    for size in EXTENSION_SIZE:
        icon[str(size)] = "data/icons/"+str(size)+".png"
    return icon    


BROWSER_MANIFEST_VERSION_3_PERMISSIONS = ["tabs","tabCapture","activeTab","storage","contextMenus","alarms","audio","background","bookmarks","browsingData","clipboardRead","clipboardWrite","contentSettings","cookies","debugger","declarativeContent","declarativeNetRequest","declarativeNetRequestFeedback","declarativeContent","desktopCapture","dns","documentScan","downloads","downloads.open","enterprise.deviceAttributes","enterprise.platformKeys","fileBrowserHandler","favicon","fontSettings","gcm","geolocation","identity","idle","identity.email","loginState","management","nativeMessaging","offscreen","pageCapture","platformKeys","power","printerProvider","privacy","processes","proxy","scripting","search","sessions","signedInDevices","storage","system.cpu","system.display","system.memory","system.storage","tabHide","topSites","tts","ttsEngine","unlimitedStorage","vpnProvider","wallpaper","webAccessibleResources","webNavigation","webRequest","webRequestBlocking","webstore","windows","system.display","system.memory","system.storage","tabHide","topSites","tts","ttsEngine","unlimitedStorage","vpnProvider","wallpaper","webAccessibleResources","webNavigation","webRequest","webRequestBlocking"]

MANIFEST_HOST_PERMISSIONS = ["<all_urls>", "*://*/*","*://youtube.com/*","*://google.com/*"]

CREATE_EXTENSION_FILE = ["background", "content", "interface", "options"]

MANIFEST ={
   "2":{
       "background":{
           "scripts": ["background.js"]
       },
       "browser_action":{
           "default_icon":EXTENSION_ICON(),
            "default_popup": "data/interface/popup.html",
            "default_title": "__MSG_app_name__"
       },
       "options_page": "data/options/options.html",
       "content_scripts": [
            {
                "matches": ["<all_urls>"],
                "js": ["content-script.js"],
                "run_at": "document_start",
                "all_frames": True
            }
        ]

    },
    "3":{
        "background":{
           "service_worker": "background.js"
       },
       "action":{
           "default_icon":EXTENSION_ICON(),
            "default_popup": "data/interface/popup.html",
            "default_title": "__MSG_app_name__"
       },
       "options_ui":{
           "page": "data/options/options.html",
            "chrome_style": True
       },
       "content_scripts": [
            {
                "matches": ["<all_urls>"],
                "js": ["content-script.js"],
                "run_at": "document_start",
                "all_frames": True
            }
        ]
    }
}

LIBERY = {
    "jquery-3.6.0.min": "https://code.jquery.com/jquery-3.6.0.min.js",
    "bootstrap.min": "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css",
    "fontawesome": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css",
    "react.dev":"https://unpkg.com/react@18/umd/react.development.js",
    "react-dom.dev":"https://unpkg.com/react-dom@18/umd/react-dom.development.js",
    "react.pro":"https://unpkg.com/react@18/umd/react.production.min.js",
    "react-dom.pro":"https://unpkg.com/react-dom@18/umd/react-dom.production.min.js",
    "vue.global":"https://unpkg.com/vue@3/dist/vue.global.js",
    "angular.min":"https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js",
    "anime.min":"https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"
}