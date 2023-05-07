import PyPDF2
import re

from django.shortcuts import render ,HttpResponse,redirect
from datetime import datetime
from Home.models import Form,File
# Create your views here.

def index(request):
    context = {
      'variable': 'THIS IS VARIABLE PLACEHOLDER'
    }
    return render(request,'index.html',context)


def about(request):
  return HttpResponse("This is about")


def form(request):
  if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      experience = request.POST.get('experience')
      education = request.POST.get('education')
      skills = request.POST.get('skills')
      varForm = Form(name = name, email= email, phone = phone , education = education, experience=experience,
                  skills=skills)
      varForm.save()
      context = {
        'name' : name,
        'email': email,
        'phone':phone,
        'experience':experience,
        'education':education,
        'skills':skills
      }
      return render(request,'dashboard.html',context)

  return render(request,'form.html')

def dashboard(request):

  return render(request,'dashboard.html')

#
# def saveForm(request):
#   if request.method == "POST":
#       n = request.POST.get('name')
#       email = request.POST.get('email')
#       phone = request.POST.get('phone')
#       experience = request.POST.get('experience')
#       education = request.POST.get('education')
#       skills = request.POST.get('skills')
#       varForm = saveForm(name = n, email= email, phone = phone , education = education, experience=experience,
#                   skills=skills, date=datetime.today())
#       varForm.save()
#   return render(request,'form.html')





def contact(request):
    return render(request,'contact.html')


def file(request):
  if request.method=="POST":
    file = request.FILES['file']
    File.objects.create(file=file)
    # Open the pdf file containing the resume
    #with open('file', 'rb') as resume_pdf:
      # Create a pdf reader object
    pdf_reader = PyPDF2.PdfReader(file)
      # Extract text from all pages in the pdf
    text = ""
    for page in pdf_reader.pages:
        # Extract the text from the page
        text += page.extract_text()

    # Parse the text to extract specific pieces of information
    # such as the candidate's name, contact information, education, and work experience

    # Extracting the name
    name = text.split('\n')[0]

    # Extracting the email
    email = re.search("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text).group(0)

    # Extracting the phone number
    phone = re.search(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text)
    if phone:
      phone = phone.group(0)
    else:
      phone = "Phone number not found"

    education_split = text.split("Education")
    if len(education_split) > 1:
      education = education_split[1].split("Experience")[0]
    else:
      education = "Education not found"

    work_experience_split = text.split("Experience")
    if len(work_experience_split) > 1:
      work_experience = work_experience_split[1].split("Skills")[0]
    else:
      work_experience = "Work Experience not found"

    skills_split = text.split("Skills")
    if len(skills_split) > 1:
      skills = skills_split[1]
    else:
      skills = "Work Experience not found"

    context = {
      'name': name,
      'email': email,
      'phone': phone,
      'work_experience': work_experience,
      'education': education,
      'skills': skills
    }
    return render(request,'file.html',context)




  return render(request,'file.html')

