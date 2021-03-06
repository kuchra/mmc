# -*- coding: utf-8 -*-


class Constants(object):
    # See command.py for implementation
    RESERVED_KEYWORDS = [
        ("help", "Maid-chan will show you these texts"),
        ("subscribe offerings", "Maid-chan will start sending a good morning & a good night messages"),
        ("unsubscribe offerings", "Maid-chan will stop sending you a good morning & a good night messages, but Maid-chan will be sad :'("),
        ("update offerings", "Maid-chan will keep her best to follow your waking up and sleeping time pattern!"),
        ("subscribe japanese", "Maid-chan will start sending you daily Japanese Kanji & Vocabulary"),
        ("unsubscribe japanese", "Maid-chan will stop sending you daily Japanese Kanji & Vocabulary"),
        ("update japanese", "Maid-chan will ask you about Kanji level selection (N1-N4, old test format)"),
        ("update name", "What name do you prefer to be called? onii-chan? goshujin-sama? or perhaps, ... darling?"),
        ("subscribe rss", "Maid-chan will guide you through RSS Feed subscription, e.g.: manga, nyaa"),
        ("unsubscribe rss", "Maid-chan will remove RSS Feed which you want to stop subscribing"),
        ("subscribe train", "[Experimental] Maid-chan will start sending you Tokyo train status information (currently, it only supports admin's train line :p)"),
        ("unsubscribe train", "[Experimental] Maid-chan will stop sending you Tokyo train status information"),
        ("show profile", "Maid-chan will show all information which Maid-chan knows about you"),
    ]

    FEATURES = [
        ("upload picture", "Maid-chan will convert it to a primivite image, but it might take several minutes"),
        ("simple chatbot", "Maid-chan will try her best to engage in a conversation!"),
        ("translate", "[Experimental] Maid-chan will ask Google-sensei for the translation from/to Indonesian, English, and Japanese (with language detection)")
    ]

    QUESTIONS = {
        1: "What time do you usually wake up in the morning, {}? (e.g.: 9:00)",
        2: "What time do you usually sleep, {}? (e.g.: 23:00)",
        3: "Which level of Kanji do you want to learn between N1-N4, {}? (e.g.: N3)",
        4: "How should Maid-chan call you? onii-chan? goshujin-sama? or perhaps, ... darling?",
        5: "Do you want to use preset RSS feed or add a custom one, {}? (Type 1 for preset, 2 for custom)",
        6: "Which preset do you want to use?",
        7: "Which RSS feed do you want to use? (e.g.: http://mangastream.com/rss)",
        8: "What is the title (regex pattern) that you want to use? (e.g.: Shokugeki no Soma, or .* to match all)",
        9: "Which number of subscription do you want to remove, {}?"
    }

    NORMAL_GOOD_MORNING = [
        "????????????! Wishing you a good day ahead, {} <3",
        "Ohaa~ I had a nice dream last night. Hope {} also had one!",
        "Good morning, {}. I feel you will have a nice day today!",
        "Ohayou gozaimasu, {}! Don't forget to exercise!",
        "Morning, {}. It's time to wake up :D",
        "Good morning to you, {}",
        "Ohaa~ Time to get up already, {}",
        "Guten Morgen, {}. A new day means a new hope, ???????????????!",
        "Good morning, {}! Don't forget to eat healthy food!"
    ]

    NORMAL_GOOD_NIGHT = [
        "????????????, {}! Have a nice dream and rest tonight <3",
        "Oyasumi, {}~ Today was fun and thanks for keep talking with me, nyaa~",
        "Good night, {}. I hope you will have a nice sleep tonight zzz...",
        "Have a nice sleep, {} <3",
        "Tomorrow will be absolutely better. It's time to sleep, {} :D",
        "Good night to you, {}",
        "Oyaa~ Let's have a nice sleep, {}",
        "Gute Nacht, have a proper rest, {}!",
        "Good night! Don't forget to have enough sleep time, {} ^^"
    ]

    SPECIAL_GOOD_MORNING = [
        "Kyaaaah! Maid-chan overslept today, ????????? ?????????! Good morning, {}~",
        "Uh? What time is it now, {}? Pyaaahh! Maid-chan is late!"
    ]

    SPECIAL_GOOD_NIGHT = [
        "Ah no, it's already this late! Good night, {} <3",
        "The game was so much fun! Are you sleeping already, {}? Good nite~"
    ]

    EVENT_GOOD_MORNING = [
        {
            "text": "Good morning, {}! It's almost time for Halloween!",
            "start_date": 1,
            "start_month": 10,
            "end_date": 30,
            "end_month": 10,
            "force": False
        },
        {
            "text": "????????????! Happy Halloween, {}! Trick or Treat <3",
            "start_date": 31,
            "start_month": 10,
            "end_date": 31,
            "end_month": 10,
            "force": True
        },
        {
            "text": "Ohaa~ Christmas is coming, {}!",
            "start_date": 1,
            "start_month": 12,
            "end_date": 24,
            "end_month": 12,
            "force": False
        },
        {
            "text": "Merry Christmas, {}! Santa came to my house last night, nyaa~",
            "start_date": 25,
            "start_month": 12,
            "end_date": 25,
            "end_month": 12,
            "force": True
        },
        {
            "text": "Good morning, {}! New year is coming soon <3",
            "start_date": 31,
            "start_month": 12,
            "end_date": 31,
            "end_month": 12,
            "force": True
        },
        {
            "text": "??????????????????????????????! ?????????????????????, {}!",
            "start_date": 1,
            "start_month": 1,
            "end_date": 1,
            "end_month": 1,
            "force": True
        },
        {
            "text": "Good morning, {}! Today is my birthday! Thanks for accompanying Maid-chan this whole year!",
            "start_date": 10,
            "start_month": 1,
            "end_date": 10,
            "end_month": 1,
            "force": True
        }
    ]

    # Base default time, before adding random delta
    DEFAULT_MORNING_TIME = "09:00"  # UTC+9
    DEFAULT_JAPANESE_TIME = "13:00"  # UTC+9
    DEFAULT_NIGHT_TIME = "23:00"  # UTC+9

    # RSS Feed default preset
    DEFAULT_RSS_PRESET = {
        "1": {
            "title": "Manga",
            "url": "https://www.mangaupdates.com/rss.php"
        },
        "2": {
            "title": "Nyaa",
            "url": "https://www.nyaa.si/?page=rss"
        }
    }

    # Supported Languages
    TRANSLATION_LANGUAGE = {
        "id": ["id", "indo", "indonesia", "bahasa", "indonesian", "?????????????????????"],
        "ja": ["ja", "jp", "japanese", "japan", "jepang", "?????????", "nihongo"],
        "en": ["en", "english", "inggris", "??????", "eigo"]
    }
    TRANSLATION_DETECT = {
        "Bahasa": "id",
        "Japanese": "ja",
        "English": "en"
    }
    TRANSLATION_MAP = { # Source : Target
        "en": "ja",
        "ja": "en",
        "id": "ja",
        "": "en"  # Default
    }
    TRANSLATION_KEYWORD = ["translate", "terjemahkan"]
    TRANSLATION_FROM = ["from", "dari"]
    TRANSLATION_TO = ["to", "ke"]
