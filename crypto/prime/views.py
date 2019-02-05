from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Alert
from .serializers import AlertSerializer, UserSerializer
from .utils import form_cleaner


def index(request):
    template = loader.get_template('prime/index.html')
    context = {}
    if request.user.is_authenticated:
        alerts = Alert.objects.filter(user=request.user)
        context['alerts'] = alerts
    return HttpResponse(template.render(context, request))


# View for register new users
class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# View for deleting an alert via a browser
class AlertDelete(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'prime/alert_create.html'

    def get(self, request, pk):
        instance = get_object_or_404(Alert, pk=pk)
        instance.delete()
        return redirect('prime:index')


# View for creating an alert via a form
class AlertCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'prime/alert_create.html'

    def get(self, request):
        serializer = AlertSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = AlertSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        r = form_cleaner(request.data)
        instance = Alert(**r)
        instance.user = request.user
        instance.save()
        return redirect('prime:index')


# View for updating an alert via a form
class AlertUpdate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'prime/alert_update.html'

    def get(self, request, pk):
        profile = get_object_or_404(Alert, pk=pk)
        serializer = AlertSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        profile = get_object_or_404(Alert, pk=pk)
        serializer = AlertSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('prime:index')
