from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
 
class Courses(BaseModel):
    course_name = models.CharField(max_length=100)
    slug= models.SlugField(unique=True , null=True , blank=True)
    course_image= models.ImageField(upload_to="course_image")
    course_title=models.TextField()
    course_price=models.IntegerField()
    course_enrolled=models.IntegerField()
    discout_price=models.FloatField(default=0)


    def save(self , *args , **kwargs):
        self.slug = slugify(self.course_name)
        super(Courses ,self).save(*args , **kwargs)


    def __str__(self) -> str:
        return self.course_name


# class ColorVariant(BaseModel):
#     color_name = models.CharField(max_length=100)
#     price = models.IntegerField(default=0)

#     def __str__(self) -> str:
#         return self.color_name

# class SizeVariant(BaseModel):
#     size_name = models.CharField(max_length=100)
#     price = models.IntegerField(default=0)
    
#     def __str__(self) -> str:
#         return self.size_name




class Course_Description(BaseModel):
    course= models.ForeignKey(Courses, on_delete=models.CASCADE , related_name="products")
    product_desription = models.TextField()
    about_course=models.TextField()
    what_will_learn=models.TextField()
    requirements=models.TextField()
    note_from_instructor=models.TextField()


    
    # def save(self , *args , **kwargs):
    #     self.slug = slugify(self.product_name)
    #     super(Product ,self).save(*args , **kwargs)


    def __str__(self) -> str:
        return self.course.course_title
    
    # def get_updated_price(self,size):
    #     print(size)
    #     return self.price+SizeVariant.objects.get(size_name = size).price




# class ProductImage(BaseModel):
#     product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="product_images")
#     image =  models.ImageField(upload_to="products")