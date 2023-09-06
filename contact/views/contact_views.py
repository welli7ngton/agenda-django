from django.shortcuts import render, get_object_or_404
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


def contact(request, contact_id):

    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )

    return render(
        request,
        'contact/contact.html',
        context={'contact': single_contact},
    )
