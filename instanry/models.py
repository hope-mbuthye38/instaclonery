from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 60)
    image_path = models.ImageField(upload_to = 'uploads/')
    caption = models.TextField()
    user = models.ForeignKey(User, related_name="posted_by", on_delete=models.CASCADE, null=True, blank =True)
    likes = models.ForeignKey(User, related_name='liked_by', on_delete=models.CASCADE,blank =True, null=True)
    comments=models.ForeignKey('Comment', on_delete=models.CASCADE, blank =True, null=True)
    post_date = models.DateTimeField(auto_now=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_name(cls,search_term):
        names = cls.objects.filter(name__icontains=search_term)
        return names
        
    @classmethod
    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.name

    @classmethod
    def update_caption(cls, caption):
        update = cls.objects.filter(id = id).update(caption=caption)
        update.save()
    
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to = 'profile/')
    bio=models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def get_profile(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

class Like(models.Model):
    like= models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_liked = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.like)

class Comment(models.Model):
    message= models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
    def add_comment(self):
        self.save()

    class Meta:
        ordering = ['created_on']

    def get_post_comments(cls, image_id):
        comments = cls.objects.filter(image_id=image_id)
        return comments

    @classmethod
    def get_comments(cls):
        comments=cls.objects.all()
        return comments
# Create your models here.
