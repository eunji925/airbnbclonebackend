from django.db import models

# Create your models here.
class House(models.Model):

    """ Model Definition for Houses"""

    name = models.CharField(max_length=140) # 텍스트
    price_per_night = models.PositiveIntegerField(
        verbose_name="price", help_text="Positive Numbers only"
    ) # 양수
    description = models.TextField() # CharField 보다 긴 텍스트
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=True, help_text= "Does this house allow pets?"
    ) # CheckBox

    # ForeignKey 설정
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    
    # house class의 string method의 형태를 설정한다.
    def __str__(self):
        return self.name 