def get_closed_class_words():
    """
    List of closed class words (i.e. Function Words -- FW) for each corpus.
    They have been extracted automatically, based on the mearning parts of each corpus. In a few cases, some adjustment were made.
    """
    if LANGUAGE == "English":
        # return ['a', 'is', 'which', 'with', 'after', 'and', 'before', 'it', 'the', 'then', 'you']
        return ['a' , 'and' , 'at' , 'is' , 'it' , 'of' , 'some' , 'that' , 'the' , 'which' , 'with'] # 'for', 'on',  'to' are considered as semantic words (SW)
    if LANGUAGE == "German":
        return ['das', 'dem', 'den', 'die', 'ein', 'einen', 'es', 'etwas', 'ihn', 'ist', 'mit', 'um', 'und', 'zu', 'zur', ','] #'für', #im
    if LANGUAGE == "Spanish":
        return ['la', 'el', 'las', 'la', '-lo', 'y', 'ella', 'una', 'un', 'con', 'que', 'está', 'a', 'al', 'de']
    if LANGUAGE == "French":
        return ['à', 'au', 'avec', "d'", 'de', 'des', 'du', 'en', 'est', 'et', 'la', 'le', 'les', 'qui', 'un', 'une'] # 'dans', 'sur', are considered as semantic words (SW)
    if LANGUAGE == "Italian":
        return ['a', 'alle', 'le', 'e', '-ci', 'alla', 'la', 'i', "d'", '-lo', 'al', 'che', 'una', 'si', 'un', 'del', 'il', 'in', 'é', 'con']
    if LANGUAGE == "Catalan":
        return ["-ho", "a", "al", "amb", "d’", "de", "el", "està", "i", "la", "les", "l’", "mica", "que", "un", "una"]
    if LANGUAGE == "Marathi":
        return ['-at', '-atla', '-cha', '-chi', '-na', '-wr', 'ahe', 'ani', 'astil', 'chi', 'davya', 'he', 'jo', 'ka', 'to']
    if LANGUAGE == "Hindi":
        return ['aek', 'aur', 'hain', 'ka', 'ke', 'ko', 'may', 'paas', 'par', 'taraf', 'thoda', 'us', 'wala']
    if LANGUAGE == "Persian":
        return ['ra', 'kon', 'bede', 'be-', '-e', 'an', 'bo-' ,'va', 'bi-', 'ba', '-yi', 'ke',  'ast', 'donbal', 'bashad', 'saat', 'dakhel']
    if LANGUAGE == "Basque":
        return ['-a', '-ak', '-an', '-ara', '-aren', '-ekin', '-en', '-etan', '-ko', '-ra', '-rean', 'bat', 'den', 'eta']
    if LANGUAGE == "Portuguese":
        return ["-o", "a", "as", "ao", "com", "da", "de", "e", "em", "estará", "está", "o", "pelo", "que", "um", "uma", "às"]
    if LANGUAGE == "Mandarin_simpl":
        return ['-个','-张','-支','-杯','-棵','-盏','-通','-道','-间','一个','一份','再','同时','它','把','放在','有','点','的','那']
    if LANGUAGE == "Malay":
        return [  '-kan' , '-nya' , 'arah' , 'berada' , 'berwarna' , 'dan' , 'di' , 'itu' , 'nya' , 'pada' , 'pukul' , 'satu' , 'sebuah' , 'sedikit' , 'yang','panggilan' ] # 'untuk' is both ccw and ocw
    if LANGUAGE == "Mandarin_traditional":
        return['-個' , '-張' , '-支' , '-杯' , '-棵' , '-盞' , '-通' , '-道' , '-間' , '一份' , '一個' , '再'  , '它' , '把' , '有' , '的' ,  '那' , '點'] # '在', '裡', '給' are both ccw and ocw
    if LANGUAGE == "Turkish":
        return [  '-a' , '-de' , '-e' , '-i' , '-ip' , '-ki' , '-li' , '-nin' ,  '-te' , '-u' , '-yi' , '-yip' , 'bir' , 'olacagina' , 'olan'] # '-ta'
    if LANGUAGE == "Bulgarian":
        return [  ',' , '-а' , '-ия' , '-та' , '-то' , 'го' , 'е' , 'и' , 'който' , 'която' , 'нея' , 'някакъв' , 'с'] # ['в' , 'за'] are both CCW and SW
