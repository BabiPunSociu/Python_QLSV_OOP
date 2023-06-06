import DanhSachSinhVien

def showMenu():
    print("===== MENU =====")
    print("1. Them sinh vien")
    print("2. Sưa sinh vien")
    print("3. Xóa sinh vien")
    print("4. Hien thi DSSV")
    print("0. Thoat")
    luachon = input('Nhap lua chon: ')
    return luachon

if __name__=="__main__":
    DanhSach = DanhSachSinhVien.DanhSachSV()
    while(True):
        luaChon = showMenu()
        if luaChon=='0':
            print('Byeee...')
            break
        elif luaChon=='1':
            DanhSach.addSV()
        elif luaChon=='2':
            DanhSach.Update()
        elif luaChon=='3':
            DanhSach.Delete()
        elif luaChon=='4':
            DanhSach.ShowStudents()