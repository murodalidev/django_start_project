from django.urls import path, include
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

app_name = 'accounts'

urlpatterns = [
    # api based path
    path('api/', include('apps.accounts.api.urls', namespace='api')),

]

# django build-in paths

# accounts/login/ [name='login']    # login
# accounts/logout/ [name='logout']  # logout


# PasswordChangeView()
# accounts/password_change/ [name='password_change']    # change
# PasswordChangeDoneView()
# accounts/password_change/done/ [name='password_change_done']  # change done


# PasswordResetView()
# accounts/password_reset/ [name='password_reset']

# PasswordResetDoneView()
# accounts/password_reset/done/ [name='password_reset_done']

# PasswordResetConfirmView()
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']

# PasswordResetCompleteView()
# accounts/reset/done/ [name='password_reset_complete']
