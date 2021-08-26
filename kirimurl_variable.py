import requests as req
import random
import time

while True:
    print ("KIRIM DATA BERHASIL")
    time.sleep(1)
    data = random.randint(0,222)
    resp = req.request(method='GET', url="http://itlab.unila.ac.id/KMMI/GIGIH_FORDA_NAMA/iot/load.php?jarak=%s" % (data))
