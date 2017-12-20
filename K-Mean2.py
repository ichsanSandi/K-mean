#digunakan untuk matriks
import numpy as np
#digunakan untuk membuat grafik
import matplotlib.pyplot as plt
#import cvs
import csv

#fungsi mengeload data set
def load_data(nama):
    with open(nama, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
    #mengubah ke dalam array
    #mengeleminasi class
    full =np.asarray(np.delete(dataset,[2,3,4],1),float)
    return full

#mengambil class
def kelasnya(nama):
    with open(nama, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
    classnya = np.asarray(np.delete(dataset,[0,1,2,3],1))
    return classnya

#fungsi Untuk menghitung jarak
def jarak(a,b):
    return np.linalg.norm(a-b)

#fungsi untuk menggambar grafik
def plot(dataset, history_centroids, belongs_to):
    #memlih warna
    colors = ['g','r','y','k']

    fig, ax = plt.subplots()

    #digambar berdasarkan cluster
    for index in range(dataset.shape[0]):
        instances_close = [i for i in range(len(belongs_to)) if belongs_to[i] == index]
        for instance_index in instances_close:
            ax.plot(dataset[instance_index][0], dataset[instance_index][1], (colors[index] + 'o'))

    #menggambar titik centroid
    history_points = []
    for index, centroids in enumerate(history_centroids):
        for inner, item in enumerate(centroids):
            if index == 0:
                history_points.append(ax.plot(item[0], item[1], 'bo')[0])
            else:
                history_points[inner].set_data(item[0], item[1])
                print("centroids {} {}".format(index, item))

                plt.pause(0.8)

def kmean():
    #epsilon adalah gagal
    epsion=0
    #membuat catatan centroid
    catatan_centroid = []
    #meload data
    databaru=load_data('iris.txt')
    # memisahkan jumalh record dan field
    jumlah_record,jumlah_field = databaru.shape
    #inisisasi centroid
    centroid_terpilih = []
    #memilih centroid
    jumlah_centroid = input("Masukan Jumlah Centroid\n")
    pilihan = input("1.Random\n2.Pilih Sendiri\n")
    if pilihan==1:
        proto = databaru[np.random.randint(0, jumlah_record - 1, size=jumlah_centroid)]
    else:
        for x in range(jumlah_centroid):
            pilih = input("Centroid yang "+repr(x+1)+"\n")
            centroid_terpilih.append(pilih)
            # print centroid_terpilih
        #mengambil centroid terpilih
        proto = databaru[[centroid_terpilih]]

    print proto
    #memasukan dalam catatan centroid
    catatan_centroid.append(proto)
    #membuat dummy pengurangan
    proto_lama = np.zeros(proto.shape)
    #membuat cluster dammy
    cluster = np.zeros((jumlah_record, 1))
    #menghitung jarak pertama
    jaraknya = jarak(proto,proto_lama)
    iterasi =0
    while jaraknya>epsion:
        iterasi+=1
        #menghitung jarak
        jaraknya = jarak(proto,proto_lama)
        proto_lama =proto
        for index_content, content in enumerate(databaru):
            #inisiasi matrik jarak
            jaraksetiap=np.zeros((jumlah_centroid,1))
            for index_proto, content_proto in enumerate(proto):
                #mengisi jarak
                jaraksetiap[index_proto] = jarak(content_proto,content)

            #memilih jarak yang paling kecil
            cluster[index_content]=np.argmin(jaraksetiap)

        #ini siasi tempat penyimpanan
        tmp_proto = np.zeros((jumlah_centroid,jumlah_field))

        for index in range(len(proto)):
            #memilihkan cluster
            instances_close = [i for i in range(len(cluster)) if cluster[i] == index]
            #mencari rata2
            proto = np.mean(databaru[instances_close], axis=0)
            # prototype = dataset[np.random.randint(0, num_instances, size=1)[0]]
            tmp_proto[index, :] = proto
        #mengeset jarak yang baru
        # print proto
        proto = tmp_proto
        #menyimpan di cetatan
        catatan_centroid.append(tmp_proto)

    return databaru,catatan_centroid,cluster,jumlah_centroid,jumlah_record


# prototypes = databaru[[0,0]]
# proorld = np.zeros(prototypes.shape)
# jaka=jarak('encludian',prototypes,proorld)
datame, catatan_centroid,cluster ,jumlah_centroid,jumlah_record=kmean()
plot(datame, catatan_centroid, cluster)
clasnya = kelasnya('iris.txt')

hitung=np.append(cluster,clasnya,axis=1)

# print jumlah_centroid
setosa=0
versi =0
virgi =0
# hh=(hitung[1]==[0.0 , 'Iris-setosa'])
# print hh
#
for y in range(jumlah_centroid):
    setosa = 0
    versi = 0
    virgi = 0
    for x in range(jumlah_record):
          if (hitung[x]==[float(y) ,'Iris-setosa']).all():

              setosa+=1
              # print hitung[x]
          elif (hitung[x]==[float(y) ,'Iris-versicolor']).all():
              versi+=1
              # print hitung[x]
          elif (hitung[x]==[float(y) ,'Iris-virginica']).all():
              virgi+=1
              # print hitung[x]
    print "untuk Cluseter" + repr(y+1)+"\n"
    hasil_setosa = (float(setosa)/jumlah_record)
    print "Iris-setosa =" + repr(setosa)
    print "Persentasenya " + repr(setosa)+"/"+repr(jumlah_record)+"="+repr(hasil_setosa*100)+"%\n"
    hasil_versi = (float(versi) / jumlah_record)
    print "Iris-versicolor =" + repr(versi)
    print "Persentasenya " + repr(versi) + "/" + repr(jumlah_record) + "=" + repr(hasil_versi*100)+"%\n"
    hasil_virgi = (float(virgi) / jumlah_record)
    print "Iris-virginica =" + repr(virgi)
    print "Persentasenya " + repr(virgi) + "/" + repr(jumlah_record) + "=" + repr(hasil_virgi*100)+"%\n"

# print catatan_centroid
#print setosa
#print hitung