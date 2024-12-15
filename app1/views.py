from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,LoginSerializer,OfficeStaffSerializer,LibraryReviewSerializer,OfficeStaffSerializer,LibrarianSerializer,StudentSerializer, LibraryHistorySerializer, FeesHistorySerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser  # Import built-in permission
from .models import OfficeStaff,Librarian,Student,LibraryHistory,FeesHistory
from app1.permission import IsAdminOrStaff


# Register function
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Create the user
            return Response(
                {
                    "message": "User registered successfully.",
                    "user_id": user.id,
                    "email": user.email,
                    "role": user.role,
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  Login for admin
class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data  # User object after successful validation

            # Authenticate user and log in if credentials are valid
            login(request, user)  

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response(
                {
                    "message": "Login successful.",
                    "user_id": user.id,
                    "email": user.email,
                    "role": user.role,
                    "access_token": access_token,
                    "refresh_token": str(refresh),
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# crud operation for office staff

class CreateOfficeStaffView(APIView):
    permission_classes = [IsAdminUser]  

    def get(self,request):
        office_staff=OfficeStaff.objects.all()
        serializer=OfficeStaffSerializer(office_staff,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        # Ensure the user making the request is a superuser
        if not request.user.is_superuser:
            return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)

        office_staff_serializer = OfficeStaffSerializer(data=request.data)

        if office_staff_serializer.is_valid():
            office_staff = office_staff_serializer.save()  # Save the OfficeStaff and User
            return Response(office_staff_serializer.data, status=status.HTTP_201_CREATED)
        else:
        
            return Response(office_staff_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def patch(self, request):
        # Get the custom_id from the request body
        custom_id = request.data.get('custom_id')

        if not custom_id:
            return Response({"detail": "custom_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            office_staff = OfficeStaff.objects.get(custom_id=custom_id)
        except OfficeStaff.DoesNotExist:
            return Response({"detail": "Office staff not found."}, status=status.HTTP_404_NOT_FOUND)

        office_staff_serializer = OfficeStaffSerializer(office_staff, data=request.data, partial=True)  

        if office_staff_serializer.is_valid():
            office_staff_serializer.save()  
            return Response(office_staff_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(office_staff_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        # Get the custom_id from the request body
        custom_id = request.data.get('custom_id')

        if not custom_id:
            return Response({"detail": "custom_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            office_staff = OfficeStaff.objects.get(custom_id=custom_id)
        except OfficeStaff.DoesNotExist:
            return Response({"detail": "Office staff not found."}, status=status.HTTP_404_NOT_FOUND)

        office_staff.delete()  
        return Response({"detail": "Office staff deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# crud Librarian

class CreateLibrarianView(APIView):
    permission_classes=[IsAdminUser]

    def get(self,request):
        librarian=Librarian.objects.all()
        serializer=LibrarianSerializer(librarian,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        if not request.user.is_superuser:
            return Response({"detail":" you do not have permission to perform this action"},status=status.HTTP_403_FORBIDDEN)
        librarian_serializer= LibrarianSerializer(data=request.data)
        if librarian_serializer.is_valid():
            librarian = librarian_serializer.save()
            return Response(librarian_serializer.data,status=status.HTTP_201_CREATED) 
        else:
            return Response(librarian_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request):
        # Get the custom_id from the request body
        custom_id = request.data.get('custom_id')

        if not custom_id:
            return Response({"detail": "custom_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            librarian = Librarian.objects.get(custom_id=custom_id)
        except Librarian.DoesNotExist:
            return Response({"detail": "Librarian not found."}, status=status.HTTP_404_NOT_FOUND)

        librarian_serializer = LibrarianSerializer(librarian, data=request.data, partial=True)  

        if librarian_serializer.is_valid():
            librarian_serializer.save()  
            return Response(librarian_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(librarian_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        # Get the custom_id from the request body
        custom_id = request.data.get('custom_id')

        if not custom_id:
            return Response({"detail": "custom_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            librarian = Librarian.objects.get(custom_id=custom_id)
        except Librarian.DoesNotExist:
            return Response({"detail": " Librarian not found."}, status=status.HTTP_404_NOT_FOUND)

        librarian.delete()  
        return Response({"detail": "Librarian deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


# student crud

class StudentView(APIView):
    permission_classes = [IsAdminUser]  

    def post(self, request):
        student_serializer = StudentSerializer(data=request.data)
        if student_serializer.is_valid():
            student = student_serializer.save()  
            return Response(student_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            # Extract the ID from the request body
            student_id = request.data.get("id")
            student = Student.objects.get(id=student_id)

            serializer = StudentSerializer(student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        try:
            # Extract the ID from the request body
            student_id = request.data.get("id")
            student = Student.objects.get(id=student_id)

            student.delete()
            return Response({"message": "Student deleted successfully."}, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
        

# crud library history 

class LibraryHistoryAPIView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = LibraryHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        library_id = request.data.get("id")
        try:
            library_history = LibraryHistory.objects.get(id=library_id)
            serializer = LibraryHistorySerializer(library_history, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except LibraryHistory.DoesNotExist:
            return Response({"error": "LibraryHistory record not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        library_id = request.data.get("id")
        try:
            library_history = LibraryHistory.objects.get(id=library_id)
            library_history.delete()
            return Response({"message": "LibraryHistory record deleted successfully."}, status=status.HTTP_200_OK)
        except LibraryHistory.DoesNotExist:
            return Response({"error": "LibraryHistory record not found."}, status=status.HTTP_404_NOT_FOUND)

# crud fees history

class FeesHistoryAPIView(APIView):
    permission_classes = [IsAdminOrStaff]
    def get(self,request):
        fees_history=FeesHistory.objects.all()
        serializer=FeesHistorySerializer(fees_history,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):       
        serializer = FeesHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):       
        fee_id = request.data.get("id")
        try:
            fee_history = FeesHistory.objects.get(id=fee_id)
            serializer = FeesHistorySerializer(fee_history, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except FeesHistory.DoesNotExist:
            return Response({"error": "FeesHistory record not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):        
        fee_id = request.data.get("id")
        try:
            fee_history = FeesHistory.objects.get(id=fee_id)
            fee_history.delete()
            return Response({"message": "FeesHistory record deleted successfully."}, status=status.HTTP_200_OK)
        except FeesHistory.DoesNotExist:
            return Response({"error": "FeesHistory record not found."}, status=status.HTTP_404_NOT_FOUND)
        
#  create library review 
class LibraryReviewView(APIView):
    permission_classes = [IsAdminOrStaff]  

    def post(self, request):
        serializer = LibraryReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
