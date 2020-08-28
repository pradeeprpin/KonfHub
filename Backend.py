import requests as r

url = "https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences"

#print(url)

resp=r.get(url)
#print(resp.status_code)
jso=resp.json()
# print(jso)

'''for key,values in jso.items():
    #print(str(type(key)),str(type(values)))
    if str(type(values)) == "<class 'list'>":
        print(values)'''

#print(jso['paid'])

conf_lis_paid=[]
paid=jso['paid']
for i in paid:
    record=record=[i['confName'],
            i['confStartDate'],
            None if i['city']=="" else i['city'],
            None if i['state']=="" else i['state'],
            None if i['country']=="" else i['country'],
            i['entryType'],
            i['confUrl']]
    conf_lis_paid.append(record)
'''j=1
for i in conf_lis_paid:
    print(j,end=". ")
    print(*i,sep=',')
    j+=1
'''
exact_duplicates_paid=[]
for i in conf_lis_paid:
    if i not in exact_duplicates_paid:
        exact_duplicates_paid.append(i)
    else:
        rec=i

'''j=1
for i in exact_duplicates_paid:
    print(j,end=". ")
    print(*i,sep=",")
    j+=1'''

'''for i in exact_duplicates_paid:
    if i == rec:
        print(*i,end=",")'''

sem_url_paid=[]
for i in exact_duplicates_paid:
    if i[:-1] not in sem_url_paid:
        sem_url_paid.append(i[:-1])

'''j=1
for i in sem_url_paid:
    print(j,i)
    j+=1
len(sem_url_paid)'''

print("\n\nPrinting Symantic duplicates Paid\n\n")

semantic_duplicates_paid=[]
j=1
for i in exact_duplicates_paid:
    if i[:-1] in sem_url_paid:
        semantic_duplicates_paid.append(i)
        sem_url_paid.remove(i[:-1])
    else:
        srec=i
for i in semantic_duplicates_paid:
    print(j,i)
    j+=1
print("\n\nDuplicates values in paid\n\n")
for i in conf_lis_paid:
    if i[0] == rec[0] or i[0] == srec[0]:
        print(i)

conf_lis_free=[]
free=jso['free']
for i in free:
    record=[i['confName'],
            i['confStartDate'],
            str(None) if i['city']=="" else i['city'],
            str(None) if i['state']=="" else i['state'],
            str(None) if i['country']=="" else i['country'],
            i['entryType'],
            i['confUrl']]
    conf_lis_free.append(record)

'''j=1
for i in conf_lis_free:
    print(j,end=". ")
    print(i,sep=",")
    j+=1'''

exact_duplicates_free=[]
rec_free=[]
for i in conf_lis_free:
    if i not in exact_duplicates_free:
        exact_duplicates_free.append(i)
    else:
        rec_free=i

'''j=1
for i in exact_duplicates_free:
    print(j,end=". ")
    print(*i,sep=',')
    j+=1
'''

'''for i in exact_duplicates_free:
    if i == rec_free:
        print(*i,sep=",")
else:
    print([])
'''

sem_url_free=[]
for i in exact_duplicates_free:
    if i[:-1] not in sem_url_free:
        sem_url_free.append(i[:-1])


'''j=1
for i in sem_url_free:
    print(j,i)
    j+=1
len(sem_url_free)'''

print("\n\nPrinting Symantic duplicates Free\n\n")
semantic_duplicates_free=[]
srec_free=[]
j=1
for i in exact_duplicates_free:
    if i[:-1] in sem_url_free:
        semantic_duplicates_free.append(i)
        sem_url_free.remove(i[:-1])
    else:
        srec_free=i
for i in semantic_duplicates_free:
    print(j,i)
    j+=1