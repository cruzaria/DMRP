from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timedelta

@view_function
def process_request(request):
    context = {
        jscontext('now'): datetime.now(),
    }
    return request.dmp.render('index.html', context)


@view_function
def gettime(request):
    context = {
        'now': datetime.now(),
    }

    return request.dmp.render('index.gettime.html', context)


# return CSV
#return request.dmp.render('my_csv.html', {}, content_type='text/csv')

# return a custom error page
#return request.dmp.render('custom_error_page.html', {}, status=404)

# specify a different template charset (or set globally in settings.py)
#return request.dmp.render('im_old.html', {}, content_type='cp1252')

#mystr = render_template(request, 'homepage', 'custom.html', context, subdir="customsubdir")

#   from django_mako_plus import get_template
# template = get_template('homepage', 'index.html')
  
    # def process_request(request, purchase:Purchase):
    # the `purchase` variable has already been pulled from the database

#django way
#return render(request,  'homepage / index.html',  context,  using='django_mako_plus')

#if need Template
#return TemplateResponse(request, dmp_get_template('homepage', 'index.html'), context)
 
    # replace 'homepage' with the name of any DMP-enabled app:
#return HttpResponse(render_template(request, 'homepage', 'index.html', context))
    # replace 'homepage' with the name of any DMP-enabled app:
#return render(request, 'homepage/index.html', context)


# @view_function
# def process_request(request, hrs: int, mins: int, forward: bool=True):
#     delta = timedelta(hours=hrs, minutes=mins)
#     if forward:
#         now = datetime.now() + delta
#     else:
#         now = datetime.now() - delta
#     context = {
#         'now': now,
#     }
#     return request.dmp.render('index.html', context)
