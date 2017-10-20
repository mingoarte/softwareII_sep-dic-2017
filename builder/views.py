import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.views.generic import TemplateView
from builder.models import *
from encuestas.models import *
from builder.forms import *
from encuestas.forms import *
from django.forms import formset_factory
from .forms import *
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

class buildTemplate(TemplateView):
    template_name = 'builder/build.html'

    def get_context_data(self, **kwargs):
        context = super(buildTemplate, self).get_context_data(**kwargs)
              

        return context

    def post(self, request, *args, **kwargs):
        return render(request, '/builder/build.html')


class homeTemplate(TemplateView):
    template_name = 'home.html'

class ver_templatesTemplate(TemplateView):
    template_name = 'ver_templates.html'
    
    def get_context_data(self, **kwargs):
        context = super(ver_templatesTemplate, self).get_context_data(**kwargs)

        context['templates'] = Template.objects.all()
        return context

class revisarTemplate(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        
        template = Template.objects.get(id=(kwargs['templateID']))
        questions = Pregunta.objects.filter(template=template) 
        patterns = []
        for question in questions:
            pattern = {'question': question,
                        'options': Opcion.objects.filter(pregunta=question)}
            patterns.append(pattern)
        context['patterns'] = patterns
        return self.render_to_response(context)


def pollConfig(request):
    
    question_text = request.GET.get('pregunta', None)
    options = request.GET.getlist('opciones[]', None)
    template_pk = request.GET.get('template', None)
    position = request.GET.get('position', None)
    created = request.GET.get('created', None)

    template = Template.objects.get(pk=int(template_pk))
    question = Pregunta.objects.filter(template=template, position=int(position))
    if question.count():
        print("ENTRO")
        question[0].texto_pregunta = question_text
        options2 = Opcion.objects.filter(pregunta=question).delete()
        # options2 = question[0].opcion_set.all()
        # print(options2)
        # for option in options2:
        #     option.delete()

        for option in options:
            Opcion.objects.create(pregunta=question[0], texto_opcion=option).save()

        question[0].save()
    else:
        question = Pregunta.objects.create(texto_pregunta=question_text,template=template,position=int(position))
        question_pk = question.pk
        question.save()

        question = Pregunta.objects.filter(pk=question_pk)
        for option in options:
            Opcion.objects.create(pregunta=question[0], texto_opcion=option).save()
    
    options = Opcion.objects.filter(pregunta=question)
    print (options)
    p1 = list(question.values('texto_pregunta', 'template', 'position'))
    p2 = list(options.values())

    return JsonResponse(data={'question': p1, 'options': p2})


def newTemplate(request):
    name = request.GET.get('name', None)
    template = Template.objects.create(name=name)
    pk = template.pk
    template.save()
    return JsonResponse(data={'id': str(pk)})


