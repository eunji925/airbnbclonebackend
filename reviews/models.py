from django.db import models
from common.models import CommonModel

class Review(CommonModel):

    """Review from a User to a Room or Experience"""
    user = models.ForeignKey("users.User", on_delete=models.CASCADE,)
    room = models.ForeignKey("rooms.Room", null=True, blank=True, on_delete=models.CASCADE,)
    experience = models.ForeignKey("experiences.Experience", null=True, blank=True, on_delete=models.CASCADE,)
    payload = models.TextField() # review 남기는 부분
    rating = models.PositiveIntegerField() # 별점

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}⭐️"