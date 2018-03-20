from django.shortcuts import render
from testapp.models import Testapp


def test(request):
    testlist = Testapp.objects.all()
    return render(request, 'test.html',{"test_list" : testlist})
