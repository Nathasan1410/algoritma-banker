from file_read import open_file
import copy

class banker_alg:
    def __init__(self, user_inp):
        data : open_file = open_file()
        self.file = data.read_file(user_inp)
        
        if self.file == False:
            return
        
        self.data_filt = data.filter(self.file)

        if self.data_filt == False :
            print ("Program mengalami Deadlock!")
            return
        
        self.process = data.process
        self.instance = data.instance
        self.available = data.available
        self.allocation = data.allocation
        self.max = data.max
        self.need = data.need
        self.avaforwork = data.avaforwork
        self.iterasi = []
        
    def main_body(self):
        if self.file == False or self.data_filt == False :
            return
        loop = True
        deadlock = False
        while loop == True and deadlock == False:
            deadlock = self.banker()
            self.test()
            loop = self.check() 
        if deadlock == False :
            self.print_iterasi()
        else :
            return

    def print_iterasi(self):
        print(f"Urutan iterasi feasible : ")
        for iterasi in range (self.process-1):
            print(self.iterasi[iterasi], end=" -> ")
        print(self.iterasi[self.process-1])

    def check(self):
        done_total = 0
        for done in self.need:
            if done == None :
                done_total +=1
        if done_total == self.process:
            print("Iterasi selesai!") 
            return False
        else :
            return True
                
            
    def banker(self):
        false_count = 0
        for data in range (self.process) :     #cek program
            avail = copy.deepcopy(self.avaforwork[0])
            need = copy.deepcopy(self.need[data])
            allocation = copy.deepcopy(self.allocation[data])
            count = 0
            
            for num in range (self.instance+1):
                if need == None :
                    break

                elif count == self.instance:
                    self.max[data] = None
                    self.allocation[data] = None
                    self.need[data] = None
                    del self.avaforwork[0]
                    self.avaforwork.append(avail)
                    print(f"P{data} telah selesai!")
                    self.iterasi.append(f"P{data}")
                    return False
   
                elif avail[0] >= need[0]:
                    count += 1
                    temp_ava = avail.pop(0)
                    need.pop(0)
                    temp_allocation = allocation.pop(0)
                    new = temp_ava + temp_allocation
                    avail.append(new)
                
                else:
                    false_count += 1
                    print("False")
                    break
        if false_count == self.process:
                print("Terjadi Deadlock!")
                return True
## binary search tree, ganti root, cari terbesar dikiri or terbesar di kanan
    def test(self):
        print(f"""\nExtract : 
P : {self.process}
I : {self.instance}
Available : {self.available}
Allocation : {self.allocation}
Max : {self.max}
Need : {self.need}
Available for Work : {self.avaforwork}
Iterasi : {self.iterasi}""")
    
    def output(self):
        print(f"Kapasitas Resource Kosong : {self.available[0]}")
        print(f"Kapasitas Resource Saat ini : {self.avaforwork[0]}")
        
        print("Process Allocation Max Need")

        for prog in range (0, self.process):
            print(f"P{prog} {self.allocation[prog]} {self.max[prog]} {self.need[prog]}")
    
            
        

def run():
    ok : banker_alg = banker_alg("test1.txt")
    ok.main_body()
run()
    