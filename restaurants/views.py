from django.http import HttpResponse
from django.shortcuts import render


# function based view
def home(request):

    html_var = 'f strings'

    html_ = f"""
        <html lang=en>
        <head>
        </head>
        
        <body>
            <h1>Hello World</h1>
            <p>This is {html_var} coming through</p>
        </body>
        
        </html>
    """

    return HttpResponse(html_)
    #return render(request, 'home.html', {})
