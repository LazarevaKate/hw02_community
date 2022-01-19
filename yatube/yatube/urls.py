urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls)
]
