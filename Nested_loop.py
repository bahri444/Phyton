# data string dengan perulangan di dalam perulangan
nama_mhs=["saepul", "bahri"]
ProgDi=["teknik informatika", "sistem informasi"]

# bagian loop
for Nm in nama_mhs:
    for Prodi in ProgDi:
        print(Nm, ": mengambil jurusan : ", Prodi)