from django.urls import path
from app1.views import RegisterAPIView,LoginAPIView,CreateOfficeStaffView,LibraryReviewView,CreateLibrarianView,StudentView,LibraryHistoryAPIView,FeesHistoryAPIView

urlpatterns = [
    
        path('register/', RegisterAPIView.as_view(), name='register'),
        path('login/', LoginAPIView.as_view(), name='login'),
        path('create-office-staff/', CreateOfficeStaffView.as_view(), name='create-office-staff'),
        path('create-librarian/', CreateLibrarianView.as_view(), name='create-librarian'),
        path('create-student/', StudentView.as_view(), name='create-student'),
        path('library-history/', LibraryHistoryAPIView.as_view(), name='library-history'),
        path('fees-history/', FeesHistoryAPIView.as_view(), name='fees-history'),
        path('LibraryReview/', LibraryReviewView.as_view(), name='LibraryReviewView'),

     
]
