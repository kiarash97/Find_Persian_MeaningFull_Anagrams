# -*- coding: utf-8 -*-
import pandas_access as mdb
import pandas as pd
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


def search (element , db ):
    # db = set(db)
    if element in db :
        return True
    else:
        return False
    #   *** very slow on long elements ***
    # element = element.encode("utf-8")
    # for i in db :
    #     try:
    #         if element == i.encode("utf-8") :
    #             return True
    #     except:
    #         print (i,db.index(i))
    # return False


print ("Loading First DataSet ")
df1 = pd.read_excel('PersianWords.xlsx', sheet_name='Sheet1')
persian_words = set(df1['*Total farsi Word (Moin+openoffice.fa+wikipedia)'])
print ("Finish Loading Fisrt DataSet")
#Load First DataSet to Memory

print ("Loading Second DataSet")
df2 = mdb.read_table("FLEXICON.mdb", "Entries")
affixes = mdb.read_table("FLEXICON.mdb", "Affixes")
# words = list(df2["WrittenForm"])
flexicon_words = set(df2["WrittenForm"])
#Load Second DataSet to Memory
print ("Finish Loading Second DataSet")

search_word = u'کیارش'
answer_list=set()
gen = all_perms(search_word)
print ("start executing ...")

while 1:
    try:
        next_perm = next(gen)
        if search(next_perm, flexicon_words) or search(next_perm, persian_words):
            answer_list.add(next_perm)
    except StopIteration:
        break;
print (answer_list)
print ("finish executing ...")