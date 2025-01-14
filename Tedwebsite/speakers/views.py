from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .forms import SpeakerModelForm
from django.contrib import messages


def speakers_home(request):
    return render(request, 'speakers/speakers.html')


def addSpeaker(request):
    if request.method == 'POST':
        form = SpeakerModelForm(request.POST)
        if form.is_valid():
            form.save()
    form = SpeakerModelForm()
    return render(request, 'speakers/form.html', {'form': form})


def nominate_yourself(request):
    return render(request, 'speakers/form2.html')


def unrestricted(request):
    return render(request, 'speakers/unrestricted.html')


def contact(request):
    return render(request, 'speakers/contact.html')


def speakerDesc1(request):
    return render(request, 'speakers/speaker21.html')


def speakerDesc2(request):
    return render(request, 'speakers/speaker22.html')


def speakerDesc3(request):
    return render(request, 'speakers/speaker23.html')


def speakerDesc4(request):
    return render(request, 'speakers/speaker24.html')


def speakerDesc5(request):
    return render(request, 'speakers/speaker25.html')


def speakerDesc6(request):
    return render(request, 'speakers/speaker26.html')


def speakerDesc7(request):
    return render(request, 'speakers/speaker27.html')


def speakerDesc8(request):
    return render(request, 'speakers/speaker11.html')


def speakerDesc9(request):
    return render(request, 'speakers/speaker12.html')


def speakerDesc10(request):
    return render(request, 'speakers/speaker13.html')


def speakerDesc11(request):
    return render(request, 'speakers/speaker14.html')


def speakerDesc12(request):
    return render(request, 'speakers/speaker15.html')


def speakerDesc13(request):
    return render(request, 'speakers/speaker16.html')


def speakerDesc14(request):
    return render(request, 'speakers/speaker31.html')


def speakerDesc15(request):
    return render(request, 'speakers/speaker32.html')


def speakerDesc16(request):
    return render(request, 'speakers/speaker33.html')


def speakerDesc17(request):
    return render(request, 'speakers/speaker34.html')


def speakerDesc18(request):
    return render(request, 'speakers/speaker35.html')


def speakerDesc19(request):
    return render(request, 'speakers/speaker36.html')


def speakerDesc20(request):
    return render(request, 'speakers/speaker37.html')


def speakerDesc21(request):
    return render(request, 'speakers/speaker38.html')


def speakerDesc22(request):
    return render(request, 'speakers/speaker39.html')
