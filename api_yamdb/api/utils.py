from django.db.models import Avg

from reviews.models import Review


def rating_avg(self, obj):
    rating = Review.objects.filter(title=obj.id).aggregate(Avg('score'))
    if rating['score__avg'] is None:
        return None
    return round(rating['score__avg'], 1)
