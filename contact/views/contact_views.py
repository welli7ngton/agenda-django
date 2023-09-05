from django.shortcuts import render
from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[0:10]

    # consulta sql do comanto acima
    # print(contacts.query)

    context = {
        'contacts': contacts,
    }
    return render(
        request,
        'contact/index.html',
        context,
    )
