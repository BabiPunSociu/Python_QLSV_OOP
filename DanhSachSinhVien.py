import SinhVien

class DanhSachSV():
    lstSV = []
    
    def addSV(self):
        # Tạo newSV
        id1 = input("Nhap id:")
        ten1 = input("Nhap ten:")
        sv = SinhVien.SinhVien(id1, ten1)
        # Add vào list
        self.lstSV.append(sv)
    
    def Delete(self):
        id = input("Nhap id sinh vien can xoa:")
        check=False
        for i in range(len(self.lstSV)):
            if self.lstSV[i].id==id:
                # Xóa
                self.lstSV.pop(i)
                print(f"Da xoa thanh cong sinh vien co id={id}")
                check = True
                break
        if check==False:
            print(f"Khong tom tai sinh vien co id={id}")

    def Update(self):
        id = input('Nhap id sinh vien can sua: id = ')
        check=False
        for i in range(0, len(self.lstSV)):
            if self.lstSV[i].id==id:
                name = input('Nhap ten sinh vien: ')
                self.lstSV[i].ten = name
                print("Da sua ten")
                check=True
                break
        if check==False:
            print(f"Khong tom tai sinh vien co id={id}")

    def ShowStudents(self):
         print("Danh sach sinh vien")
         for sv in self.lstSV:
             print(sv)