from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View

from newapp.models import Category, Post
from .models import Appointment


class AppointView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'test_test.html')

    def post(self, request):
        pole_test = request.POST['test']
        if pole_test:
            pole_test = pole_test
        else:
            pole_test = 1

        pole_test2 = request.POST['test2']
        if pole_test2:
            pole_test2 = pole_test2

        pole_spisok1 = Category.objects.get(pk=pole_test)

        pole_spisok2 = Category.objects.get(pk=pole_test).subscribers.all()
        for qwe in pole_spisok2:
            pass

        for category in Category.objects.all():
            news_from_each_category = []

            for news in Post.objects.filter(category_id=category.id,
                                           dateCreation__week=datetime.now().isocalendar()[1] - 1).values('pk', 'title',
                                                                                                        'dateCreation'):
                new = (f'{news.get("title")}, {news.get("dateCreation")}, http://127.0.0.1:8000/news/{news.get("pk")}')
                news_from_each_category.append(new)
            print("Письма отправлены подписчикам категории:", category.id, category.name)
            for qaz in news_from_each_category:
                print(qaz)
            qwe = category.subscribers.all()
            for wsx in qwe:
                print('Новости отправлены на', wsx.email)






        return render(request, 'test_test.html', {
            'pole_test_html': pole_test,
            'pole_test_html2': pole_test2,
            "pole_spisok_html1": pole_spisok1,
            "pole_spisok_html2": pole_spisok2,
        })






class AppointmentView(View):
    def get(self, request, ):
        return render(request, 'make_appointment.html', {})

    def post(self, request, ):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        return redirect('make_appointment')  # (1)
