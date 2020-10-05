
import itertools
import copy

def func():
  #ある選好の組み合わせにおける、アルゴリズム回数を求める関数を組む
  #男側は現在の状態を表す変数、女側は現在キープしてる男の数値を表す変数を用意
  aStatus=[0,0,0,0]
  bKeep=[0,0,0,0]

  #aStatusが1の場合は仮カップルが成立しているため選好が行われない
  #bKeepの中には、現在キープしている男の番号が記録される
  #マッチングは全てのaStatusが1になった段階で終了する。
  ans=0
  sbj=[1,2,3]

  while aStatus!=[0,1,1,1]:
    #「iの選好順位が1位の女」にとってのiのキープ順位と、「iの選好順位が1位の女」の現在のキープ順位を比較して、それに応じて操作を場合分けする。
    
    for i in sbj:
      print("現在男",i,"の操作を行っています")
      print([female[male[i][0]].index(1),male[i][0]])
      if bKeep[male[i][0]]!=0:
        if female[male[i][0]].index(i)<female[male[i][0]].index(bKeep[male[i][0]]): #iの方がキープ順位が上の場合
          #bKeep[i[0]]のリストからこの女を除外し、bKeep[a1[0]]の状態を0にする
          male[bKeep[male[i][0]]].remove(male[i][0])
          aStatus[bKeep[male[i][0]]]=0

          #bKeep[i[0]]（女のキープ）を更新し、iのaStatusは状態を1にする
          bKeep[male[i][0]]=i
          aStatus[i]=1
        else: #iのキープ順位が、元のキープ順位より下の場合
          #女のキープ順位には変化はなく、iのリストからこの女を除外する
          male[i].remove(male[i][0])
      else:
        #bKeep[i[0]]（女のキープ）を更新し、iのaStatusは状態を1にする
        bKeep[male[i][0]]=i
        aStatus[i]=1
    
    print("女側のキープ番号は",bKeep)
    print("現在の男の操作完了状態は",aStatus,"です。[0,1,1,1]になったら操作が完了します")

    #フリーになった男は、次のwhile周回においては操作から除外される。
    #逆にフリーでなくなった男は、次のwhile周回において操作に追加される。
    #この状態はaStatusから読み取る。
    temp=[]
    for i in range(1,4):
      if aStatus[i]==0:
        temp.append(i)
    sbj=temp
    print("次のwhile周回の男は",sbj,"です")
    ans+=1
  
  ansli[ans]+=1
  if ans==4:
    four.append(tempmale)


ansli=[0,0,0,0,0,0,0,0,0,0,0,0]
four=[]

#選好を全パターン用意して、それぞれの組み合わせで先ほど用意した関数を実行
for a1 in itertools.permutations([1,2,3],3):
  for a2 in itertools.permutations([1,2,3],3):
    for a3 in itertools.permutations([1,2,3],3):
      for b1 in itertools.permutations([1,2,3],3):
        for b2 in itertools.permutations([1,2,3],3):
          for b3 in itertools.permutations([1,2,3],3):
            male=[0,list(a1),list(a2),list(a3)]
            tempmale=[0,list(a1),list(a2),list(a3)]
            female=[0,list(b1),list(b2),list(b3)]
            func()

print(ansli)
print(four)





