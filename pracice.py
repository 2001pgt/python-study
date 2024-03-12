# 변수 선언
a='파이썬'
b='자바'
print('개발 언어에는',a,b,'등이 있어요')

#튜플 
#튜플은 한번 만들면 수정이 불가

fruit=('apple','banana','orange','grape')#중복허용,아무 자료형이나 다넣을수 있음
(mine,*yours)=fruit #언패킹
print(yours)

#세트
#세트는 값들의 순서X중복X
세트={"값1","값2","값3"}
print(세트)
A={1,2,3,4,5,6,7,8,}
B={3,4,5,6,7,8,9,0}
print(A.intersection(B))#교집합
print(A.union(B))#합집합
print(A.difference(B)) #차집합A-B
#튜플은 순서가 없으므로 인덱스 사용불가
#하지만 수정은 가능하다
A.add(11)#11을 추가
print(A)#11이 포함된 결과
A.remove(11)#11을 제거
A.clear()#모든값 삭제
del A#A라는 세트를 완전 삭제
print(A)#완전 삭제된 A

#딕셔너리(사전)
#어떤 단어와 의미가 있다면 여기서 단어를 key,의미를 value라고 한다.
#딕셔너리는{key:value}가 한쌍으로 이루어진다.
#단, 이때 key는 중복X
딕셔너리={'key1':'value1','key2':'value2'}
person={
    '이름':'박규태',#key는 중복만 피하면 다른 자료형태로도 사용가능
    '나이':23,     #value또한 마찬가지로 리스트,숫자,문자,튜플,불리안 등 여러가지 사용가능
    '키':183,
    '몸무게':120}#줄바꿈
print(person['나이'])#딕셔너리 데이터 접근법
print(person['키'])
#오류상황
print(person['별명'])
print(person.get('별명'))#'별명'이라는 'key'에 접근,'key'가 없을시 'None'출력
person['학번']=20#새로운 데이터 추가,단 key가 같을시 value가 변경됨 
        #key #value
person['키']=185#특정 key의 value를 바꾸거나 추가 할 때
person.update({'키':190,'몸무게':90})#여러 key들의 value를 바꿀 때
person.pop('몸무게')#특정 key값 지우기
person.clear()#모든 데이터 삭제
print(person.keys())#모든 key확인
print(person.values())#모든 value 확인
print(person.items())

