from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

# Create your views here.
@api_view(['GET'])
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return Response(context)

@api_view(['POST'])
# @method_decorator(csrf_exempt, name='dispatch')
def follow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    user = request.user

    if person != user:
        if person.followings.filter(pk=user.pk).exists():
            person.followings.remove(user)
            isFollow = False
        else:
            person.followings.add(user)
            isFollow = True
    followings_cnt = person.followings.count()
    context =  {
        'isFollow': isFollow,
        'followings_cnt' : followings_cnt,
    }
    return Response(context)
