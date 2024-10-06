from django.shortcuts import render
from .models import *

# Create your views here.

def homeFun(request):
    return render(request, 'home.html')

def homeSecondFun(request):
    return render(request, 'home2.html')

def cvTemplateFun(request):
    if request.method == 'POST':
        # Retrieve form data and create or update CV
        full_name = request.POST.get('full_name')
        photo = request.FILES.get('photo')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        address = request.POST.get('address')
        social_media = request.POST.get('social_media')
        languages = request.POST.get('languages')
        skills = request.POST.get('skills')
        education = request.POST.get('education')
        experience = request.POST.get('experience')

        sendData = cvTemplateClass(
            fullName=full_name,
            photo=photo,
            contactNumber=contact,
            email=email,
            address=address,
            socialMediaLinks=social_media,
            languages=languages,
            skills=skills,
            education=education,
            experience=experience
        )
        sendData.save()

        # Render the template with the cv_id included in the context
        return render(request, 'cvTemplateShow.html', {
            'full_name': full_name,
            'photo': sendData.photo,
            'contact': contact,
            'email': email,
            'address': address,
            'social_media': social_media,
            'languages': languages,
            'skills': skills,
            'education': education,
            'experience': experience,
            'cv_id': sendData.id  # Ensure this is included
        })

    return render(request, 'cvTemplate.html')



# THIS IS DOWNLOAD

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# from .models import cvTemplateClass
from django.shortcuts import get_object_or_404

# Function to generate the PDF
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# View to download the CV as PDF
# def download_cv(request, cv_id):
#     try:
#         # Fetch the CV data from the database using the cv_id
#         cv_data = cvTemplateClass.objects.get(id=cv_id)

#         # Prepare context to render the CV as PDF
#         context = {
#             'full_name': cv_data.fullName,
#             'photo': cv_data.photo,
#             'contact': cv_data.contactNumber,
#             'email': cv_data.email,
#             'address': cv_data.address,
#             'social_media': cv_data.socialMediaLinks,
#             'languages': cv_data.languages,
#             'skills': cv_data.skills,
#             'education': cv_data.education,
#             'experience': cv_data.experience,
#         }
#         # Render and return the PDF file
#         return render_to_pdf('cvTemplateShow.html', context)
#     except cvTemplateClass.DoesNotExist:
#         return HttpResponse('CV not found', status=404)

def download_cv(request, cv_id):
    cv = get_object_or_404(cvTemplateClass, id=cv_id)

    # Example response for testing
    response = HttpResponse(f"CV for {cv.fullName} downloaded", content_type='text/plain')
    return response


