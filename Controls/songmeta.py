import meta

def music(m_link):
    id3r = meta.Reader(m_link)
    listi = []
    #songname, artist, genre, album
    listi.append(m_link.split('/')[-1])
    listi.append(id3r.getValue('performer'))
    listi.append(id3r.getValue('genre'))
    listi.append(id3r.getValue('album'))

    #print listi
    return listi

if __name__=="__main__":
    music("C:/Users/Harshit Soni/Desktop/python/forProject/Down.mp3")