from django.db import models


class wp_term_taxonomy(models.Model):
    taxonomy = models.CharField(max_length=100)
    term_id = models.IntegerField()
    description = models.CharField(max_length=400)
    parent = models.IntegerField()
