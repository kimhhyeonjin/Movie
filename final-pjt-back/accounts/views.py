from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.http import JsonResponse

# Create your views here.
@login_required
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return Response(context)

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                isFollow = False
            else:
                person.followers.add(user)
                isFollow = True
        follower_cnt = person.followers.count()
        context =  {
            'isFollow': isFollow,
            'follower-cnt' : follower_cnt
        }
    return JsonResponse(context)
