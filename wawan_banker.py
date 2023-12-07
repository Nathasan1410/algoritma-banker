print("DIBUAT MODE COLLAPSE UNTUK BISA JALANKAN PROGRAM")
print()
print("-----BANKER ALGORITHM-----")
print("PROGRAM INI MEMERLUKAN INPUTAN>>> INSTANCE, JumlahProses, Allocation, MAX")
print("Disusun: Kelompok 1")
print()
try:
    jinstance=int(input("Masukkan jumlah Instance:"))  #acuan

    instance=[]


    for i in range(jinstance):
        angkainstance=int(input("Masukkan Instance: "))
        instance.append(angkainstance)



    jproses=int(input("Masukkan jumlah proses: ")) #acuan

    proses=[]

    for i in range(jproses):
        proses.append(f"P{i}")


    print()

    #Allocation
    print("MASUKKAN JUMLAH ALLOCATION")

    alloc=[]

    for i in range(jproses):
        allocdata=input(f"Masukkan data sebanyak *{jinstance}* dan parameter koma , pemisah: ")
        hasilalloc=allocdata.split(",")
        alloc.append(hasilalloc)

    #ubah dari string ke integer
    for i in range(len(alloc)):
        for j in range(len(alloc[i])):
            alloc[i][j]=int(alloc[i][j])
            
    print()
    
    #TOTAL ALLOCATION
    totalalloc=[]  #ACUAN
    
    for i in range(jinstance):
        totalalloc.append(0)
    
    for i in range(jproses):
        for j in range(len(alloc[i])):
            totalalloc[j]+=alloc[i][j]
            
    
    #KETERSEDIAAN RESOURCE
    tersediaResource=[]
    
    for i in range(len(instance)):
        hasil=instance[i]-totalalloc[i]
        tersediaResource.append(abs(hasil))
    
   
    print()
    
    
    #max
    print("MASUKKAN JUMLAH MAX")

    max=[]

    for i in range(jproses):
        maxdata=input(f"Masukkan data sebanyak *{jinstance}* dan parameter koma , pemisah: ")
        hasilmax=maxdata.split(",")
        max.append(hasilmax)

    #ubah dari string ke integer
    for i in range(len(max)):
        for j in range(len(max[i])):
            max[i][j]=int(max[i][j])


    #NEED
    
    Need=[]
    
    for i in range(jproses):
        tneed=[]
        for j in range(len(alloc[i])):
            hasil=alloc[i][j]-max[i][j]
            tneed.append(abs(hasil))
        Need.append(tneed)
    
    print()
    
    #tampilan kerja
    print("Allocation :",instance)
    print()
    print("Ketersediaan Resource :",tersediaResource)
    print()
    
    print(f"Proses  Allocation   MAX      NEED")
    for i in range(jproses):
        print(f"  {proses[i]}    {alloc[i]} {max[i]} {Need[i]}")
    
    print()
    print("TOTAL ALLOCATION: ",totalalloc)
    print()

    
    
    #PROGRAM UTAMA
    hasilakhirproses=[]
    
    
    acuanResource=tersediaResource.copy() 
    
    i=0
    
    while i < len(Need):
        if Need[i]<=acuanResource:
            
            for j in range(jinstance):
                acuanResource[j]+=alloc[i][j]

            hasilakhirproses.append(proses[i])
            proses.remove(proses[i])
            alloc.remove(alloc[i])
            max.remove(max[i])
            Need.remove(Need[i])
            
            i=0
            
        else:
            i+=1
            
                
    
    print()     
            
   
    # Hasil
    hasilmurni=[]
    hasilak=[]
    if acuanResource==instance:
        
        print("Alur safe data : ")
        for i in hasilakhirproses:
            hasilmurni.append(f"{i}")
            hasilak.append(f"{i} ->")
        
        hasilak.pop()
        
        hasilak.append(hasilmurni[-1])
        
        
        for i in hasilak:
            print(i,end=" ")
            
    else:
        print("tidak ada hasil tidak bisa dikerjakan")
        
    
    
    
except:
    print("Kesalahan inputan")
