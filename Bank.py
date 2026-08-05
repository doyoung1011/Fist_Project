import random as rand

class Bank:
    # total=0
    # 이거는 원래 있던 돈이라고 가정함.
    def __init__(self):
        # self.balance=0
        # 아직 계좌번호가 안만들어진 상태임
        self.__account_number=None
        self.balance=0
    '''
    사용자가 은행원보고 개설해줘! 라는 순간 개설되는 설정...
    '''
    def make_account(self):
        self.__account_number=rand.randint(1,3)
        print('계좌 개설 완료되셨습니다',self.__account_number)

    # def get_account(self):
    #     return  self.__account_number
    
       

    
        
      


    # 이전에 있던 돈+보낼 돈
    # def send_money(self,money):
    #     self.balance-=money
    #     print(f'현재 잔고:')
    

    # #  저축하는 상황연출
    # def save_money(self,money):
    #     self.balance+=money
    #     print(f'현재 잔고: ')

     
a=Bank()

# a.save_money(1)

'''
은행이 하는일
 1. 저축
 2. 송금
 3.계좌 개설(random으로 숫자 생성해서 그걸 계좌 번호라고 지정하기.)

 계좌 개설은 은행원만 가능하니까... 

계좌 개설은 은행에서 담당하고 사용자는 개설된 계좌 번호만
조회 가능할 수 있어야함.

getter,setter 개념 적용시키기...

'''