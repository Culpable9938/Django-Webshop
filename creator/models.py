from django.db import models
    
class Rig(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0, blank=False)
    
    max_piece = models.IntegerField(default=0, blank=False)

    
    def __str__(self):
        return self.name
    
class RigImage(models.Model):
    name = models.CharField(max_length=100)
    rig = models.ForeignKey(Rig, on_delete=models.CASCADE)
    
    color = models.CharField(max_length=100)
    
    imagemain = models.ImageField(upload_to="Rig_images/", default="", blank=False)
    image2 = models.ImageField(upload_to="Rig_images/", default="", blank=True)
    image3 = models.ImageField(upload_to="Rig_images", default="", blank=True)
    image4 = models.ImageField(upload_to="Rig_images", default="", blank=True)
    image5 = models.ImageField(upload_to="Rig_images", default="", blank=True)
    image6 = models.ImageField(upload_to="Rig_images", default="", blank=True)

    
    def __str__(self):
        return self.name
    
class Bead(models.Model):
    name = models.CharField(max_length=100)
    
    color = models.CharField(max_length=100)
    
    Types = ((1,'bead'),(2,'charm'))
    type = models.IntegerField(default=1, choices=Types)
    
    imagemain = models.ImageField(upload_to="Bead_images/", default="", blank=False)
    image2 = models.ImageField(upload_to="Bead_images/", default="", blank=True)
    image3 = models.ImageField(upload_to="Bead_images", default="", blank=True)
    image4 = models.ImageField(upload_to="Bead_images", default="", blank=True)
    image5 = models.ImageField(upload_to="Bead_images", default="", blank=True)
    image6 = models.ImageField(upload_to="Bead_images", default="", blank=True)
     
    def __str__(self):
        return self.name
    
class Decor(models.Model):
    name = models.CharField(max_length=100)
    
    Types = ((1,'box'),(2,'bag'), (3,'card'))
    type = models.IntegerField(default=1, choices=Types)
    
    price = models.IntegerField(default=0,blank=True)
    
    imagemain = models.ImageField(upload_to="Decor_images/", default="", blank=False)
     
    def __str__(self):
        return self.name
    
class Font(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=400)

class Message(models.Model):
    
    name = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    body = models.TextField(max_length=300)
    
    font = models.ForeignKey(Font, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    