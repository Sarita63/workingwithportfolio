from django.db import models

# Create your models here.
class Contact(models.Model):
	name=models.CharField(max_length=300)
	email=models.EmailField(max_length=300)
	subject=models.TextField()
	message=models.TextField()


	def __str__(self):
		return self.name




class Feedback(models.Model):
	name=models.CharField(max_length=300)
	post=models.CharField(max_length=300)
	image=models.TextField()
	message=models.TextField()



	def __str__(self):
		return self.name





class Information(models.Model):
	address=models.CharField(max_length=300)
	address_info=models.CharField(max_length=300)
	phoneno=models.CharField(max_length=300)
	time=models.TextField()
	email=models.CharField(max_length=300)



	def __str__(self):
		return f'{self.address}  {self.phoneno}'







    