#coding: utf-8

from django.db import models

class user_table_prefer(models.Model):
    user = models.ForeignKey('auth.User', verbose_name=u'Пользователь')
    ptable = models.CharField(max_length=100, verbose_name=u'Таблица')
    config = models.TextField(verbose_name=u'Настройки')

    class Meta:
        verbose_name = u'Пользовательские настройки таблиц'
        verbose_name_plural = u'Пользовательские настройки таблиц'

    def __unicode__(self):
        return u"{0} {1}".format(unicode(self.user),unicode(self.ptable))
