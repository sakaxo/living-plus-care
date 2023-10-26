from django.shortcuts import render

def home(request):
	return render(request, 'main/index.html')


def location(request):
	return render(request, 'main/location.html')


def contact_us(request):
	return render(request, 'main/contact-us.html')

def who_we_are(request):
	return render(request, 'main/who-we-are.html')

def why_choose_us(request):
	return render(request, 'main/why-choose-us.html')

def corporate_responsibility(request):
	return render(request, 'main/our-corporate-social-responsibility.html')

def domicialiary_service(request):
	return render(request, 'main/domiciliary-care-service.html')

def supported_service(request):
	return render(request, 'main/supported-living-service.html')

# def corporate_responsibility(request):
# 	return render(request, 'main/index.html')

# def corporate_responsibility(request):
# 	return render(request, 'main/index.html')