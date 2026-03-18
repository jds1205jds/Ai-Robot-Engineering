class Namecard :

    namecards = []

    @classmethod
    def print(cls):
        print('번호\t이름\t전화번호')
        print('--------------------------------')
        for n in cls.namecards :
            print(str(n))

    def __init__(self, id, name, pnum):
        self.__id =id
        self.__name = name
        self.__pnum = pnum
        Namecard.namecards.append(self)
    
    def __str__(self) :
        return "{}\t{}\t{}".format(self.__id, self.__name, self.__pnum)
    

    @classmethod
    def add(cls):
        id = input("아이디 입력 : ")
        name = input("이름 입력 : ")
        pnum = input("핸드폰 번호 입력 : ")
        Namecard(id,name, pnum)
        print('명함 목록에 '+name+'님이 추가되었습니다')

    @classmethod
    def edit(cls):
        target = input('수정할 id를 입력하세요 >> ')
        for n in cls.namecards :
            if n.__id == target :
                new_id = input('새로운 id 입력 : ')
                new_name = input('새로운 name 입력 : ')
                new_pnum = input('새로운 pnum 입력 : ')
                n.__id = new_id
                n.__name = new_name
                n.__pnum = new_pnum 
                print('수정이 완료되었습니다')
        else :
            print('id를 찾을 수 없습니다')

    @classmethod
    def delete(cls) :
        target = input('삭제할 id를 입력하세요 >> ')
        for n in cls.namecards :
            if n.__id == target :
                cls.namecards.remove(n)
                print('해당 명함이 삭제되었습니다.')
                return
        else :
            print('id를 찾을 수 없습니다')

Namecard('0','홍길동','010-0000-0000')
Namecard('1','이순신','010-1111-1111')

while True :
    print('--------------------------------')
    print('\t명함관리프로그램\t')
    print('1. 명함 목록 ')
    print('2. 명함 추가 ')
    print('3. 명함 수정 ')
    print('4. 명함 삭제 ')
    print('5. 프로그램 종료 ')
    choice = input("메뉴선택 >> ")
    if choice == '1':
        Namecard.print()
    elif choice == '2' :
        Namecard.add()
    elif choice == '3' : 
        Namecard.edit()
    elif choice == '4' :
        Namecard.delete()
    elif choice == '5' :
        print('---------------종료--------------')
        break



