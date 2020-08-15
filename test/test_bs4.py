from bs4 import BeautifulSoup

html = '''
<td class="title black">
    <div class="tit3 white" data-no='10'>
        <a href="/movie/bi/mi/basic.nhn?code=189069" title="다만 악에서 구하소서">다만 악에서 구하소서</a>
    </div>
</td>
'''

# 1. tag 조회

def ex01():
    bs = BeautifulSoup(html, 'html.parser')
    #print(bs) 그냥 문서 내용 출력

    tag_td = bs.td
    #print(tag_td)

    tag_a = tag_td.a # a 태그만 뽑아준다
    #print(tag_a)

    #없는 태그를 가져오면?
    tag_h4 = bs.td.h4
    print(tag_h4) # none이라고 나온다.(에러안나옴)

#2. 속성(attribute) 값 가져오기
def ex02():
    bs = BeautifulSoup(html, 'html.parser')
    tag_td = bs.td
    print(tag_td['class']) # class라는 속성을 가져오고 싶을때

    tag_div = bs.div
    #print(tag_div['id']) # 없는 속성달라고 하면 에러가 검출이 된다.

    print(tag_div.attrs)

# 3. attribute로 조회하기기
def ex03():
    bs = BeautifulSoup(html, 'html.parser')

    #찾을때는 함수를 이용해준다.
    tag_td = bs.find('td', attrs={'class' : 'title'})

    #print(tag_td)

    tag_div = bs.find(attrs={'data-no' : '10'})

    print(tag_div)

if __name__ == '__main__' :
    #ex01()
    #ex02()
    ex03()