import copy

class open_file :
# init format data awal yang bakal dipake
    def __init__(self):
        self.process = 0    #jumlah proses yang akan dilakukan
        self.instance = 0   #jumlah instance yang dimiliki
        self.available = []     #jumlah resource yang tersedia
        self.allocation = []    #jumlah alokasi data dari tiap proses
        self.max = []   #jumlah max data dari tiap proses
        self.need = []  #total resource yang diperlukan untuk tiap proses, diperoleh dari max - allocation
        self.avaforwork = []    #jumlah resource yang tersedia setelah dikurangi allocation

# Fungsi untuk Baca File dlm format, fungsi berhenti kalo file ga ketemu 
    def read_file(self, filename):
        # cek ada filenya enggak
        try:                
            f = open(filename, "r")         ##opsional bs dijadiin input
            return f.readlines()     ##kalo ketemu di return
        # in case file ga ketemu
        except:                           
            print(f"File '{filename}' tidak ditemukan!")
            return False        # return False
        
# Fungsi untuk ngubah string ke integer     
    def str_to_int (self, data, address):   
        temp = []       # temporary list untuk nyimpen data yang udah diubah
        for string in data:     #ngeluarin tiap string dalem data
            temp.append(int(string))    #ubah data & append ke temporary list
        address.append(temp)    #temporary list di append ke address, address di isi pake data baru

# Fungsi untuk mecah belahin data, untuk masukin data ke variabel masing2
    def filter(self, all_lines):        
        deadlock = 0        #untuk hitung berapa kali deadlock terjadi dan menjadi syarat untuk bisa atau tidaknya data dikerjakan
        self.process = int(all_lines[0])        #isi self.process, selalu pada baris ke 0
        self.instance = int(all_lines[1])       #isi self.instance, selalu pada baris ke 1
        
        #isi available, selalu pada baris ke 2
        available = all_lines[2].replace('\n','').split(',')     #penyimpanan sementara available dalam bentuk string, split untuk menghilangkan koma(,) dan replace untuk menghilangkan newline(\n)
        self.str_to_int(available, self.available)       #pengubahan available ke integer, isi self.available
        
        try:
        #isi allocation, selalu ada pada baris ke 3 sampai 3+process (tergantung jumlah proses)
            for proc_all in range (self.process):       #perulangan untuk menarik semua data allocation dan memindahkannya ke self.allocation
                allocation = all_lines[3+proc_all].replace('\n','').split(",")      #penyimpanan sementara allocation dalam bentuk string, split untuk menghilangkan koma(,) dan replace untuk menghilangkan newline(\n), indeks 3+proc_all untuk memastikan data yang ditarik hanya data dari baris ke 3 sampai 3+proc_all
                self.str_to_int(allocation, self.allocation)        #pengubahan allocation ke integer, isi self.allocation

            #isi max, selalu ada pada baris ke 3+process sampai ke 3+process+process    
            for proc_max in range (self.process):   #perulangan untuk menarik semua data max dan memindahkannya ke self.max
                max = all_lines[3+proc_max+self.process].replace('\n','').split(",")    #penyimpanan sementara max dalam bentuk string, split untuk menghilangkan koma(,) dan replace untuk menghilangkan newline(\n), indeks 3+proc_all untuk memastikan data yang ditarik hanya data dari baris ke 3+self.process sampai 3+self.process+proc_max
                self.str_to_int(max, self.max)      #pengubahan max ke integer, isi self.max

            #isi need, didapatkan dari max-allocation, jika hasilnya negatif maka terjadi deadlock karena data tidak feasible
            for proc_need in range (self.process):     #perulangan untuk menarik semua data need dan memindahkannya ke self.need
                save = []      #penyimpanan sementara untuk need per process
                for proc_single in range (self.instance):       #perulangan untuk menarik data satuan dalam max dan allocation untuk diproses
                    max = int(self.max[proc_need][proc_single])     #penarikan max, dengan alamat [proses ke berapa][data ke berapa]
                    allocation = int(self.allocation[proc_need][proc_single])   #penarikan allocation, dengan alamat [proses ke berapa][data ke berapa]
                    need = max-allocation   #penghitungan need, dengan pengurangan max dan allocation
                    if need < 0 :   #pengecekan data, apakah feasible ato tidak, jika tidak maka akan terjadi deadlock jika dilanjutkan
                        deadlock += 1   #jika data ditemukan tidak feasibel, data yang tidak feasible akan dihitung
                    save.append(need)   #append data yang di ekstrak
                self.need.append(save)      #append data yang sudah di save setelah diproses
            #mengcopy data available untuk data yang tersedia untuk mengerjakan proses (avaforwork)
            self.avaforwork = copy.deepcopy(self.available)     
            for proc_work in range(self.instance):      #pengulangan untuk menarik instance yang ingin dikerjakan, pengulangan akan terus dilakukan hingga
                num = self.avaforwork[0].pop(0)     #penarikan data ke-0 pada avaforwork
                for proc_single_work in range(self.process):    #pengulangan untuk menarik data dari program untuk dikerjakan
                    min = self.allocation[proc_single_work][proc_work]      #penarikan data allocation yang kemudian akan digunakan untuk menghitung need, dengan alamat [proocess][instance]  
                    num = num - min     #penghitungan need, dengan avaforwork dikurangi dengan allocation
                    if num < 0 :        #pengecekan data, apakah feasible ato tidak, jika tidak maka akan terjadi deadlock jika dilanjutkan
                        deadlock += 1   #jika data ditemukan tidak feasibel, data yang tidak feasible akan dihitung
                self.avaforwork[0].append(num)    #append data yang sudah di proses
        except:     #in case data tidak valid, maka akan terjadi deadlock
                deadlock+=1     #jika data invalid, data yang tidak akan dihitung dan dianggap terjadi deadlock
                print("Data tidak Valid!")      # output print
        #jika ditemukan adanya deadlock pada proses fungsi filter, maka data akan di return False dan output terjadi deadlock
        if deadlock > 0 :       
            print("Terjadi Deadlock!")
            return False
