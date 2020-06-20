from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from smart_selects.db_fields import ChainedForeignKey 
from PIL import Image
from django.utils import timezone



class Category(models.Model):
	title = models.CharField(max_length=80)
	slug = models.SlugField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('category_post_list', args=[self.slug])

	@property
	def subcategories(self):
		return self.subcategory.all()


class SubCategory(models.Model):
	title	 = models.CharField(max_length=80)
	slug 	 = models.SlugField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory')
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('subcategory_post_list', args=[self.category.slug, self.slug])


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')


class Articles(models.Model):
	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published')
		)
	
	BiharNews    = models.BooleanField(default=False)
	ChiefNews    = models.BooleanField(default=False)
	PopularNews  = models.BooleanField(default=False)
	BreakingNews = models.BooleanField(default=False)
  
	
	category = models.ForeignKey(Category,  on_delete=models.CASCADE)
	subcategory = ChainedForeignKey(
		SubCategory,
		chained_field = 'category',
		chained_model_field = 'category',
		show_all = False,
		auto_choose = True,
		null = True,
		blank = True, 	
	)

	title 			 =  models.CharField(max_length=200)
	url_title 		 = models.URLField()
	slug 			 = models.SlugField(max_length=250, unique_for_date='publish')
	thumbnail 		 = models.ImageField(default='thumbnails/download.jpeg', upload_to='thumbnails/' )
	shortdescription = models.TextField()
	description 	 = models.TextField()
	publish 		 = models.DateTimeField(default=timezone.now)
	created  		 = models.DateTimeField(auto_now_add=True)
	updated 		 = models.DateTimeField(auto_now=True)
	status 			 = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	objects = models.Manager()
	published = PublishedManager() ## our custom manager
	
	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title

	@property
	def popular(self):
		return Articles.published.filter(PopularNews=True)
		
	@property
	def popular_five(self):
		return self.popular[:5]
	
	@property
	def chief(self):
		return Articles.published.filter(ChiefNews=True)

	@property
	def chief_five(self):
		return self.popular[:5]
	
	@property
	def breaking(self):
		return Articles.published.filter(BreakingNews=True)

	@property
	def bihar(self):
		return Articles.published.filter(BiharNews=True)

		
	@property
	def breaking_five(self):
		return self.popular[:5]
	
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.thumbnail.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.thumbnail.path)
		
	def get_absolute_url(self):
		return reverse('article', args=[self.category.slug, self.id, self.slug])


class Profile(models.Model):
	user 			= models.ForeignKey(User, on_delete=models.CASCADE)
	qualification 	= models.CharField(max_length=80)
	emp_id 			= models.CharField(max_length=80)

	def __str__(self):
		return self.user.name


class Advertisment(models.Model):
	url 	= models.CharField(max_length=1000)	
	title 	= models.CharField(max_length=100)
	image 	= models.ImageField(default='default.jpg',upload_to='advertisment')

	def __str___(self):
		return self.title

class Video(models.Model):
	title 			= models.CharField(max_length=100)
	url 			= models.CharField(max_length=100)
	exclusiveVideo 	= models.BooleanField(default=False)

	def __str__(self):
		return self.title


class Reporter(models.Model):
	emp_id 			= models.CharField(max_length=80, null=True, blank=True, unique=True)
	fname 			= models.CharField(max_length=20)	
	lname 			= models.CharField(max_length=20)
	email 			= models.EmailField()
	image 			= models.ImageField(upload_to="reporter/")
	dob				= models.DateField()
	mob_number  	= models.CharField(max_length=10)
	adhar_number 	= models.CharField(max_length=16)
	qualification  	= models.CharField(max_length=80)
	address   		= models.TextField()
	isReporter		= models.BooleanField(default=False)
	designation 	= models.CharField(max_length=120, null=True, blank=True)
	join_date 		= models.DateField(null=True, blank=True)
	isActive 		= models.BooleanField(default=False)

	@property
	def activeReporter(self):
		return Reporter.objects.filter(isActive=True)
	
	@classmethod
	def get_reporter_by_id(cls, e_id):
		return Reporter.objects.filter(isActive=True).filter(emp_id=e_id)

	def get_absolute_url(self):
		return reverse('reporter', args=[self.emp_id])

	def __str__(self):
		return f'{self.fname} {self.lname} {self.emp_id}'
