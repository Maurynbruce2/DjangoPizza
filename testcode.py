import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import *
from pizzas.views import *
'''
p = Pizza.objects.all()
print(p)

for pizzas in p: 
    print(pizzas.pizza_name)
'''
p = Pizza.objects.get(id=1)
print(p)

c = Comment.objects.all()
print(c)

m = Comment.objects.all()
print(m)


