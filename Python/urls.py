"""Jukka Pirinen  8.9.2016
"""Djangon urls.py tiedosto

from django.conf.urls import url
from Apit.views import Teht3, Teht4, Teht4Tulos, Teht5, Teht6, Teht7, Teht8, Teht8Tulos,\
                        Teht9, Teht9Tulos, TehtKymppi, TehtKymppiTulos, TehtKymppiLogged,\
                        UusiHarjoitus, Yhteenveto, VieKantaan

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^Teht3/', Teht3),
    url(r'^Teht4/', Teht4),
    url(r'^Teht4Tulos/', Teht4Tulos),
    url(r'^Teht5/', Teht5),
    url(r'^Teht6/', Teht6),
    url(r'^Teht7/', Teht7),
    url(r'^Teht8/', Teht8),
    url(r'^Teht8Tulos/', Teht8Tulos),
    url(r'^Teht9/', Teht9),
    url(r'^Teht9Tulos/', Teht9Tulos),
    url(r'^TehtKymppi/', TehtKymppi),
    url(r'^TehtKymppiTulos/', TehtKymppiTulos),
    url(r'^TehtKymppiLogged/', TehtKymppiLogged),
    url(r'^UusiHarjoitus/', UusiHarjoitus),
    url(r'^Yhteenveto/', Yhteenveto),
    url(r'^VieKantaan/', VieKantaan)
]
