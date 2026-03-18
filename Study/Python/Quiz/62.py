#1.생성자 만들기, 
# 맴버 private id:num, name:str, pnum:str,
# 메소드  공부하다() : 공부를 합니다.
    #getter/setter
class Student:
    def __init__(self, id, name, pnum):
        self.__id = id
        self.__name = name
        self.__pnum = pnum

    def study(self):
        print("공부를 합니다.")

    def get_Id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_pnum(self):
        return self.__pnum        
    
    def set_id(self, new_id):
        self.__id = new_id

    def set_name(self, new_name):
        self.__name = new_name

    def set_pnum(self, new_pnum):
        self.__pnum = new_pnum
      
    
student = Student(1,'홍길동','010-1111-1111')
student.study()
print(student.get_Id())
print(student.get_name())
print(student.get_pnum())
student.set_id(2)
student.set_name('김수한')
student.set_pnum('010-2222-3333')
print(student.get_Id())
print(student.get_name())
print(student.get_pnum())

---기본 생성자처럼 사용하고 싶을때는 이렇게 수정, __str__ 함수 추가---
#1.생성자 만들기, 
# 맴버 private id:num, name:str, pnum:str,
# 메소드  공부하다() : 공부를 합니다.
    #getter/setter
class Student:
    def __init__(self, id = 0, name = '학생', pnum = '010-111-2222'):
        self.__id = id
        self.__name = name
        self.__pnum = pnum

    def study(self):
        print("공부를 합니다.")

    def __str__(self):
        return '{} / {} / {}\n'.format(self.__id, self.__name, self.__pnum)

    def get_Id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_pnum(self):
        return self.__pnum        
    
    def set_id(self, new_id):
        self.__id = new_id

    def set_name(self, new_name):
        self.__name = new_name

    def set_pnum(self, new_pnum):
        self.__pnum = new_pnum
      
    
student = Student(1,'홍길동','010-1111-1111')
student.study()
print(student.get_Id())
print(student.get_name())
print(student.get_pnum())
student.set_id(2)
student.set_name('김수한')
student.set_pnum('010-2222-3333')
print(student.get_Id())
print(student.get_name())
print(student.get_pnum())

hun = Student()
print(hun.get_Id())
print(hun.get_name())
print(hun.get_pnum())
print(student)
