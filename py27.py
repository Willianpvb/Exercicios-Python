#cidade = input('Digite o nome da sua cidade:').title()
#contem=''
#if(cidade.count('Santo') > 0):
#    contem = 'Sim'
#else:
 #   contem = 'Não'
#print(">{}< possui o nome 'Santo'? {}".format(cidade,contem))

def order(sentence):
    s2 = sentence.split()
    s3 = s2.join()
    for i in range(0,len(s2)):
        for t in range(0,10):
            if(s2[i].find(str(t)) == True ):

                s3.replace(s3[t],s2[i])
    return s3

