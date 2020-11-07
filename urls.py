import django
from django.url import path
from . import vote

urlpatterns = {
    path("voteApi",vote.rec,name='voteRec')
}