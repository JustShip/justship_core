from django.views import generic


class ErrorView(generic.ListView):
    def dispatch(self, request, *args, **kwargs):
        raise Exception('Error view')
