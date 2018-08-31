
from pygermanet import load_germanet
from gersense.resource import word2vecDicLoc, VOC_Loc, WORDSENSE_Loc


def get_name_of_synset(synset):
    return synset.__str__()[7:-1]

def create_w2v_voc(w2vFile="", vocFile=""):
    """
    sample call: create_w2v_voc(vocFile="/home/kdml21/dongt/data/word2vec/de/VOC_DE.tsv")
    :param w2vFile:
    :param vocFile:
    :return:
    """
    if w2vFile=="":
        w2vFile = word2vecDicLoc["de"][0]["local"]
    if vocFile=="":
        vocFile = VOC_Loc["de"][0]["local"]
    wlst = []
    with open(w2vFile, 'r') as ifh:
        for ln in ifh:
            # second string in ln is a word
            wlst.append(ln.split()[1])
    wlst = [ele for ele in wlst if '.' not in ele]
    wlst.sort()
    print("number of voc:", len(wlst))
    print(wlst[:10])
    with open(vocFile, 'w') as ofh:
        ofh.write("\n".join(wlst))


def create_word2wordsense_dic(vocFile="", wwsFile=""):
    """
    sample call: create_word2wordsense_dic()
    :param vocFile:
    :param wwsFile:
    :return:
    """
    if vocFile=="":
        vocFile = VOC_Loc["de"][0]["local"]
    if wwsFile=="":
        wwsFile = WORDSENSE_Loc["de"][0]["local"]
    wwlst = []
    gn = load_germanet()
    with open(vocFile, 'r') as ifh:
        for ln in ifh:
            word = ln[:-1]
            wslst = [get_name_of_synset(ele) for ele in gn.synsets(word)]
            if wslst:
                wwlst.append(word+" "+" ".join(wslst))

    print(wwlst[:10])
    with open(wwsFile, 'w') as ofh:
        ofh.write("\n".join(wwlst))


if __name__=="__main__":
    pass