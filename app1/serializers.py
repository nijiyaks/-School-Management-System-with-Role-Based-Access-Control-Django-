from rest_framework import serializers
from .models import User, OfficeStaff, Librarian,Student,LibraryHistory, FeesHistory ,LibraryReview
from django.utils import timezone
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

# register serializer
class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['name', 'email', 'phone_number', 'country_code', 'role', 'password', 'joining_date']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        role = validated_data.pop('role', 'staff')  # Default to 'staff'
        user = User.objects.create_user(**validated_data, role=role)

        # Additional logic for specific roles
        if role == 'staff':
            joining_date = validated_data.pop('joining_date', timezone.now().date())  # Use default current date if not provided
            OfficeStaff.objects.create(user=user, joining_date=joining_date)  # Add joining_date here
        elif role == 'librarian':
            joining_date = validated_data.pop('joining_date', timezone.now().date())  # Use default current date if not provided
            Librarian.objects.create(user=user, joining_date=joining_date)  # Add joining_date here
        
        return user

# login for admin
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    phone_number = serializers.CharField(max_length=15, required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        phone_number = data.get('phone_number')
        password = data.get('password')

        # Check if either email or phone number is provided
        if not email and not phone_number:
            raise ValidationError("Email or phone number must be provided.")

        # Authenticate the user based on email or phone number
        user = None
        if email:
            user = authenticate(email=email, password=password)
        elif phone_number:
            user = authenticate(phone_number=phone_number, password=password)

        if not user:
            raise ValidationError("Invalid credentials.")

        if user.role != 'admin':
            raise ValidationError("User is not an admin.")

        return user

# user serializer for creating user lb,os by admin
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'phone_number', 'country_code', 'role', 'joining_date', 'password']

class OfficeStaffSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = OfficeStaff
        fields = ['user', 'department', 'position', 'joining_date']

    def create(self, validated_data):
        # Extract user data from validated data
        user_data = validated_data.pop('user')

        # Set the role for user as 'staff'
        user_data['role'] = 'staff'

        # Handle password hashing if provided
        password = user_data.get('password')
        if password:
            user_data['password'] = make_password(password)  # Hash the password

        # Create and save the User instance
        user = User.objects.create(**user_data)

        # Extract the office staff data (department, position, joining_date) from validated_data
        department = validated_data.get('department')
        position = validated_data.get('position')
        joining_date = validated_data.get('joining_date')

        # Create and save the OfficeStaff instance, using the extracted data
        office_staff = OfficeStaff.objects.create(user=user, department=department, position=position, joining_date=joining_date)

        return office_staff


class LibrarianSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Librarian
        fields = ['user', 'library_section', 'shifts','books_managed','joining_date']

    def create(self, validated_data):
        # Extract user data from validated data
        user_data = validated_data.pop('user')

        # Set the role for user as 'staff'
        user_data['role'] = 'librarian'

        # Handle password hashing if provided
        password = user_data.get('password')
        if password:
            user_data['password'] = make_password(password)  # Hash the password

        # Create and save the User instance
        user = User.objects.create(**user_data)

        library_section = validated_data.get('library_section')
        shifts = validated_data.get('shifts')
        books_managed = validated_data.get('books_managed')
        joining_date = validated_data.get('joining_date')

        # Create and save the OfficeStaff instance, using the extracted data
        librarian = Librarian.objects.create(user=user, library_section=library_section, shifts=shifts, books_managed=books_managed,joining_date=joining_date)

        return librarian
    
#  student serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

# library history serializer
class LibraryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryHistory
        fields = '__all__'

#  fees history serializer
class FeesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesHistory
        fields = '__all__'
        
#  library review serializer
class LibraryReviewSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())

    class Meta:
        model = LibraryReview
        fields = ['id', 'student', 'book', 'rating', 'comment', 'created_at']

   