from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail


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

def faq(request):
	return render(request, 'main/faqs.html')

def about(request):
	return render(request, 'main/about-us.html')

def temporary_staffing(request):
	return render(request, 'main/temporary-staffing.html')


def send_form_data(request):
	if request.method == 'POST':
		data = request.POST
		fname = data.get("firstName")
		lname = data.get("lastName")
		phone = data.get("phoneNumber")
		email = data.get("email")
		msg = data.get("message")

		try:
			subject = f"New messsage from {fname} {lname}."
			msg_from = email
			msg_to = "info@livingpluscare.co.uk"
			send_mail(subject, msg, msg_from, [msg_to], fail_silently=False,)
			messages.success(request, 'Message sent successfully, LPC team will reach out to you soon.')
		
		except:
			messages.error(request, 'An error occurred, try sending your message again!')
		
		return redirect('contact_us')


	return render(request, 'main/contact-us.html')
