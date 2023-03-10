# -*- coding: utf-8 -*-
""" helpers.py """
__author__ = 'abdullahbozdag'
__creation_date__ = '18.02.2023'

from typing import Optional

import requests


def usernames():
    return [
        "inancgumus",
        "grkn",
        "seyfoyun",
        "gorkemcetin",
        "fatihhayri",
        "burakdonertas",
        "muratcorlu",
        "gunbatimi",
        "ahmetb",
        "CanDeger",
        "yakuter",
        "umutluoglu",
        "esesci",
        "eser",
        "firatdemirel",
        "dashersw",
        "umutgokbayrak",
        "fatih",
        "tayfunerbilen",
        "cagataykurt",
        "osmancelik",
        "aydantasdemir",
        "eayurt",
        "lagrimacanta",
        "milikkan",
        "koziLife",
        "FerdiCildiz",
        "Atinux",
        "duybir",
        "SelmanKahyaX",
        "barisakin",
        "ademilter",
        "saucecover",
        "farukec",
        "Ammarceker",
        "codeforwhat",
        "ZaferAyan",
        "kaldiroglu",
        "srhtcn",
        "ahmetcigsar",
        "izniburak",
        "ilkerkurtel",
        "huseyinbabal",
        "yanolacagidi",
        "atifceylan",
        "EmirKarsiyakali",
        "scihan",
        "kandemir",
        "rizasabuncu",
        "berilKarabulut",
        "erkan_erol_",
        "aslanon",
        "iskenderalper",
        "elowendark",
        "emredipi",
        "ulusalomer1",
        "celilbozkurt",
        "mdisec",
        "MertSusur",
        "frkntplglu",
        "fkadev",
        "hopehero3",
        "sezeriltekin",
        "fatihacet",
        "CoderBora",
        "menzilcim",
        "ifndefgt",
        "YGelistiriciler",
        "oozn",
        "damla_ygmr",
        "yigitalpciray",
        "alionurozdemir",
        "tunayani",
        "omursonerozer",
        "c__dursun",
        "Yemregundogmus",
        "mstfvrdl",
        "azmimengu",
        "omer_colakoglu",
        "AltugAkgul",
        "deusmur",
        "denizirgin",
        "pissang1",
        "zekeriyamulbay",
        "onatm",
        "deadponyclb",
        "BaranGenez",
        "selimdoyranli",
        "uysallmustafa",
        "gokhansengun",
        "reymoloji",
        "nlycskn",
        "zeynepnurdilek",
        "strheberga",
        "mervederbeder",
        "cansualtunn",
        "DevrimGunduzTR",
        "povderpinkdream",
        "YTolun",
        "eda__ercan",
        "mertcangokgoz",
        "mstrYoda_",
        "oncekiyazilimci",
        "eyvahmett",
        "gokhanadev",
        "kazmaadam21",
        "0gxd14g",
        "TRbilisimvakfi",
        "Renaittre",
        "terskaplumbaa",
        "glcebru",
        "0guzKilic",
        "nurvekotuseyler",
        "AskeriMuhendiss",
        "demirbasayyuce",
        "bilal0rnek",
        "Gizemm_Cobann",
        "AbtoncDev",
        "umuterdogan000",
        "muratozakcill",
        "eserozvataf",
        "mhcifci",
        "buradabirisi",
        "aysscbn17",
        "cans3ray",
        "ahmetbcakici",
        "bloacko",
        "yazilimci_adam",
        "ssserhatli",
        "kubraderlermis",
        "ibrahimery1",
        "kosansuu",
        "utkusen",
        "Enginnblt",
        "iremaltnz_",
        "baskindev",
        "evrn_tan",
        "betulisover",
        "10VBacik",
        "meyusufdemirci",
        "brsyldrm_9",
        "busracetinellii",
        "hizliemre26",
        "erhnml",
        "guvendik_ahmet",
        "beyzamadenoglu",
        "metinaksu_28",
        "melihkrhmet28",
        "iremkomurcu",
        "EylemGokdemir05",
        "mhk_developer",
        "yasingaziturk",
        "salihoktayakar",
        "iamyusufonder",
        "antfu7",
        "ezgiturali",
        "mihribansahinnn",
        "kevstopcu",
        "esmovski",
        "mustafa_namoglu",
        "faridaelchuzade",
        "BestamiNuri",
        "mertcobanov",
        "demirkoparann_",
        "tanmehmet06",
        "elificlk",
        "aayseaktag",
        "onurschu",
        "glshrdnr",
        "benfurkankilic",
        "coderspace_io",
        "ozcandroid",
        "baranymo",
        "devalpaca",
        "Wincase_",
        "sayin_karahanli",
        "birceste",
        "secalaban",
        "DidemKkkaraasl1",
        "_lothlorien_0",
        "baristunar",
        "mervenoyann",
        "0xfahrettin",
        "ysnce26",
        "alipempe",
        "dogancna",
        "erinanakiiri",
        "zypylmzz",
        "SerhanYavcin",
        "edakarakkus",
        "dashersw_TR",
        "safaorhanTR",
        "yazilimcikisi",
        "myavuzyalcintas",
        "apo_bozdag",
        "nubisqueendom",
        "trendyoltech",
        "boratalemdar",
        "nilpotentmatris",
        "fiercebudd",
        "alioksuzdev",
        "humeyrabnl",
        "karahanax",
        "dogrulllk",
        "elifbilgepp",
        "startupekibi",
        "emrecanakisik2",
        "yuricagla",
        "blocktheunity",
        "tubalptekin",
        "imays3gul",
        "ceyylan__",
        "ebrardev",
        "DoanDadelen5",
        "BerkantCen",
        "IdilAlemdar",
        "asimcanyagizz",
        "berk1ya",
        "_NoFearr_",
        "yakupinho",
        "kaansen97",
        "trusilca",
        "aslinurtolga",
        "merpassenger",
        "Harss78",
        "SugeXBT",
        "berkayKuzu_",
        "HaticeDaglidev",
        "AyeTok02463593",
        "FikretAkincom",
        "Ensdrms16",
        "PelinHngs",
        "fatih24yavuz",
        "kalenderbdrum",
        "cansucavuldak_",
        "muffafa",
        "berkan2109_",
        "devkarayagiz",
        "bilisoftenginar",
        "eserxp",
        "Sezer1123435",
        "acikyazilimagi",
        "BerkantCen",
        "berkbirkan",
        "gzc_mrt",
        "mustfgnn",
        "cemalbasargan",
        "ogunaryus",
        "KurtayVedat",
        "hakanakcivi",
        "talhafaki",
        "ilkerdemirx",
        "ey_machina",
        "kivilgym",
        "aykutsarach",
        "MahmutGundogdu",
        "umayecek",
        "msrexe",
    ]


def labels():
    return [
        "software", "hardware", "game", "sport", "politics", "economy",
        "company", "brand", "person", "computer", "phone", "programming",
        "health", "education", "science", "art", "music", "movie", "book",
        "food", "travel", "weather", "nature", "animal", "plant", "vehicle",
        "building", "furniture", "clothing", "tool", "weapon", "medicine",
        "religion", "language", "country", "city", "town", "village", "street",
        "house", "apartment", "office", "school", "university", "hospital",
        "factory", "shop", "market", "restaurant", "cafe", "bar", "hotel",
        "bank", "park", "garden", "forest", "mountain", "sea", "lake", "river"
    ]


def translate(text, target_language) -> Optional[str]:
    from dotenv import load_dotenv
    load_dotenv()
    import os

    google_api_key = os.environ.get('google_translate_api_key')
    url = "https://translation.googleapis.com/language/translate/v2"
    params = {
        "key": google_api_key,
        "q": text,
        "target": target_language,
        "format": "text"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["data"]["translations"][0]["translatedText"]
    else:
        return None
