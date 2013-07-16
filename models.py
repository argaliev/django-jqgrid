#coding: utf-8

from django.db import models

class user_table_prefer(models.Model):
    user = models.ForeignKey('auth.User', verbose_name=u'Пользователь')
    ptable = models.CharField(max_length=100, verbose_name=u'Таблица')
    prefer = models.TextField(verbose_name=u'Настройки')
    hidegrid = models.CharField(max_length=100, verbose_name=u'Скрыть/Показать')
    filters = models.TextField(verbose_name=u'Фильтры')
    colmodel = models.TextField(verbose_name=u'Параметры колонок')
    sortname = models.CharField(max_length=100, verbose_name=u'Поле сортировки')
    sortorder = models.CharField(max_length=100, verbose_name=u'Порядок сортировки')
    colsorder = models.TextField(verbose_name=u'Порядок полей')
    rowcount = models.IntegerField(verbose_name=u'Записей на страницу')

    class Meta:
        verbose_name = u'Пользовательские настройки таблиц'
        verbose_name_plural = u'Пользовательские настройки таблиц'

    def __unicode__(self):
        return u"{0} {1}".format(unicode(self.user),unicode(self.ptable))
