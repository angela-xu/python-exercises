"""
This is a simple formatter for text display, which formats text into several lines of the same length.
"""

def prettyprint(text, n):
    
    # text: text that needs to be formatted
    # n: maximun number of characters that can be shown on each line
    
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
