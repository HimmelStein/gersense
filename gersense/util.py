
from gersense.resource import word2vecDicLoc


def create_w2v_voc(w2vFile="", vocFile=""):
    if w2vFile=="":
        w2vFile = word2vecDicLoc["de"][0]["local"]
    wlst = []
    with open(w2vFile, 'r') as ifh:
        for ln in ifh:
            wlst.append(ln.split()[1])
    wlst = [ele for ele in wlst if '.' not in ele]
    wlst.sort()
    print("number of voc:", len(wlst))
    print(wlst[:10])
    with open(vocFile, 'w') as ofh:
        ofh.write("\n".join(wlst))


if __name__=="__main__":
    create_w2v_voc(vocFile="/home/kdml21/dongt/data/word2vec/de/VOC_DE.tsv")