from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import os


def get_user_path(username):
	return os.path.join('uploads/templates', username)


class Template(models.Model):
	# user = models.OneToOneField(User)
	# html = models.FileField(upload_to="uploads/")
	name = models.CharField(max_length=128, default="")
	created_at = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def sorted_patterns(self):
		patterns = self.questions() + self.forms()
		# patterns += self.accordions()
		return sorted(patterns, key = lambda p: p.position)

	def forms(self):
		# TODO: Obtener forms del template
		return []

	def questions(self):
		from encuestas.models import Pregunta, Opcion
		return Pregunta.objects.filter(template=self)

	def accordions(self):
		from accordion.models import Accordion
		return Accordion.objects.filter(template=self.id)

	def carousels(self):
		patterns = []
		carousels = Carousel.objects.filter(template=template)
		for carousel in carousels:
			patterns.append({
				'carousel': carousel,
				'content': Content.objects.filter(pregunta=carousel),
				'position': carousel.position
			})
		return patterns


class Pattern(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

# Los componentes que forman parte del template implementan este modelo abstracto
class TemplateComponent(models.Model):
    position = models.IntegerField(null=True)
    template = models.ForeignKey(Template, null=True)

    class Meta:
        abstract = True
