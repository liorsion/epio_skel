from django.conf.urls.defaults import patterns, include, url

# Uncomment the next line to enable the robots.txt support:
#from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'epio_skel.views.home', name='home'),
    # url(r'^epio_skel/', include('epio_skel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    # Uncomment for django support of robots.txt
    #(r'^robots\.txt$', direct_to_template,{'template': 'robots.txt', 'mimetype': 'text/plain'}),
)
