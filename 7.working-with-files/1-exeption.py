acronyms = {
    'LOL' : 'laugh out load', 
    'IDK': "I don't know",  
    'TBH': 'to be honest'
}

try:
    definition = acronyms['BTW']
except:
    print('BTW is not existed')
finally:
    print('List of acronyms')
    for acr in acronyms:
        print('Acronyms:', acr, '- Definition:', acronyms[acr])