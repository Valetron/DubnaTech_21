pH = {
    "картофель" : (4.5, 6.5),
    "кукуруза" : (5.8, 6.8),
    "рожь" : (5.5, 7.5),
    "лён" : (5.9, 6.5),
    "подсолнечник" : (6, 6.8),
    "свекла" : (6, 6.8),
    "капуста" : (6.7, 7.4)
}

# print(pH["картофель"])

SOIL = { 
    "подзолистые" : {"картофель" : False,
    "кукуруза" : True,
    "рожь" : True,
    "лён" : True,
    "подсолнечник" : False,
    "свекла" : False,
    "капуста" : True} ,

    "серые лесные" : {"картофель" : False,
    "кукуруза" : True,
    "рожь" : True,
    "лён" : False,
    "подсолнечник" : False,
    "свекла" : False,
    "капуста" : True} ,

    "каштановые" :  {"картофель" : False,
    "кукуруза" : True,
    "рожь" : True,
    "лён" : True,
    "подсолнечник" : False,
    "свекла" : False,
    "капуста" : True} ,
     "" : {} ,
     "" : {} ,
     "" : {} ,
     "" : {} 
}

# print(SOIL["каштановые"]["картофель"])

PRED = {
    "картофель" : ["рожь", "свекла", "капуста"],
    "кукуруза" : ["картофель", "лён", "подсолнечник", "капуста"],
    "рожь" : [],
    "" : [],
    "" : [],
    "" : [],
    "" : []
}

# print(PRED["картофель"][0])

if __name__ == "__main__":
    main()