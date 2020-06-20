from django import forms
from .models import Reporter


class ReporterForm(forms.ModelForm):
	class Meta():
		model = Reporter
		fields=['fname','lname','email','image','dob','mob_number','adhar_number','qualification','address']
		
		widgets = {
			'fname' : forms.TextInput(attrs={
				'placeholder': 'Enter the first Name',
				'class' : 'form-control',
			}),
				'lname' : forms.TextInput(attrs={
				'class' : 'form-control',
				'placeholder': 'Enter the lastName',
			}),
				'email' : forms.EmailInput(attrs={
				'class' : 'form-control',
				'placeholder': 'Enter the Email',
			}),
				'image' : forms.FileInput(attrs={
				'class' : 'form-control',
			}),
				'dob' : forms.DateInput(attrs={
				'class' : 'form-control',
				'placeholder': 'mm/dd/yyyy'
			}),
				'mob_number' : forms.TextInput(attrs={
				'class' : 'form-control',
				'placeholder': 'Enter your mobile number'	
			}),
				'adhar_number' : forms.TextInput(attrs={
				'class' : 'form-control',
				'placeholder': 'Enter your adhar number'	
			}),
				'qualification' : forms.TextInput(attrs={
				'class' : 'form-control', 
				'placeholder': 'Enter your highest qualification'
			}),
				'address' : forms.Textarea(attrs={
				'class' : 'form-control',
				'cols': 4,
				'placeholder': 'Enter the full addresss'
				
			}),
		}


		

	# fname = forms.CharField()
	# lname = forms.CharField()
	# email = forms.EmailField()
	# image = forms.ImageField()
	# dob = forms.DateField()
	# mob_number = forms.CharField()
	# adhar_number = forms.CharField()
	# qualification = forms.CharField()
	# address = forms.CharField(widget=forms.Textarea())
	
	
	
  
# #     
# #     
# 	# # ame = forms.CharField(widget=forms.TextInput(attrs={
# 	# lass':'form-control',
# 	# # d':'lastname',
# 	# laceholder':'Enter Your First Name'
# #   
# 	# #     ,max_length=100,required=True)
# #     
# 	#		 # ame = forms.CharField(widget=forms.TextInput(attrs={
# 	# lass':'form-control',
# 	# # d':'lastname',
# 	# laceemailr':'Enter Your Last Name'
# # 	
# 	#	 ,max_length=10, ,max_length=200,required=True)
# # 	'placeholder:'Upload Your Image'
# 	# # ail = forms.EmailField(widget=forms.EmailInput(attrs={
# 	# # lass':'form-control',
# 	# d':'email',
# 	#	 # laceholder':'Enter Your Email'
# 	#	 # ,required=True)
# # 	
# 	# age = forms.ImageFieltrs={# # lass':'form-control',
# 	# d':'image',

# 	#   b#  = forms.DateField(
#     #         widget=DatePickerInput(format='%m/%d/%Y')
#     #   )	}),required=True)
# 	# 	# 
# 	# dob# 

# 	# 	# b_number = forms.CharField(widget=forms.TextInput(attrs={
# 	#     # lass':'form-control',
# 	# d    ':'mobno',
# 	# 		 # laceholder':'Enter Your Mobile Number'
# 	# # ,max_length=10,required=True)

# 		# har_number = forms.CharField(widget=forms.TextInput(attrs={
# 	#     lass':'form-control',
# 	# d    ':'addhar',
# 	#     laceholder':'Enter Your Addhar Number'
# 	# ,max_length=10,required=True)

# 	# alification = forms.CharField(widget=forms.TextInput(attrs={
# 	#     lass':'form-control ',
# 	d    ':'qualification',
# 	#     laceholder':'Enter Your Qualification'
# 	# ,max_length=100,required=True)
	
# 	# dress = forms.CharField(widget=forms.Textarea(attrs={
# 		 # lass':'form-control ',
# 	 	d':'address',,'addres,s']

# 	class Meta():
# 		model = Reporter,''e
# 	shar