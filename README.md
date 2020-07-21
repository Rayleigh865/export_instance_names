# export_instance_names

使い方

```
$ python main.py test000-010.test.com
test000.test.com
test001.test.com
test002.test.com
test003.test.com
test004.test.com
test005.test.com
test006.test.com
test007.test.com
test008.test.com
test009.test.com
test010.test.com
```

命名規則が決まっているインスタンスを連番でリスト化したい時などに使ってください。
こんな感じでテキストにも書き出せます。

```
$ python main.py test000-010.test.com > text.txt
$ cat text.txt
test000.test.com
test001.test.com
test002.test.com
test003.test.com
test004.test.com
test005.test.com
test006.test.com
test007.test.com
test008.test.com
test009.test.com
test010.test.com
```