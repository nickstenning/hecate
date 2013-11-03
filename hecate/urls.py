from django.conf.urls import patterns, include, url

from apps.accounts.forms import AuthenticationForm, PasswordResetForm

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'apps.homepage.views.homepage', name='homepage'),

    # Authentication, account management, etc.
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'accounts/login.html',
         'authentication_form': AuthenticationForm},
        name='login'),
    url(r'^logout/$', 'apps.accounts.views.logout', name='logout'),

    url(r'^change-password/$',
        'apps.accounts.views.password_change',
        name='password_change'),
    url(r'^change-password/done/$',
        'django.contrib.auth.views.password_change_done',
        name='password_change_done'),

    url(r'^reset-password/$',
        'django.contrib.auth.views.password_reset',
        {'password_reset_form': PasswordResetForm,
         'email_template_name': 'emails/accounts/password_reset.html'},
        name='password_reset'),
    url(r'^reset-password/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'apps.accounts.views.password_reset_confirm',
        {'post_reset_redirect': '/'},
        name='password_reset_confirm'),
    url(r'^reset-password/done/$',
        'django.contrib.auth.views.password_reset_done',
        name='password_reset_done'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),)
