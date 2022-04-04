
from django.shortcuts import render
from django.views.generic import TemplateView 
from django.db.models import Avg,Count
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from apps.poll.models import Poll,SocialNetwork
from apps.poll.forms import PollForm
# Create your views here.





class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_average_age_range(self,social_network='Facebook'):
        data = {}
        try:
            result = Poll.objects.filter(favorite_sn__name=social_network).values('favorite_sn__name','age').annotate(total=Count('age')).order_by()
            for i in list(result):
                data[i['age']]=i['total']
            Keymax = max(data, key=data.get)
            ranges = ''
            for i in data.keys():
                maxValue = data[Keymax]
                if(data[i]==maxValue):
                    ranges+=i
                    ranges+=','
            return ranges[:-1]
        except Exception as e:
            print(str(e))
        return data

    def get_less_used_social_net(self):
        data = {}
        try:
            result = Poll.objects.values('favorite_sn__name').annotate(total=Count('favorite_sn')).order_by()
            for i in list(result):
                data[i['favorite_sn__name']]=i['total']
            Keymin = min(data, key=data.get)
            less_used = ''
            for i in data.keys():
                maxValue = data[Keymin]
                if(data[i]==maxValue):
                    less_used+=i
                    less_used+=','
            return less_used[:-1]
        except Exception as e:
            print(str(e))
        return data

    def get_favorite_social_net(self):
        data = {}
        try:
            data = {}
            result = (Poll.objects.values('favorite_sn__name').annotate(total=Count('favorite_sn')).order_by())
            for i in list(result):
                data[i['favorite_sn__name']]=i['total']
            Keymax = max(data, key=data.get)
            favorites = ''
            for i in data.keys():
                maxValue = data[Keymax]
                if(data[i]==maxValue):
                    favorites+=i
                    favorites+=','
            return favorites[:-1]
        except Exception as e:
            print(str(e))
        return data


    def get_time_avg(self):
        data = []
        try:
            data.append(round(float(Poll.objects.aggregate(Avg('time_avg_facebook'))['time_avg_facebook__avg']),2))
            data.append(round(float(Poll.objects.aggregate(Avg('time_avg_whatsapp'))['time_avg_whatsapp__avg']),2))
            data.append(round(float(Poll.objects.aggregate(Avg('time_avg_twitter'))['time_avg_twitter__avg']),2))
            data.append(round(float(Poll.objects.aggregate(Avg('time_avg_instagram'))['time_avg_instagram__avg']),2))
            data.append(round(float(Poll.objects.aggregate(Avg('time_avg_tiktok'))['time_avg_tiktok__avg']),2))
        except Exception as e:
            print(str(e))
        return data

    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if(action=='add'):
                p = Poll()
                p.email = request.POST['email']
                p.age = request.POST['age']
                p.gender = request.POST['gender']
                p.favorite_sn = SocialNetwork.objects.get(pk=request.POST['favorite_sn'])
                p.time_avg_facebook = request.POST['time_avg_facebook']
                p.time_avg_whatsapp = request.POST['time_avg_whatsapp']
                p.time_avg_twitter = request.POST['time_avg_twitter']
                p.time_avg_instagram = request.POST['time_avg_instagram']
                p.time_avg_tiktok = request.POST['time_avg_tiktok']
                p.save()
                messages.add_message(request, messages.SUCCESS, 'Se ha guardado con exito la encuesta')


            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PollForm()
        context['total'] = Poll.objects.all().count()
        context['favorites'] = self.get_favorite_social_net()
        context['less_used'] = self.get_less_used_social_net()
        context['data'] = self.get_time_avg()
        context['facebook_range'] = self.get_average_age_range('Facebook')
        context['whatsapp_range'] = self.get_average_age_range('Whatsapp')
        context['twitter_range'] = self.get_average_age_range('Twitter')
        context['instagram_range'] = self.get_average_age_range('Instagram')
        context['tiktok_range'] = self.get_average_age_range('Tiktok')
        context['other_range'] = self.get_average_age_range('Otra')
        context['title'] = 'Estadisticas de Redes Sociales'
        return context