from django.urls import path
from .views import home, categorypage, subcategorypage,article, reporter,chekIdCard
from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = [

	path('', home, name='home'),
	path('reporter', reporter, name='reporter-page'),	
	path('checkID/',chekIdCard,name="reporter-ID"),
	path('<slug:category>', categorypage, name='category_post_list' ),
	path('<slug:category>/<slug:subcategory>', subcategorypage, name='subcategory_post_list' ),
	path('<slug:category>/<int:id>/<slug:article>', article, name='article')
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 