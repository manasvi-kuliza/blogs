from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField


class ModelBase(models.Model):
    """
    abstract model class to add is_deleted, created_at and modified at fields in any model
    """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """ Soft delete """
        self.is_deleted = True
        self.save()


class Blog(ModelBase):
    """
    model to save blog information
    """
    blog_number = models.CharField(max_length=254, unique=True)  # unique identifier
    title = models.TextField(default="")  # blog's title


class Paragraph(ModelBase):
	"""
	model to save blog's paragraphs
	"""
	blog = models.ForeignKey(Blog, null=True, blank=True)
	paragraph_number = models.CharField(max_length=254, unique=True)
	sequence = models.IntegerField()
	body = models.TextField(default="")


class Comment(ModelBase):
	"""
	model to save comments for a paragraph 
	"""
	paragraph = models.ForeignKey(Paragraph, null=True, blank=True)
	message = models.TextField(default="")