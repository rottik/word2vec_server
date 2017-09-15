def get_w2v_similarity(word1,word2,ip="147.230.21.32",port="8888"):
    import requests
    import json 
    try:
        r=requests.post("http://"+ip+":"+port+"/word2vecdiff", data={'word1':word1, "word2":word2})
    except TimeoutError:
        print("Word2Vec server "+ip+":"+port+" error.")
        return 0.0
    if(r.status_code!=200):
        print("Word2Vec server "+ip+":"+port+" error.")
        return 0.0        
        j=json.loads(r.text)
    return float(j['word2vec_sim'])
def get_w2v_vector(word,ip="147.230.21.32",port="8888"):
    import requests
    import json 
    try:
        r=requests.post("http://"+ip+":"+port+"/word2vec", data={'word':word})
    except TimeoutError:
        print("Word2Vec server "+ip+":"+port+" error.")
        return 0.0
    if(r.status_code!=200):
        print("Word2Vec server "+ip+":"+port+" error.")
        return 0.0
    j=json.loads(r.text)
    return j['vector']

if(__name__=="__main__"):
    print(get_w2v_similarity("king","queen",ip="147.230.21.32"))
    print(get_w2v_vector("king",ip="147.230.21.32"))
