
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("files/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("files/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(str):
    for char in punctuation_chars:
        if char in str:
            str = str.replace(char, "")
    return str            

def get_pos(str):
    lines = strip_punctuation(str)
    words = lines.lower().split()
    count = 0
    for word in words:
        if word in positive_words:
            count = count + 1
    return count

def get_neg(str):
    lines = strip_punctuation(str)
    words = lines.lower().split()
    count = 0
    for word in words:
        if word in negative_words:
            count = count + 1
    return count   

fh = open("files/project_twitter_data.csv", 'r')
lines = fh.readlines()
new_file = open("files/resulting_data.csv", 'w')
new_file.write("""Number_of_Retweets ,Number_of_Replies, Positive_Score, Negative_Score, Net_Score""")
new_file.write("\n")

for line in lines[1:]:
    content = line.strip().split(",")
    a = get_pos(content[0])
    b = get_neg(content[0])
    #row_string = ",".join([content[1], content[2], str(a), str(b), str(a-b)])
    row_string = '{},{},{},{},{}'.format(content[1], content[2], str(a), str(b), str(a-b))
    new_file.write(row_string)
    new_file.write("\n")

new_file.close()
fh.close()
