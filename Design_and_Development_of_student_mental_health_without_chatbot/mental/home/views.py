from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.core.exceptions import ValidationError
import numpy as np
import joblib
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse

# Load your model
model = joblib.load('static/Student_Mental_Health_Predicator')

# Create a mapping for the predicted values
pred_mapping = {
    1: "Healthy",
    2: "Moderate Affected",
    3: "Severely affected"
}

# Create your views here.

def index(request):
    return render(request,'index.html')



def about(request):
    return render(request,'about.html')
def prediction(request):
    output = None 

    if request.method == 'POST':
        try:
            # Fetching form values safely and converting them to the required data types
            gender = int(request.POST.get('gender', 0))  # Gender encoded as 0 or 1
            education_level = int(request.POST.get('education_level', 0))  # Education level
            depressed = int(request.POST.get('depressed', 0))  # Feeling depressed
            interest = int(request.POST.get('interest', 0))  # Little interest or pleasure in doing things
            sleep = int(request.POST.get('sleep', 0))  # Are you having proper sleep (min 6hrs)
            energy = int(request.POST.get('energy', 0))  # Feeling tired or having little energy
            meal = int(request.POST.get('meal', 0))  # Taking proper meals or not
            failure = int(request.POST.get('failure', 0))  # Feeling of failure
            concentration = int(request.POST.get('concentration', 0))  # Trouble concentrating
            restless = int(request.POST.get('restless', 0))  # Restless or slowed movements
            self_harm = int(request.POST.get('self_harm', 0))  # Thoughts of harming yourself
            job = int(request.POST.get('job', 0))  # Part-time/full-time job
            family = int(request.POST.get('family', 0))  # Living with family
            study_hours = int(request.POST.get('study_hours', 0))  # Hours spent studying each day
            gadgets = int(request.POST.get('gadgets', 0))  # Hours spent on electronic gadgets
            social_media = int(request.POST.get('social_media', 0))  # Hours spent on social media
            exercise = int(request.POST.get('exercise', 0))  # Weekly physical activity hours
            substance = int(request.POST.get('substance', 0))  # Consumption of substances (alcohol, tobacco, drugs)
            percentage = float(request.POST.get('percentage', 0.0))  # Last year percentage (decimal number)

            
            input_data = np.array([[gender, education_level, depressed, interest, sleep, energy, meal, failure,
                                   concentration, restless, self_harm, job, family, study_hours, gadgets, 
                                   social_media, exercise, substance, percentage]])

            
            pred = model.predict(input_data)

            
            decoded_pred = pred_mapping.get(pred[0], "Unknown")

           
            output = f"Prediction: {decoded_pred}"

        except ValueError as e:
            
            output = f"Error: {str(e)}"

    
    return render(request, 'prediction.html', {'output': output})
def contact(request):
    return render(request,'contact.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use Django's login function
            return redirect('home')  # Redirect to home page or any desired page
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')
    

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email_or_phone')  # Adjusted field name to match the form
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'signup.html')

        # Check if username is alphanumeric and not purely numeric
        if not username.isalnum() or username.isnumeric():
            messages.error(request, "Username must contain both letters and numbers, and it can't be purely numeric.")
            return render(request, 'signup.html')

        # Create the user and set additional fields
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name  # Set first name
            user.last_name = last_name  # Set last name
            user.save()

            messages.success(request, "Account created successfully.")
            return redirect('login')  # Redirect to login page after successful signup
        except ValidationError as e:
            messages.error(request, str(e))
            return render(request, 'signup.html')

    return render(request, 'signup.html')




def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('login')  # Redirect to login if not authenticated
