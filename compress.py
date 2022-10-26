#Parcial 2 Computación

class Compress():
    def __init__(self):
        self.listText = []
        self.dictText = {}

    def compress(self, text):
        
        textlistwords = text.split(' ')
        num = 1
        
        for word in range(len(textlistwords)):
            listdictkeys = self.dictText.keys()
            if textlistwords[word] not in listdictkeys:
                self.dictText.update({textlistwords[word]:num})
                self.listText.append(num)
                num = num +1
            else:
                self.listText.append(self.dictText[textlistwords[word]])
        
        values = self.dictText
        compressed = self.listText
        return compressed, values
            
    def uncompress(self, compressedText, dictText):

        uncompressText = ''
        valuesOfdict = dictText.values()
        listofvaluesOfdict = []
        keysOfdict = dictText.keys()
        listofkeysOfdict = []
        for i in valuesOfdict:
            listofvaluesOfdict.append(i)
        for i in keysOfdict:
            listofkeysOfdict.append(i)

        for num in compressedText:
            for value_num in listofvaluesOfdict:
                if num == value_num:
                    indexValue = listofvaluesOfdict.index(value_num)    
                    uncompressText = uncompressText + listofkeysOfdict[indexValue] + ' '
        uncompressText = uncompressText[:-1]
        return uncompressText