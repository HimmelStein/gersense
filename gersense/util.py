
from pygermanet import load_germanet
from gersense.resource import word2vecDicLoc, VOC_Loc, FILE_Loc


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
        w2vFile = word2vecDicLoc["de"]["kyubyong"]["w2v"]
    if vocFile=="":
        vocFile = VOC_Loc["de"]["kyubyong"]["voc"]
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


def create_word2wordsense_dic(vocFile="", wwsFile="", vocWsFile=""):
    """
    sample call: create_word2wordsense_dic()
    :param vocFile:
    :param wwsFile:
    :param vocWsFile:
    :return:
    """
    if vocFile=="":
        vocFile = FILE_Loc["de"]["kyubyong"]["voc"]
    if wwsFile=="":
        wwsFile = FILE_Loc["de"]["kyubyong"]["w2ws"]
    if vocWsFile == "":
        vocWsFile = FILE_Loc["de"]["kyubyong"]["wsVoc"]
    wwlst = []
    wslst = []
    gn = load_germanet()
    with open(vocFile, 'r') as ifh:
        for ln in ifh:
            word = ln[:-1]
            lst = [get_name_of_synset(ele) for ele in gn.synsets(word)]
            if lst:
                wwlst.append(word+" "+" ".join(lst))
            wslst += lst
    wslst = list(set(wslst))
    wslst.sort()
    print(wwlst[:10])
    print(wslst[:10])
    with open(wwsFile, 'w') as ofh:
        ofh.write("\n".join(wwlst))
    with open(vocWsFile, 'w') as ofh:
        ofh.write("\n".join(wslst))


def create_wordsense_struc_dic(vocWsFile="", childrenFile="", parentFile="", pathFile=""):
    if vocWsFile=="":
        vocWsFile = FILE_Loc["de"]["kyubyong"]["wsVoc"]
    if childrenFile=="":
        childrenFile = FILE_Loc["de"]["kyubyong"]["wsChildren"]
    if parentFile == "":
        parentFile = FILE_Loc["de"]["kyubyong"]["wsParent"]
    if pathFile == "":
        pathFile = FILE_Loc["de"]["kyubyong"]["wsPaths"]
    chidrenLst = []
    parentLst = []
    pathLst = []
    gn = load_germanet()
    with open(vocWsFile, 'r') as ifh:
        for ln in ifh:
            ws = ln[:-1]
            ins = gn.synset(ws)
            if ins.__class__.__name__ != 'Synset':
                print(ins)
                continue
            chidren =  [get_name_of_synset(ele) for ele in ins.hyponyms]
            chidrenLst.append(ws+" "+" ".join(chidren))

            parent = [get_name_of_synset(ele) for ele in ins.hypernyms]
            parentLst.append(ws+" "+" ".join(parent))

            plst = []
            for apath in ins.hypernym_paths:
                pathStr = " ".join([get_name_of_synset(ele) for ele in apath])
                plst.append(pathStr)
            pathLst.append(":".join(plst))

    with open(childrenFile, 'w') as ofh:
        ofh.write("\n".join(chidrenLst))
    with open(parentFile, 'w') as ofh:
        ofh.write("\n".join(parentLst))
    with open(pathFile, 'w') as ofh:
        ofh.write("\n".join(pathLst))


if __name__=="__main__":
    create_wordsense_struc_dic()