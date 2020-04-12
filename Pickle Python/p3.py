#python_version == '3.7.4'
import pickle
def load_data(file):
    try:
        f = open(file,"rb")
        result = pickle.load(f)
        f.close()
    except:
        pass
    return result

def query_following(user_name):
    result = load_data("followers.pydata")
    Final =[]
    for i in result:
        for j in result[i]:
            if user_name in j:
                Final.append(i)
                break
    return(Final)

def update():
    x = load_data("followers.pydata")
    del x["Lorna Carrico"]
    x["Anne Smelcer"] = ["Christine Phillips","Charles Mason","Tim Lathrop"]
    f = open("followers-updated.pydata", "wb")
    pickle.dump(x,f)
    f.close()

def get_num_of_followers():
    x = load_data("followers-updated.pydata")
    for key in x:
        x[key] = len(x[key])
    return(x)