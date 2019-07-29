# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.db import models
# Create your models here.
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #models.ForeignKey – これは他のモデルへのリンク
    title = models.CharField(max_length=200) #models.CharField – 文字数が制限されたテキストを定義するフィールド
    text = models.TextField() #models.TextField – これは制限無しの長いテキスト用です。ブログポストのコンテンツに理想的なフィールド
    created_date = models.DateTimeField(
            default=timezone.now) #models.DateTimeField – 日付と時間のフィールド
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#def publish(self): は何かと言うと、 これこそが先程お話ししたブログを公開するメソッドそのものです。
#def は、これはファンクション（関数）/メソッドという意味です。publish はメソッドの名前で、 変えることもできます。
#メソッドの名前に使っていいのは、英小文字とアンダースコアで、アンダースコアはスペースの代わりに使います。
#（例えば、平均価格を計算するメソッドは calculate_average_price っていう名前にします）

#メソッドは通常何かを return します。
#一つの例が __str__ メソッドにあります。 このシナリオでは、__str__() を呼ぶと、
#ポストのタイトルのテキスト（string）が返ってきます。

#def publish(self): と def __str__(self): の両方が class キーワードに続く行でインデントされているのに気づきましたか？
#Pythonにモデルのメソッドだと伝えるために、class キーワードに続く行(列？)ではメソッドをインデントしましょう。
#そうしないと、メソッドはモデルのものではなくなり、思ってもみない振る舞いをするでしょう。
