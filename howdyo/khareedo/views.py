from django.http import HttpResponse

# Create your views here.
def howdy(request, name=None):
    return HttpResponse(f"Howdy, {name if name is not None else 'partner'}!")
