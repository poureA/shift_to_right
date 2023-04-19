try :
    def shift_right(text)->str :
        '''this function shifts the first letter of each word to the next word in the sentence'''
        text_list = text.split()
        if len(text_list) >= 0 :
            temp = str()
            temp += text_list[-1][0]
            temp += text_list[0][1:]
            temp += ' '
            idx = 1
            for i in range(len(text_list)) :
                if i == len(text_list) - 1 :
                    if len(text_list) == 2 :
                        temp += text_list[0][0]
                        temp += text_list[1][1:]
                        break
                    else :
                        break
                temp += text_list[i][0]
                temp += text_list[idx][1:]
                temp += ' '
                idx += 1
            return temp[:-1]
        else :
            return 'at least 1 words needed'
    try :
        print(shift_right(input('enter a text here :')))
    except :
        raise
except :
    print('something wrong with function')
exit = input('enter any key to exit :')
