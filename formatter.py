def prettyprint(text, n):
    '''
    text: string
    n: integer
    This function formats the string into pretty text on several lines of the same length. 
    Formatting principles: 1) number of characters on each line cannot exceed n
                           2) if the length of a word is less than n, do not split it into different lines
                              otherwise, split it into different lines
    '''
    
    textList = text.split()
    results = []   # final results of the text display
    line = ''      # characters shown on each line
    count = 0      # number of characters on each line

    for word in textList:
        if line == '':
            count += len(word)
        else:
            count += len(word) + 1
        
        if count <= n:
            if line == '':
                line += word
            else:
                line += ' ' + word            
        else:
           results.append(line)
           while len(word) > n:
               line = word[:n]
               results.append(line)
               word = word[n:]
          
           line = word
           count = len(word)
               
    for line in results:
        print('[' + line + (n - len(line)) * ' ' + ']')
    
    return results

text = "I am an International student from Jfdsfkjsdjjjjjjjjjjjjjjjjj" \
       "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj" \
       "jjjjjjjjjhfsdj is country and I am very pleased to meet you"   \
       "here dfsfdfsdsda ewrqer" 
n = 20

prettyprint(text, n)
