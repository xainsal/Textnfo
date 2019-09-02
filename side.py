import string


class TextTools():
    def __init__(self, text):
        self.text = text
        self.mainDic = self.character_counter()

    def __len__(self):
        self.length = len(self.text)
        print('Total Characters:', self.length)
        print('-' * 35)

    def character_counter(self):
        words_info = [[string.digits], [string.ascii_lowercase], [string.ascii_uppercase], [string.punctuation]]
        text_length = len(self.text)
        small_amount = 0
        run = 0
        main_dictionary = {}
        alphabet_info = [{}, {}, {}, {}]
        #This for loop will loop lists from words_info List
        for lists in words_info:
            for words in lists:
                for single_char in words:
                    for y in range(0, text_length):
                        if self.text[y] == single_char:
                            small_amount += 1
                    if small_amount > 0:
                        alphabet_info[run][single_char] = small_amount
                    small_amount = 0
                run += 1
        main_dictionary['Digits'] = alphabet_info[0]
        main_dictionary['Small-Alphabets'] = alphabet_info[1]
        main_dictionary['Capital-Alphabets'] = alphabet_info[2]
        main_dictionary['Punctuation'] = alphabet_info[3]
        return main_dictionary

    def words_counter(self):
        max = 0
        min = 0
        word_list = self.text.split(' ')
        word_count = len(word_list)
        for word in word_count:
            if max < len(word):
                max = len(word)
        print(max)
        print('=' * 35)
        print('Total Words: ', word_count)
        print('=' * 35)

    def print_info(self):
        for kdic, vdic in self.mainDic.items():
            print(kdic,':')
            for keys, val in vdic.items():
                print('\t', keys, ' : ', val)
            print('\n')

    def total_count(self):
        total = 0
        self.words_counter()
        self.__len__()
        for kdic, vdic in self.mainDic.items():
            print('\tTotal', kdic,': ', end='')
            for val in vdic.values():
                total += val
            print(total)
            total = 0


