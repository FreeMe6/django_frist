from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
django.http module defined HttpResponse object APIs

FOR:: 
    content : return content, is const-string.
    charset : response charset.
    status_code : http response status code, such as : [200|204|404|500]
'''

'''
Example Hello Word.
    define a function accept request param.
    use request you can get request params.
    
    here you coding finished , you need add mapping , so jump and looking 
    `urls.py` , yes you get, you need to mapping in it.
'''
def hello(request):
    return HttpResponse('Hello World ! django .... <|`( -_- >3')

def msg(request,name,age):
    return HttpResponse('My name is' + name + ', i am '+ age + 'years old')
