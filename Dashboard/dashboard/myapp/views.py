from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.db.models import Q


# Create your views here.
def home_view(request):
    users_count = UserProfile.objects.count()
    manders_count = Mander.objects.count()
    pending_requests_count = Request.objects.filter(status_request='Pendiente').count()
    in_process_requests_count = Request.objects.filter(status_request='Proceso').count()
    completed_requests_count = Request.objects.filter(status_request='Finalizado').count()
    available_manders_count = Mander.objects.filter(isactive_mander=True).count()

    context = {
        'users_count': users_count,
        'manders_count': manders_count,
        'pending_requests_count': pending_requests_count,
        'in_process_requests_count': in_process_requests_count,
        'completed_requests_count': completed_requests_count,
        'available_manders_count': available_manders_count,
    }


    return render(request, 'home.html', locals())


def users_view(request):
    search_query = request.GET.get('search', '')
    users_list = UserProfile.objects.filter(
        Q(name_userProfile__icontains=search_query) | Q(lastname_userProfile__icontains=search_query)
    )
    return render(request, 'users.html', locals())

def manders_view(request):
    search_query = request.GET.get('search', '')
    manders_list = UserProfile.objects.filter(
        Q(ismander_userProfile=True),
        Q(name_userProfile__icontains=search_query) | Q(lastname_userProfile__icontains=search_query)
    )
    return render(request, 'manders.html', {'manders_list': manders_list, 'search_query': search_query})


def edit_user_view(request, user_id):
    user_profile = get_object_or_404(UserProfile, id_userProfile=user_id)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('users_view')  # Redirige a la página de usuarios después de la edición
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'edit_user.html', locals())







