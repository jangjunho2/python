pdf2wordcloud 개선할점

긴 텍스트를 split을 이용해서 나눳지만 대문자->소문자 로 바꾸는 작업 , . ' 등을 걸러주는 대부분의 작업 필요
-> 자연어 처리 라이브러리 이용

자연어 처리 라이브러리에서는 split() 함수보다 더 세부적인 토큰화 기능을 제공하며,
이러한 함수를 사용하는 것이 보다 안정적인 결과를 얻을 수 있습니다.