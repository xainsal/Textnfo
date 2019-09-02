def words_counter(self):
    longest_word ='pneumonoultramicroscopicsilicovolcanoconiosis'
    max = 0
    word_list = text.split(' ')
    word_count = len(word_list)
    for word in word_list:
        if max < len(word):
            max = len(word)
    min = max + 1
    for word in word_list:
        if min > len(word) and min > 2:
            min = len(word)
    print(f'Length of longest Word: {max}')
    print(f'Length of Smallest Word {min}')
    print('=' * 35)
    print('Total Words: ', word_count)
    print('=' * 35)


text = "modify the egg timer we created in Chapter 2 so that the user can enter the number of seconds that the timer must run. This would ()() the user to customize their"
words_counter(text)