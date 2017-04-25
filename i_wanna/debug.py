def coinGreedy(money, cash_type):
    def coinGreedyRecursive(money, cash_type, res, idx):
        if idx >= len(cash_type): #화폐 다 사용 시 종료
            return res

        dvmd = divmod(money,cash_type[idx]) #divmond(362,100) => (3,62)
        res[cash_type[idx]] = dvmd[0]       #res[100] = 3
        return coinGreedyRecursive(dvmd[1],cash_type,res,idx+1)

    cash_type.sort(reverse=True)  # 화폐 내림차순 정렬
    return coinGreedyRecursive(money,cash_type,{},0)

    #coinGreedyRecursive(362,[100,50,1],res,0) => 1 res= {}
    #coinGreedyRecursive(62,[100,50,1],res,1) => 2 res = {100:3}
    #coinGreedyRecursive(12,[100,50,1],res,2) => 3 res = {100:3, 50:1}
    #coinGreedyRecursive(0,[100,50,1],res,3) => 4 res ={100:3, 50:1, 1:12}


money = int(input('액수입력 : '))
cash_type = [int(x) for x in input('화폐단위를 입력하세요 : ').split(' ')]
res = coinGreedy(money,cash_type)
for key in res:
    print('{0}원 : {1}개'.format(key,res[key]))