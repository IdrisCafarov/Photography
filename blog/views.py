from django.shortcuts import render, get_object_or_404,redirect
from blog.models import *
from .options import NUMBERTYPE
from .forms import BookForm, MessageForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.shortcuts import render_to_response
from django.template import RequestContext
# from django.shortcuts import render_to_response

# Create your views here.


def index_view(request):
    context = {}
    first_sliders = Index_First_Slider.objects.all()
    index_settings = Index_Settings.objects.all()
    services = Services.objects.all()
    images = Service_Images.objects.all().order_by('-created_date')
    offers = Offers.objects.all()
    categories = Work.objects.all()

    context["first_sliders"] = first_sliders
    context["index_settings"] = index_settings
    context['services'] = services
    context["images"] = images
    context["offers"] = offers
    context["categories"] = categories

    return render(request, "index.html", context)


def service_detail(request, slug):
    context = {}
    why = Why_Us_Detail.objects.all()
    service = get_object_or_404(Services, slug=slug)

    if request.method == 'POST':
        form = BookForm(request.POST)
        # print(form)
        if form.is_valid():
            form = form.save(commit=False)
            form.service = service.name
            form.save()
            
            messages.success(request, 'Sizin müraciətiniz uğurla göndərildi !')
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = BookForm()

    context['form'] = form

    context["service"] = service
    context["why"] = why
    return render(request, 'services-details.html', context)


def portfolio(request):
    context = {}
    categories = Category.objects.all()
    works = Work.objects.all()
    context['categories'] = categories
    context['works'] = works

    return render(request,"portfolio.html",context)


def portfolio_details(request,slug):
    context = {}
    work = get_object_or_404(Work,slug=slug)
    images = Images.objects.filter(work_id=work.id)

    page = request.GET.get('page')
    paginator = Paginator(images, 12)
    
    try:
        images=paginator.page(page)
    
    except PageNotAnInteger:
        images= paginator.page(1)
    except EmptyPage:
    
        images=paginator.page(paginator.num_pages)


    if request.method == 'POST':
        form = BookForm(request.POST)
        # print(form)
        if form.is_valid():
            form = form.save(commit=False)
            # form.service = 
            form.save()
            messages.success(request, 'Sizin müraciətiniz uğurla göndərildi !')
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = BookForm()

    context['form'] = form

    context['images'] = images

    context["work"] = work

    return render(request, "portfolio-details.html",context)



def about(request):
    context = {}
    about = About.objects.all()
    services = Services.objects.all()
    members = Member.objects.all()

    context['about'] = about
    context['services'] = services
    context['members'] = members


    return render(request,"about.html",context)


def contact(request):
    context = {}

    if request.method == 'POST':
        form = MessageForm(request.POST)
        # print(form)
        if form.is_valid():
            form = form.save(commit=False)
            # form.service =
            form.save()
            messages.success(request, 'Sizin müraciətiniz uğurla göndərildi !')
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = MessageForm()

    context['form'] = form


    return render(request,"contact-us.html",context)






def handler404(request, exception):
    return render(request, "error.html", {})


def handler500(request, exception=None):
    return render(request, "error.html", {})
