class SinhVien:
    # Các thuộc tính
    _id = ''
    _ten = ''

    # Hàm tạo
    def __init__(self, id, ten):
        self._id = id
        self._ten = ten

    # Getter - Setter
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id_new):
        self._id = id_new

    @property
    def ten(self):
        return self._ten

    @ten.setter
    def ten(self, new_ten):
        self._ten = new_ten

    def __str__(self):
        return f"Id: {self.id} | Tên sinh viên: {self.ten}"
