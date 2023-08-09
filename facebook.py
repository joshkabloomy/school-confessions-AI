import requests

#Your Access Keys
messageList = []
with open('/Users/joshuadiao/Brucker Final Project/gpt2_gentext.txt') as f:
    messageList = f.readlines()
    
with open('/Users/joshuadiao/Brucker Final Project/count.txt') as count_f:
    count_lines = count_f.readline()

count = int(count_lines)

page_id_1 = 110694251655224
facebook_access_token_1 = 'EAAN9acW6M3oBAMMYWcE9EPqEf77sQlRJP0oublmJcscOd9f7ta3nVZCbWABtJ88ZAndM3MtA6e8FQrjXMqLZCImOGzoTNrVDkOfRFZBENMAMa5ZBPzkLGZAQhNwTexd5CfcjQ1GRyECXEahe1lgKWQF3RW7hZCKZCOuCRD79Dky1lJGsJlxHi4a5'

msg= ""

i =0
while i< len(messageList):
    if(messageList[i] == "====================\n") :
        i+=1
        continue

    msg = "#" + str(count) + ": " +  "\""  + messageList[i]; 
    
    while (i+1 < len(messageList) and messageList[i+1] != "====================\n" and messageList[i+1] != "===================="):
        msg += messageList[i+1]; 
        i+=1
        
    msg+= "\""
    i+=1
    post_url = 'https://graph.facebook.com/{}/feed'.format(page_id_1)
    payload = {
        'message': msg,
        'access_token': facebook_access_token_1
    }
    r = requests.post(post_url, data=payload)
    print(r.text)
    count+=1
    

count_write = open("/Users/joshuadiao/Brucker Final Project/count.txt", "w")
count_write.write(str(count))
count_write.close()