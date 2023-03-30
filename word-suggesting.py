from csv_to_dict import CsvConverter 
import time 

converter = CsvConverter()

word_dict = converter.convert_to_dict('ngram_freq_dict.csv')

st = time.time()

def word_scheme(my_word, word_dict: dict):
    output_word_dict = {
        # words that match the requirements (they starts with the same letters as my_word) 
    }
    got_response = False
    for word in word_dict.keys():
        try:
            if my_word == word[:len(my_word)]:
                distance = len(word) - len(my_word)
                if distance == 0:
                    continue
                elif distance == 1:  
                    output_word_dict[word] = word_dict[word]
                    got_response = True
                    return word
                else:
                    try:
                        if int(word_dict[word]) > max(int(output_word_dict.values())):
                            output_word_dict.update({word : word_dict[word]})
                    except:
                        output_word_dict.update({word : word_dict[word]})
        except: 
            continue
             
    max_value = 0
    if not got_response:
        for key in output_word_dict:
            output_word_dict[key] = int(output_word_dict[key])  
            if output_word_dict[key] > max_value:
                max_value = output_word_dict[key]
                most_used_word = key 
    return most_used_word

print(word_scheme('unill', word_dict=word_dict))
et = time.time()

elapsed_time = et - st
print(f'Execution time: {elapsed_time}')