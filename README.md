# -Hello-World-action-pipeline-
В [/.github/worflows/hello_world.yaml](https://github.com/UnknownC3PO/-Hello-World-action-pipeline-/blob/main/.github/workflows/hello_world.yaml) лежит github action pipeline, который перекидывает [hello_world.py](https://github.com/UnknownC3PO/-Hello-World-action-pipeline-/blob/main/hello_world.py) в функцию aws lambda. 
***
[hello_world.py](https://github.com/UnknownC3PO/-Hello-World-action-pipeline-/blob/main/hello_world.py) реализует [кольцевой буфер](https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BB%D1%8C%D1%86%D0%B5%D0%B2%D0%BE%D0%B9_%D0%B1%D1%83%D1%84%D0%B5%D1%80).
***
Простенький пример на python ```z[int(time.time())%len(z):]+z[:int(time.time())%len(z)]``` где z-массив с нашими табличными данными поля "title"  которые мы распарсили с airtable. С помощью ```time.time()%len(z)``` мы получаем индекс который постоянно меняеться ([time.time()](https://www.programiz.com/python-programming/time) - время в секундах с начала эпохи) то есть каждую секунду двигается вперед, таким образом
```z[int(time.time())%len(z):]``` дает нам данные 'title' c текущей позиции и до конца массива, а ```+z[:int(time.time())%len(z)]``` прибавляет остальнные данные, и так происходит с 0 индекса и двигаемся вплоть до конечного когда при получении остатка мы получаем ноль и возвращаемся к начальному состоянию массива.
