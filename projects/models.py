import uuid
from django.db import models

# Create your models here.



class Project(models.Model):
    #owner
    title = models.CharField(max_length = 200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
    demo_link = models.CharField(max_length=200, null=True, blank=True)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank='True')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
     

    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            img = self.featured_image.url
        except:
            img = ''
        return img        



class tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.name    
    



class review(models.Model):
    
    VOTE_TYPE = (

        ('UP', 'UP'),
        ('down', 'down'),
         
    )



    #owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank= True)

    body = models.TextField(null=True, blank= True)
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    update = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    


    def __str__(self):
        return self.value
    


    
    