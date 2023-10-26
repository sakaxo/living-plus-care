from django.urls import path
from main import views

urlpatterns = [
    path("", views.home, name="home"),
    path("our-location/", views.location, name="location"),
    path("contact-us/", views.contact_us, name="contact_us"),
    path("who-we-are/", views.who_we_are, name="who_we_are"),
    path("why-choose-living-plus-care/", views.why_choose_us, name="why_choose_us"),
    path("Our corporate social responsibility/", views.corporate_responsibility, name="corporate_responsibility"),
    path("Domicialiary care service/", views.domicialiary_service, name="domicialiary_service"),
    path("Supported living service/", views.supported_service, name="supported_service"),
    path("Location/", views.location, name="location"),
]
