# Banker Algorithm By Kelompok 1

import copy

class open_file :

    def __init__(self):
        self.process = 0    
        self.instance = 0   
        self.available = []     
        self.allocation = []    
        self.max = []   
        self.need = []  
        self.avaforwork = []    

    def read_file(self, filename):

        try:                
            f = open(filename, "r")         
            return f.readlines()     

        except:                           
            print(f"'{filename}' tidak ditemukan!")
            return False        

    def str_to_int (self, data, address):   
        temp = []       
        for string in data:     
            temp.append(int(string))    
        address.append(temp)    

    def filter(self, all_lines):        
        deadlock = 0        
        self.process = int(all_lines[0])        
        self.instance = int(all_lines[1])       

        available = all_lines[2].replace('\n','').split(',')     
        self.str_to_int(available, self.available)       

        try:

            for proc_all in range (self.process):       
                allocation = all_lines[3+proc_all].replace('\n','').split(",")      
                self.str_to_int(allocation, self.allocation)        

            for proc_max in range (self.process):   
                max = all_lines[3+proc_max+self.process].replace('\n','').split(",")    
                self.str_to_int(max, self.max)      

            for proc_need in range (self.process):     
                save = []      
                for proc_single in range (self.instance):       
                    max = int(self.max[proc_need][proc_single])     
                    allocation = int(self.allocation[proc_need][proc_single])   
                    need = max-allocation   
                    if need < 0 :   
                        deadlock += 1   
                    save.append(need)   
                self.need.append(save)      

            self.avaforwork = copy.deepcopy(self.available)     
            for proc_work in range(self.instance):      
                num = self.avaforwork[0].pop(0)     
                for proc_single_work in range(self.process):    
                    min = self.allocation[proc_single_work][proc_work]      
                    num = num - min     
                    if num < 0 :        
                        deadlock += 1   
                self.avaforwork[0].append(num)    
        except:     
                deadlock+=1     
                print("Data tidak Valid!")    

        if deadlock > 0 :       
            print("Terjadi Deadlock!")
            return False

