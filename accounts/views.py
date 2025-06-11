from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from actions.models import Action
from actions.utils import create_action

from .models import Profile, Contact
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm


User = get_user_model()


@login_required
def user_list(request: HttpRequest):
    users = User.objects.filter(is_active=True)
    return render(
        request,
        "accounts/user/list.html",
        {"section": "people", "users": users},
    )


@login_required
def user_detail(request: HttpRequest, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(
        request,
        "accounts/user/detail.html",
        {"section": "people", "user": user},
    )


def user_login(request: HttpRequest):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd["username"],
                password=cd["password"],
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated successfully")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")

    return render(request, "accounts/login.html", {"form": form})


@login_required
def dashboard(request: HttpRequest):
    actions = Action.objects.exclude(user=request.user)
    following_ids = request.user.following.values_list("id", flat=True)
    if following_ids:
        # If user is following others, retrieve only their actions
        actions = actions.filter(user_id__in=following_ids)
    actions = actions.select_related("user", "user__profile").prefetch_related(
        "target"
    )[:10]
    return render(
        request,
        "accounts/dashboard.html",
        {"section": "dashboard", "actions": actions},
    )


def register(request: HttpRequest):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # * This method handles password hashing before storing the password in the database
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            # Profile.objects.create(user=new_user)
            create_action(new_user, "has created an account")
            return render(
                request,
                "accounts/register_done.html",
                {
                    "new_user": new_user,
                },
            )
    else:
        user_form = UserRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {
            "user_form": user_form,
        },
    )


@login_required
def edit(request: HttpRequest):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES,
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request,
                "Profile updated successfully",
            )
        else:
            messages.error(
                request,
                "Error updating your profile",
            )
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(
        request,
        "accounts/edit.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
        },
    )


@require_POST
@login_required
def user_follow(request: HttpRequest):
    user_id = request.POST.get("id")
    action = request.POST.get("action")
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == "follow":
                Contact.objects.get_or_create(
                    user_from=request.user,
                    user_to=user,
                )
                create_action(request.user, "is following", user)
            else:
                Contact.objects.filter(
                    user_from=request.user,
                    user_to=user,
                ).delete()
            return JsonResponse({"status": "ok"})
        except User.DoesNotExist:
            pass
    return JsonResponse({"status": "error"})
