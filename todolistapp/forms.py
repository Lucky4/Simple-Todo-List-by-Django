# -*- coding:utf-8 -*-

from django import forms


class AddtaskForm(forms.Form):

    todo = forms.CharField(max_length=64,
                           required=True)
    priority = forms.ChoiceField(widget=forms.RadioSelect(),
                                 choices=((0, u'common'), (1, u'middle'), (2, u'prior'),))
    expire_time = forms.DateTimeField(required=False)
