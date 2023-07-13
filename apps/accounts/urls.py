from django.urls import path, include

app_name = 'accounts'

urlpatterns = [
    # api based path
    path('api/', include('apps.accounts.api.urls', namespace='api')),

]

# django build-in paths

# accounts/login/ [name='login']    # login
# accounts/logout/ [name='logout']  # logout


# accounts/password_change/ [name='password_change']    # change
# accounts/password_change/done/ [name='password_change_done']  # change done


# submit email form -> PasswordResetView()
# accounts/password_reset/ [name='password_reset']

# email sent success message -> PasswordResetDoneView()
# accounts/password_reset/done/ [name='password_reset_done']

# link to password rest form in email - > PasswordResetConfirmView()
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']

# password successfully changed message -> PasswordResetCompleteView()
# accounts/reset/done/ [name='password_reset_complete']
