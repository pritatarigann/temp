from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_xml, show_json, show_json_by_id, show_xml_by_id
from wishlist.views import register 
from wishlist.views import login_user
from wishlist.views import logout_user
from wishlist.views import show_wishlist_ajax, submit_ajax

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='how_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('ajax/', show_wishlist_ajax, name='show_wishlist_ajax'),
    path('ajax/submit/', submit_ajax, name='submit_ajax'),
]