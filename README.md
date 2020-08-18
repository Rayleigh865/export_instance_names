# export_instance_names

使い方

```
$ python main.py test-hoge000~010.test.com list
test-hoge000.test.com
test-hoge001.test.com
test-hoge002.test.com
test-hoge003.test.com
test-hoge004.test.com
test-hoge005.test.com
test-hoge006.test.com
test-hoge007.test.com
test-hoge008.test.com
test-hoge009.test.com
test-hoge010.test.com
```

```
$ python main.py test-hoge000~010.test.com comma
test-hoge000.test.com, test-hoge001.test.com, test-hoge002.test.com, test-hoge003.test.com, test-hoge004.test.com, test-hoge005.test.com, test-hoge006.test.com, test-hoge007.test.com, test-hoge008.test.com, test-hoge009.test.com, test-hoge010.test.com
```

命名規則が決まっているインスタンスを連番でリスト化したい時などに使ってください。
こんな感じでテキストにも書き出せます。

```
$ python main.py test-hoge000~010.test.com list > text.txt
$ cat text.txt
test-hoge000.test.com
test-hoge001.test.com
test-hoge002.test.com
test-hoge003.test.com
test-hoge004.test.com
test-hoge005.test.com
test-hoge006.test.com
test-hoge007.test.com
test-hoge008.test.com
test-hoge009.test.com
test-hoge010.test.com
```