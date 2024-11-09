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
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        experience = request.POST.get("experience")
        education = request.POST.get("education")
        skills = request.POST.get("skills")
        linkedin = request.POST.get("linkedin")
        leetcode = request.POST.get("leetcode")
        codechef = request.POST.get("codechef")
        codeforces = request.POST.get("codeforces")
        social_profiles = {
            "linkedin": linkedin if linkedin else "LinkedIn not found",
            "leetcode": leetcode if leetcode else "Leetcode not found",
            "codechef": codechef if codechef else "CodeChef not found",
            "codeforces": codeforces if codeforces else "CodeForces not found",
        }

        varForm = Form(
            name=name,
            email=email,
            phone=phone,
            education=education,
            experience=experience,
            skills=skills,
            social_profiles=social_profiles,
        )
        varForm.save()

        context = {
            "name": name,
            "email": email,
            "phone": phone,
            "experience": experience,
            "education": education,
            "skills": skills,
            "linkedin": linkedin,
            "leetcode": leetcode,
            "codechef": codechef,
            "codeforces": codeforces,
        }
        return render(request, "dashboard.html", context)

    return render(request, "form.html")


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
    return render(request, "contact.html")


def file(request):
    if request.method == "POST":
        file = request.FILES["file"]
        File.objects.create(file=file)

        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Extracting the name
        name = text.split("\n")[0]

        # Extracting the email
        email_match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
        email = email_match.group(0) if email_match else "Email not found"

        # Extracting the phone number
        phone_match = re.search(
            r"\(?\+?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}", text
        )
        phone = phone_match.group(0) if phone_match else "Phone number not found"

        # Extracting LinkedIn
        linkedin_match = re.search(r"(https?://[^\s]+linkedin\.com[^\s]+)", text)
        linkedin = linkedin_match.group(0) if linkedin_match else "LinkedIn not found"

        # Extracting Leetcode
        leetcode_match = re.search(r"(https?://[^\s]+leetcode\.com[^\s]+)", text)
        leetcode = leetcode_match.group(0) if leetcode_match else "Leetcode not found"

        # Extracting CodeChef
        codechef_match = re.search(r"(https?://[^\s]+codechef\.com[^\s]+)", text)
        codechef = codechef_match.group(0) if codechef_match else "CodeChef not found"

        # Extracting CodeForces
        codeforces_match = re.search(r"(https?://[^\s]+codeforces\.com[^\s]+)", text)
        codeforces = (
            codeforces_match.group(0) if codeforces_match else "CodeForces not found"
        )

        # Extracting education
        education = extract_section(
            text,
            "Education",
            ["Experience", "Projects", "Technical Skills", "Achievements"],
        )

        # Extracting work experience
        work_experience = extract_section(
            text,
            "Experience",
            ["Education", "Projects", "Technical Skills", "Achievements"],
        )

        # Extracting skills
        skills = extract_section(
            text,
            "Technical Skills",
            ["Education", "Experience", "Projects", "Achievements"],
        )

        # Split skills and education into lists
        skills_list = [skill.strip() for skill in skills.split("\n") if skill.strip()]
        education_list = [edu.strip() for edu in education.split("\n") if edu.strip()]
        print(f'leetcode: {leetcode}')
        print(f'codechef: {codechef}')
        print(f'codeforces: {codeforces}')
        print(f'linkedin: {linkedin}')
        context = {
            "name": name,
            "email": email,
            "phone": phone,
            "work_experience": work_experience,
            "education": education_list,
            "skills": skills_list,
            "linkedin": linkedin,
            "leetcode": leetcode,
            "codechef": codechef,
            "codeforces": codeforces,
        }
        return render(request, "file.html", context)

    return render(request, "file.html")


def extract_section(text, start_keyword, end_keywords):
    start_index = text.find(start_keyword)
    if start_index == -1:
        return f"{start_keyword} not found"

    end_index = len(text)
    for end_keyword in end_keywords:
        temp_index = text.find(end_keyword, start_index)
        if temp_index != -1 and temp_index < end_index:
            end_index = temp_index

    return text[start_index:end_index].strip()
