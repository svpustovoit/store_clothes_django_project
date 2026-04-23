"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include

from main import views

app_name = 'main'

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name='about'),
    path("delivery_payment/", views.delivery_payment, name="delivery_payment"),
    path("contact_information/", views.contact_information, name="contact_information"),
    path("catalog/", include("goods.urls", namespace="catalog")),
]
