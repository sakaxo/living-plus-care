from django.urls import path
from main import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about-us/locations/", views.location, name="location"),
    path("contact-us/", views.contact_us, name="contact_us"),
    path("about-us/who-we-are/", views.who_we_are, name="who_we_are"),
    path("about-us/why-choose-living-plus-care/", views.why_choose_us, name="why_choose_us"),
    path("about-us/our-corporate-social-responsibility/", views.corporate_responsibility, name="corporate_responsibility"),
    path("services/domicialiary-care/", views.domicialiary_service, name="domicialiary_service"),
    path("services/supported-living/", views.supported_service, name="supported_service"),
    path("frequently-asked-questions/", views.faq, name="faq"),
]
