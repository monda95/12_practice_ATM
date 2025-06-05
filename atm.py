#잔액 초기화 == 통장 잔고
balance = 1000

while True: #조건이 트루일 동안 무한으로 반복
    num = input('사용하실 기능의 번호를 선택해주세요(1,입금, 2.출금, 3.영수증보기, 4.종료): ')

    if num == "1":
        deposit_amount = int(input('입금하실 금액을 입력해주세요: '))
        balance += deposit_amount
        print(f'입급하신 금액은 {deposit_amount}원 이고, {balance}원 입니다.')

    if num == "4":
        print('화면을 종료합니다.')
        break
