from django.db import models

MATCHER_ENUM = [("MATCHER1", "search matcher 1"), ("MATCHER2", "search matcher 2")]
STATUS_ENUM = [("CREATED", "step one of searching"), ("RUNNING", "step two of searching")]


class Search(models.Model):
    name = models.CharField(max_length=100)
    matcher = models.CharField(choices=MATCHER_ENUM, max_length=64)
    status = models.CharField(choices=STATUS_ENUM, default="CREATED", max_length=64)
    percent_complete = models.FloatField(default=0)
