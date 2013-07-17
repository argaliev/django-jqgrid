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
        
    def get_sortname(self, model_fields, default_sortname):
        """ Get saved sortname. Check that saved sortname exist in
        modelclass fields, in case of deletion, or rename of field
        Args:
            model_fields(list of str): list of modelclass fields names
        Returns:
            saved sortname if name exist, default_sortname otherwise """
        if self.sortname and self.sortname in model_fields:
            return self.sortname
        return default_sortname

    def get_gridstate(self):
        if self.hidegrid:
            return True if self.hidegrid == 'hidden' else False
        return None

    def get_colsorder(self, model_fields):
        """ Reorder model fields if saved config exist.
        Args:
            model_fields(list of str): list of modelclass fields names
        Returns:
            ordered model fields names list
        """
        if self.colsorder:
            fields_count = len(model_fields)-1
            for x,saved_fld_name in enumerate(simplejson.loads(self.colsorder)):
                for y,fld_name in enumerate(model_fields):
                    if saved_fld_name == fld_name:
                        if x <= fields_count:
                            model_fields[y], model_fields[x] = model_fields[x], model_fields[y]
                            break
        return model_fields

    def get_colmodel(self):
        if self.colmodel:
            return simplejson.loads(self.colmodel)
        return None
