from hashlib    import sha256
import time


class block:
    def __init__(self,timeStamp,data,previousHash=''):
        self.timeStamp = timeStamp
        self.data = data
        self.previousHash = previousHash
        self.kuvvet = 0
        self.hash = self.hesapla()

    def hesapla(self):
        while True:
            self.kuvvet =self.kuvvet+1
            ozet = sha256((str(self.timeStamp)+str(self.data)+str(self.previousHash)+str(self.kuvvet)).encode()).hexdigest()
            if ozet[0:2] == "00":
                break
        return ozet

class blockChain:
    def __init__(self):
        self.chain=[self.genesisOlustur()]

    def genesisOlustur(self):
        return block(time.ctime(),"EBA","")

    def blockEkle(self,data):
        node = block(time.ctime(),data,self.chain[-1].hash)
        self.chain.append(node)

    def kontrol(self):
        for i in range(len(self.chain)):
            if i!=0:
                ilk = self.chain[i-1].hash
                suan = self.chain[i].previousHash
                if ilk!=suan:
                    return "Zincir Kopmuş"
                if sha256((str(self.chain[i].timeStamp)+str(self.chain[i].data)+str(self.chain[i].previousHash)+str(self.chain[i].kuvvet)).encode()).hexdigest() != self.chain[i].hash:
                    return "Zincir Kopmuş"      
        return "Sağlam"


    def listeleme (self):
        print("BlockChain = \n")
        for i in range(len(self.chain)):
            print("Block => ",i," \nHash = " ,str(self.chain[i].hash),"\nZaman Damgası =",str(self.chain[i].timeStamp),"\nData =",str(self.chain[i].data), "\nKuvvet =", str(self.chain[i].kuvvet),"\nPreviousHash = ", str(self.chain[i].previousHash))


AsilChain = blockChain()


while True:
    print("Lütfen seçiminizi yapınız \nBlock eklemek için 0 \nBlockchain'i görmek için 1 \nZinciri kontrol etmek için 2 \nÇıkmak için 3 'ü seçiniz") 
    data = input()
    if data == "0":
        print("Gönderilen miktarı giriniz = ")
        miktar = input()
        AsilChain.blockEkle(miktar)
    elif data =="1":
        AsilChain.listeleme()
    elif data =="2":
        print(str(AsilChain.kontrol()))
    elif data =="3":
        break
                        

                     
            

