# from django.contrib.auth.views import (
#     LoginView,
#     LogoutView,
#     PasswordChangeView,
#     PasswordChangeDoneView,
#     PasswordResetView,
#     PasswordResetDoneView,
#     PasswordResetConfirmView,
#     PasswordResetCompleteView,
# )
from django.urls import path

from .views import dashboard, register, edit, user_list, user_detail, user_follow


urlpatterns = [
    # * My view
    # path("login/", user_login, name="login"),
    # *
    # path("login/", LoginView.as_view(), name="login"),
    # path("logout/", LogoutView.as_view(), name="logout"),
    # path(
    #     "password-change/",
    #     PasswordChangeView.as_view(),
    #     name="password_change",
    # ),
    # path(
    #     "password-change-done/",
    #     PasswordChangeDoneView.as_view(),
    #     name="password_change_done",
    # ),
    # path(
    #     "password-reset/",
    #     PasswordResetView.as_view(),
    #     name="password_reset",
    # ),
    # path(
    #     "password-reset/done",
    #     PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "password-reset/<uidb64>/<token>/",
    #     PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "password-reset/complete/",
    #     PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
    path("", dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path("users/", user_list, name="user_list"),
    path("users/follow/", user_follow, name="user_follow"),
    path("users/<str:username>/", user_detail, name="user_detail"),
    path("edit/", edit, name="edit"),
]
