from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import *
from .forms import ReporterForm
# def nav(request):
# 	category = Category.objects.all()
# 	return render(request, 'news_post/nav.html', {'category': category} )

def home(request):
	advertisment = Advertisment.objects.all()
	video = Video.objects.all()
	category = Category.objects.all()
	exclusive = Video.objects.filter(exclusiveVideo=True).first()
	national = Articles.published.filter(category=Category.objects.filter(slug='national')[0])
	sports = Articles.published.filter(category=Category.objects.filter(slug='sports')[0])
	entertainment = Articles.published.filter(category=Category.objects.filter(slug='entertainment')[0])


	return render(request, 'news_post/index.html',
	 {'newslist': Articles,
	  'category': category,
	  'advertisment':advertisment,
	  'video':video,
	  'national': national,
	   'exclusive': exclusive,
	   'sports': sports,
	   'entertainment': entertainment})

# def base(request):
# 	category = Category.objects.all()
# 	exclusive = Video.objects.filter(exclusiveVideo=True).first()
# 	advertisment = Advertisment.objects.all()

# 	context = {
# 		'category': category,
# 		'advertisment': advertisment,
# 		'exclusive': exclusive,
# 		'newslist': Articles,
# 	}

# 	return render(request, 'news_post/base.html', context)

def categorypage(request, category):
	news = Articles.published.filter(category=Category.objects.filter(slug=category)[0])

	exclusive = Video.objects.filter(exclusiveVideo=True).first()
	advertisment = Advertisment.objects.all()
	category = Category.objects.all()

	context = {
		'category': category,
		'advertisment': advertisment,
		'exclusive': exclusive,
		'newslist': Articles,
		'Articles': news
	}

	return render(request, 'news_post/list.html', context)

def subcategorypage(request, category, subcategory):
	news = Articles.published.filter(
		category=Category.objects.filter(slug=category).first(),
		subcategory= SubCategory.objects.filter(slug=subcategory).first()
		)

	exclusive = Video.objects.filter(exclusiveVideo=True).first()
	advertisment = Advertisment.objects.all()
	category = Category.objects.all()

	context = {
		'category': category,
		'advertisment': advertisment,
		'exclusive': exclusive,
		'newslist': Articles,
		'Articles': news
	}


	return render(request, 'news_post/list.html', context )

def article(request, category, id,  article):
	news = get_object_or_404(Articles,
		category=Category.objects.filter(slug=category).first(),
		slug= article,
		id = id
	)
	national = Articles.published.filter(category=Category.objects.filter(slug='national')[0])
  
	exclusive = Video.objects.filter(exclusiveVideo=True).first()
	advertisment = Advertisment.objects.all()
	category = Category.objects.all()

	context = {
		'category': category,
		'advertisment': advertisment,
		'exclusive': exclusive,
		'newslist': Articles,
		'national': national,
		'article': news
	}
	return render(request, 'news_post/article.html', context )


def reporter(request):
	exclusive = Video.objects.filter(exclusiveVideo=True).first()
	advertisment = Advertisment.objects.all()
	category = Category.objects.all()

	form = ReporterForm()

	# if request.method == 'POST':
		# form = ReporterForm(request.POST)
		# if form.is_valid():
		# 	new_reporter = Reporter.create(request.POST, request.FILES)
		# 	print(request.POST)
		# 	print(new_reporter)
		# 	new_reporter.save()

		# 	return redirect('home')
	if request.method == 'POST':
		form = ReporterForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			return render(request, 'news_post/reporter-success.html')
	else:
		form = ReporterForm()
 
	context = {
		'category': category,
		'advertisment': advertisment,
		'exclusive': exclusive,
		'newslist': Articles,
		'form':form
	}
	
	return render(request, 'news_post/reporter.html', context)

def chekIdCard(request):
	exclusive = Video.objects.filter(exclusiveVideo=True).first()
	advertisment = Advertisment.objects.all()
	category = Category.objects.all()


	employee_id  = request.GET.get('emp_id')
	

	msg = None
	emp = None

	if employee_id is not None and employee_id != '':
		emp = Reporter.objects.filter(emp_id__exact=employee_id, isActive=True).first()
		if emp is None:
			msg = f'Employee id "{employee_id}" is invalid'
		
	context = {
		'category': category,
		'advertisment': advertisment,
		'exclusive': exclusive,
		'newslist': Articles,
		'emp': emp,
		'msg': msg
	}
	
	return render(request, 'news_post/idcard.html', context)