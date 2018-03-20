# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521239017.345443
_enable_loop = True
_template_filename = '/edx/htdocs/django/django-react-redux-base/src/homepage/templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['pagetitle']


from django.utils.translation import ugettext as _ 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'main.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def pagetitle():
            return render_pagetitle(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n    ')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pagetitle'):
            context['self'].pagetitle(**pageargs)
        

        __M_writer('\n\n<section class="container about">\n    <h1>О нас</h1>\n\n    <h2>Мы - это жители Ельца, которые решили сохранить достояние своего города в аналах веб.</h2>\n    <p>Наш портал собирает информацию, которая поможет будущим поколениям иметь правдивую информацию о городе и его жителях..</p>\n    \n</section>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagetitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pagetitle():
            return render_pagetitle(context)
        __M_writer = context.writer()
        __M_writer(filters.html_escape(str(_("About"))))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/edx/htdocs/django/django-react-redux-base/src/homepage/templates/about.html", "uri": "about.html", "line_map": {"18": 2, "51": 5, "38": 1, "39": 2, "40": 3, "57": 5, "63": 57, "45": 5, "31": 1}}
__M_END_METADATA
"""
