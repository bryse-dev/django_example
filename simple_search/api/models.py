from django.db import models

MATCHER_ENUM = [("MATCHER1", "search matcher 1"), ("MATCHER2", "search matcher 2")]


class Search(models.Model):
    name = models.CharField(max_length=100)
    matcher = models.CharField(choices=MATCHER_ENUM, max_length=64)
