def read_scores(fil):
    '''Takes a text file and outputs a dictionary that maps the letters to the scores
    specified in file'''

    data = open(fil, 'rU')
    scores = {}
    for line in data:
        dummy = line.strip().split(',')
        scores[dummy[0]] = int(dummy[1])
    return scores


def bizarro_world(fil):

    data = open(fil)
    letters = {}
    for line in data:
        dummy = line.strip().split(',')
        try:
            letters[dummy[1]]
        except KeyError:
            letters[dummy[1]] = dummy[0]
        else:
            letters[dummy[1]] += dummy[0]
    return letters

def get_score(scores, word):

    ans = 0
    for c in word:
        ans += scores[c]
    return ans

def read_config(fil):

    data = open(fil)
    ans = {}
    for line in data:
        lin = line.strip()

        if lin.startswith('['):
            dummy1 = {} #when encounter new [] start new dictionary
            ans[lin[1:-1]] = dummy1
        else:
            body = lin.partition('=')
            dummy1[body[0]] = body[2] #fill dictionary with all values under []
    
    return ans

def get_value(config, string1):

    request = string1.partition('.')
    return config[request[0]][request[2]]
                  
if __name__ == '__main__': 
    scores = read_scores('scrabble_scores.txt')
    bizarro_world('scrabble_scores.txt')
    get_score(scores, 'quack')
    config = read_config('config.txt')
    get_value(config, 'user.mobile')
