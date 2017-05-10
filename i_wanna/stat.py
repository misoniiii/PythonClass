# #1-1
# file = open("/Users/misoni/Desktop/pythondata/winter.txt",'r',encoding='CP949')
# tot_word =[]  #단어 하나씩 넣기 ( 특수문자나 공백 처리 추가 작업 필요)
# for winter_list in file:
#     split = winter_list.split(' ')
#
#     for i in split:
#         word =i.strip('\n')
#         tot_word.append(word.lower())
#
# def mean(val):
#     tot = len(tot_word) #tot = 겨울왕국의 전체 단어 개수
#     cnt = 0        #cnt = 입력한 단어 개수
#     for i in tot_word:
#         if i == val:
#             cnt = cnt + 1
#     res = round(float(cnt/tot),5)
#     return(res)
#
# print(mean('the'))
#
#
# #1-2
# import csv
# file = open("/Users/misoni/Desktop/pythondata/emp2.csv", "r")
# emp_csv = csv.reader(file)
#
# clerk_cnt = 0 #clerk 인원수
# clerk_20_inter_cnt = 0 #clekr&부서번호 20인원수
# for i in emp_csv:
#     if i[2]  == 'CLERK':
#         clerk_cnt += 1
#         if i[-1] == '20':
#             clerk_20_inter_cnt += 1
# res = clerk_20_inter_cnt / clerk_cnt
# print(res)
#
# #1-3
# import csv
# file = open("/Users/misoni/Desktop/pythondata/emp2.csv", "r")
# emp_csv = csv.reader(file)
# hiredate_cnt = 0
# hire_20_inter_cnt = 0
# for i in emp_csv:
#     if i[4][0:4]=='1981':
#         hiredate_cnt += 1
#         if i[-1] == '20':
#             hire_20_inter_cnt += 1
# res = hire_20_inter_cnt / hiredate_cnt
# print(res)
#
#
# #1-4,5
# import csv
# import numpy
# file = open("/Users/misoni/Desktop/pythondata/emp2.csv", "r")
# emp_csv = csv.reader(file)
# sal_list=[]
# for i in emp_csv:
#     sal_list.append(int(i[5]))
# sal_mean = numpy.mean(sal_list)
# sal_var = numpy.var(sal_list)   #sal_var2= sum((sal_list-sal_mean)**2) / len(sal_list)
# sal_std = numpy.std(sal_list)
# print(sal_mean, sal_var, sal_std)
#
# #1-6,7
# #pandas
# import pandas as pd
# emp= pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
# sal_mean = emp.groupby('deptno')['sal'].mean()
# sal_var = emp.groupby('deptno')['sal'].var()
# sal_std = emp.groupby('deptno')['sal'].std()
# print(sal_mean)
# print(sal_var)
# print(sal_std)
#
#
# #numpy 부서별 평균월급
# import numpy, csv
# # file = open("/Users/misoni/Desktop/pythondata/emp2.csv", "r")오픈은 한번만 해줌
# # emp_csv = csv.reader(file)
#
# deptno = ['10','20','30']
# for i in deptno:
#     sal_list=[]
#     file = open("/Users/misoni/Desktop/pythondata/emp2.csv", "r")
#     for j in csv.reader(file):
#         if j[-1] == i:
#             sal_list.append(int(j[5]))
#     print(i, round(numpy.mean(sal_list)))
#     file.close()
#
#
# #####
# create or replace function no3_cancer
# ( p_cancer number,
# p_positiveGivenCancer number)
# return number
#
# is
# v_cancer                number(10,6) := p_cancer; --p(cancer) : 폐암에 걸린 확률
# v_positiveGivenCancer   number(10,6) := p_positiveGivenCancer; --p(+|cancer) : 폐암일때 양성판정 받을 확률
# v_positive              number(10,6) ; --p(+) : 양성인 확률
# v_res                   number(10,6);
#
# begin
#     v_positive := (1-v_positiveGivenCancer)*(1-v_cancer) + (v_positiveGivenCancer*v_cancer) ;
#     v_res := (v_positiveGivenCancer*v_cancer ) / v_positive;
#
#
#     return v_res;
# end;
#
# def no3_cancer(cancer,positiveGivenCancer):
#     list = [cancer,positiveGivenCancer]
#     positive = (1-list[1])*(1-list[0]) + (list[1]*list[0])
#     res = (list[1]*list[0])/positive
#     return res
#
# print(no3_cancer(0.01,0.99))



to_change = 1/ㅜ