text = "I am an International student from Jfdsfkjsdjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjhfsdj is country and I am very pleased to meet you here dfsfdfsdsda ewrqer"

n = 20

def prettyprint(text, n):

    textList = text.split()
    count = 0
    results = [] 
    line = ''

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
        print('[' + line + ((n - len(line)) * ' ') + ']')
    
    return results

prettyprint(text, n)
