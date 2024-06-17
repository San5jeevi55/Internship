from django.shortcuts import render
from firebase_admin import firestore
from django.shortcuts import render,redirect
from django.urls import reverse
from firebase_admin import db,auth


student_id=205002015
faculty_id=1

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        global student_id
        student_id=email.split("@")[0][-7:]
        print(student_id) 
        sync_data_with_sheets()
        if email=="sanjeevi2210539@ssn.edu.in" and password=="12":
            return redirect(reverse('student'), {"id": email.split("@")[0][-7:]})
        
    return render(request, 'login.html')


def calender(request):
    return render(request,"calender.html")
from django.db import connection


from .models import *

from django.shortcuts import render, redirect
from django.db import connection
from .models import InternshipResponse
from django.utils.dateparse import parse_date

def student(request):

    if request.method == 'POST':
        if "form" in request.POST:
            org_name = request.POST.get('organisation_name')
            org_address = request.POST.get('organisation_address_website')
            nature_of_work = request.POST.get('nature_of_work')
            repr_name = request.POST.get('repr_name')
            repr_designation = request.POST.get('repr_designation')
            repr_email_id = request.POST.get('repr_email_id')
            repr_mobile_no = request.POST.get('repr_mobile_no')
            start_date = request.POST.get('start_date')
            completion_date = request.POST.get('completion_date')
            duration = request.POST.get('duration')
            internship_mode = request.POST.get('mode_of_internship')
            stipend = request.POST.get('stipend')
            stipend_amount = request.POST.get('stipend_amount')
            internship_status = request.POST.get('status')
            offer_letter_submitted = request.FILES.get('offer_letter_submitted')
            completion_certificate_submitted = request.FILES.get('completion_certificate_submitted')

            InternshipResponse.objects.create(
                organisation_name=org_name,
                organisation_address_website=org_address,
                nature_of_work=nature_of_work,
                repr_name=repr_name,
                repr_designation=repr_designation,
                repr_email_id=repr_email_id,
                repr_mobile_no=repr_mobile_no,
                start_date=start_date,
                completion_date=completion_date,
                duration=duration,
                mode_of_internship=internship_mode,
                stipend=stipend,
                stipend_amount=stipend_amount,
                status=internship_status,
                offer_letter_submitted=offer_letter_submitted,
                completion_certificate_submitted=completion_certificate_submitted
            )
        else:
            idnum=request.POST.get("internship_id_num")
            print(idnum,'ss')
            internship=InternshipResponse.objects.get(id=idnum)
            a,cre=OD.objects.update_or_create(
            register_number=internship.register_number,
            organisation_name=internship.organisation_name,
                        id=idnum,
            defaults={
                'email_id': internship.email_id,
            },
            approved=False
            )

    student_internships = InternshipResponse.objects.filter(digital_id=205002001)
    approved_od=list(OD.objects.filter(approved=True))

    for i in range(len(approved_od)):
        approved_od[i] =approved_od[i].id
    print(approved_od)
    return render(request, "studentprofile.html", {
        "internships": student_internships,
        'od':approved_od,
        "announcements": Announcement.objects.all()
    })


from .models import Student


from django.http import JsonResponse
from .models import Internship

def get_internship_details(request):
    if request.method == 'GET':
        internship_id = request.GET.get('internship_id')
        try:
            internship = Internship.objects.get(id=internship_id)
            data = {
                'org_name': internship.org_name,
                'org_address': internship.org_address,
                'nature_of_work': internship.nature_of_work,
                'reporting_authority': internship.reporting_authority,
                'start_date': str(internship.start_date),
                'end_date': str(internship.end_date),
                'internship_mode': internship.internship_mode,
                'stipend': internship.stipend,
                'ppo': internship.ppo,
                'status': internship.status,
            }
            return JsonResponse(data)
        except Internship.DoesNotExist:
            return JsonResponse({'error': 'Internship not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


from django.http import JsonResponse
from .models import InternshipResponse  # Assuming your model is named InternshipResponse

def get_internship_response_details(request):
    if request.method == 'GET':
        internship_response_id = request.GET.get('internship_response_id')
        print(internship_response_id)
        try:
            internship_response = InternshipResponse.objects.get(id=internship_response_id)
            data = {
                'digital_id': internship_response.digital_id,
                'register_number': internship_response.register_number,
                'name': internship_response.name,
                'email_id': internship_response.email_id,
                'alternate_email_id': internship_response.alternate_email_id,
                'mobile_no': internship_response.mobile_no,
                'organisation_name': internship_response.organisation_name,
                'organisation_address_website': internship_response.organisation_address_website,
                'nature_of_work': internship_response.nature_of_work,
                'repr_name': internship_response.repr_name,
                'repr_designation': internship_response.repr_designation,
                'repr_email_id': internship_response.repr_email_id,
                'repr_mobile_no': internship_response.repr_mobile_no,
                'start_date': str(internship_response.start_date),  # Convert to string if needed
                'completion_date': str(internship_response.completion_date),  # Convert to string if needed
                'duration': internship_response.duration,
                'status': internship_response.status,
                'mode_of_internship': internship_response.mode_of_internship,
                'stipend': internship_response.stipend,
                'stipend_amount': float(internship_response.stipend_amount),  # Convert to float if needed
                'remarks': internship_response.remarks,
                'offer_letter_submitted': internship_response.offer_letter_submitted,
                'completion_certificate_submitted': internship_response.completion_certificate_submitted,
            }
            return JsonResponse(data)
        except InternshipResponse.DoesNotExist:
            return JsonResponse({'error': 'Internship response not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def student_page(request, student_id):
    student=InternshipResponse.objects.filter(digital_id=student_id)
    print(student[0].digital_id)

    return render(request,'student.html',{'internships':student,'student': student[0]})





from django.shortcuts import render
from .models import Internship
from collections import Counter
import json
from django.db.models import Count

def internship_statistics(request):
    internships = InternshipResponse.objects.all()

    # Internship Mode Distribution
    mode_distribution = dict(Counter(internships.values_list('mode_of_internship', flat=True)))

    # Stipend Distribution
    stipend_distribution = dict(Counter(internships.values_list('stipend', flat=True)))


    # Status Distribution
    status_distribution = dict(Counter(internships.values_list('status', flat=True)))

    # Nature of Work Distribution
    nature_of_work_distribution = dict(Counter(internships.values_list('nature_of_work', flat=True)))

    # Number of Internships per Organization
    org_distribution = internships.values('organisation_name').annotate(total=Count('organisation_name')).order_by('-total')
    org_distribution = {entry['organisation_name']: entry['total'] for entry in org_distribution}

    # Internship Durations
    duration_distribution = [
        {
            'student': internship.digital_id,
            'duration': (internship.completion_date - internship.start_date).days if internship.completion_date and internship.start_date else 0
        }
        for internship in internships
    ]
    internships = InternshipResponse.objects.all()
    total_internships = internships.count()
    total_students = len(set(internship.name for internship in internships))

    average_duration = calculate_average_duration(internships)
    mode_distribution = calculate_distribution(internships, 'mode_of_internship')
    stipend_distribution = calculate_distribution(internships, 'stipend')
    status_distribution = calculate_distribution(internships, 'status')
    top_organizations = calculate_top_organizations(internships)

    context = {
  
    }
    context = {
        'stipend_amount':InternshipResponse.objects.values('stipend_amount').annotate(count=Count('stipend_amount')).order_by('stipend_amount'),
        'total_internships': total_internships,
        'total_students': total_students,
        'average_duration': average_duration,
        'mode_distribution': mode_distribution,
        'stipend_distribution': stipend_distribution,
        'status_distribution': status_distribution,
        'top_organizations': top_organizations,
        'mode_distribution': json.dumps(mode_distribution),
        'stipend_distribution': json.dumps(stipend_distribution),
        'status_distribution': json.dumps(status_distribution),
        'nature_of_work_distribution': json.dumps(nature_of_work_distribution),
        'org_distribution': json.dumps(org_distribution),
        'duration_distribution': json.dumps(duration_distribution),
    }


    return render(request, 'internship.html', context)

def calculate_average_duration(internships):
    durations = [(internship.completion_date - internship.start_date).days for internship in internships if internship.completion_date and internship.start_date]
    return sum(durations) / len(durations) if durations else 0

def calculate_distribution(internships, field):
    distribution = dict(Counter(internships.values_list(field, flat=True)))
    print(distribution)
    return distribution

def calculate_top_organizations(internships, n=5):
    organizations = internships.values('organisation_name').annotate(total=Count('organisation_name')).order_by('-total')[:n]
    return organizations

from collections import Counter



from django.views.decorators.csrf import csrf_exempt





import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from datetime import datetime
from .models import InternshipResponse  # Import your Django model


def parse_date(date_str):
    for fmt in ("%d/%m/%Y", "%d/%m/%y", "%d-%m-%Y", "%d-%m-%y"):
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise ValueError(f"Date format for '{date_str}' is not supported")

def sync_data_with_sheets():
    # Authenticate with Google Sheets API
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("intern/credentials.json", scopes=scopes)
    client = gspread.authorize(creds)

    # Open the Google Sheet
    sheet_id = "1MVkeFe3kWfES3Ni1J8ED7bL_zcmnk-3uCLRTiL0ZIKA"
    workbook = client.open_by_key(sheet_id)
    worksheet = workbook.sheet1  # Assuming the data is in the first sheet

    # Read data from the Google Sheet
    data = worksheet.get_all_values()

    # Skip the header row and create or update Django model instances
    for row in data[1:]:
        try:
            # Convert date strings to Python datetime objects
            start_date = parse_date(row[15])
            completion_date = parse_date(row[16])

            # Create or update model instance based on digital_id
            internship_response, created = InternshipResponse.objects.update_or_create(
                digital_id=row[2],  # Use digital_id as a unique identifier
                defaults={
                    'register_number': row[3],
                    'name': row[4],
                    'email_id': row[5],
                    'alternate_email_id': row[6],
                    'mobile_no': row[7],
                    'organisation_name': row[8],
                    'organisation_address_website': row[9],
                    'nature_of_work': row[10],
                    'repr_name': row[11],
                    'repr_designation': row[12],
                    'repr_email_id': row[13],
                    'repr_mobile_no': row[14],
                    'start_date': start_date,
                    'completion_date': completion_date,
                    'duration': row[17],
                    'status': row[18].lower().capitalize().strip(),
                    'mode_of_internship': row[19].lower().capitalize().strip() ,
                    'stipend': row[20].lower().capitalize().strip(),
                    'stipend_amount': row[21],
                    'remarks': row[22],
                    'offer_letter_submitted': row[23],
                    'completion_certificate_submitted': row[24]
                }
            )
        except ValueError as e:
            print(f"Error parsing date for row {row}: {e}")


def sync_data_with_sheets1():
    # Authenticate with Google Sheets API
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("intern/credentials.json", scopes=scopes)
    client = gspread.authorize(creds)
    # Open the Google Sheet
    sheet_id = "1F_-74LnjJ5a_EUx6e-cc_Ete6KExInRKiFkaifbswOk"
    workbook = client.open_by_key(sheet_id)
    worksheet = workbook.sheet1  # Assuming the data is in the first sheet

    # Read data from the Google Sheet
    data = worksheet.get_all_values()
    # Skip the header row and create or update Django model instances
    for row in data[1:]:
        # Convert date strings from "dd-mm-yyyy" to Python datetime objects
        for i in InternshipResponse.objects.all():

            if i.register_number ==row[3] and i.organisation_name==row[1]:
                intern_id=i.id
        # Create or update model instance based on digital_id
        internship_response, created = OD.objects.update_or_create(
            register_number=row[3], 
            organisation_name=row[1],
            id=intern_id,
            defaults={
                'email_id': row[2],
            },
            approved=True if row[4]=="yes" else False
        )
        internship_response.id=intern_id
        internship_response.save()


        # Print the created/updated instance for debugging
        print("Created:", created, "InternshipResponse:", internship_response)


def dummy():
    return None

from django.shortcuts import render
from django.utils.dateparse import parse_date
from .models import InternshipResponse

def faculty(request):
    student_internships = InternshipResponse.objects.all()

    search_query = request.GET.get('search', '')
    start_date_query = request.GET.get('start_date', '')
    end_date_query = request.GET.get('end_date', '')
    name_query = request.GET.get('name', '')
    stipend_query = request.GET.get('stipend', '')
    mode_query = request.GET.get('mode', '')
    status_query = request.GET.get('status', '')
    completion_cert_query = request.GET.get('completion_certificate', '')

    if search_query:
        student_internships = student_internships.filter(organisation_name__icontains=search_query)
    
    if name_query:
        student_internships = student_internships.filter(name__icontains=name_query)

    if stipend_query:
        student_internships = student_internships.filter(stipend=stipend_query)

    if mode_query:
        student_internships = student_internships.filter(mode_of_internship=mode_query)

    if status_query:
        student_internships = student_internships.filter(status=status_query)

    if completion_cert_query:
        if completion_cert_query.lower() == 'yes':
            student_internships = student_internships.filter(completion_certificate_submitted__isnull=False)
        elif completion_cert_query.lower() == 'no':
            student_internships = student_internships.filter(completion_certificate_submitted__isnull=True)

    if start_date_query and end_date_query:
        start_date = parse_date(start_date_query)
        end_date = parse_date(end_date_query)
        if start_date and end_date:
            student_internships = student_internships.filter(start_date__gte=start_date, completion_date__lte=end_date)

    return render(request, "calender.html", {"internship": student_internships})


def student_internships(request):
    student_internships = InternshipResponse.objects.all()

    search_query = request.GET.get('search', '')
    start_date_query = request.GET.get('start_date', '')
    end_date_query = request.GET.get('end_date', '')
    name_query = request.GET.get('name', '')
    stipend_query = request.GET.get('stipend', '')
    mode_query = request.GET.get('mode', '')
    status_query = request.GET.get('status', '')
    completion_cert_query = request.GET.get('completion_certificate', '')

    if search_query:
        student_internships = student_internships.filter(organisation_name__icontains=search_query)
    
    if name_query:
        student_internships = student_internships.filter(name__icontains=name_query)

    if stipend_query:
        student_internships = student_internships.filter(stipend=stipend_query)

    if mode_query:
        student_internships = student_internships.filter(mode_of_internship=mode_query)

    if status_query:
        student_internships = student_internships.filter(status=status_query)

    if completion_cert_query:
        if completion_cert_query.lower() == 'yes':
            student_internships = student_internships.filter(completion_certificate_submitted__isnull=True)
        elif completion_cert_query.lower() == 'no':
            student_internships = student_internships.filter(completion_certificate_submitted__isnull=False)

    if start_date_query and end_date_query:
        start_date = parse_date(start_date_query)
        end_date = parse_date(end_date_query)
        if start_date and end_date:
            student_internships = student_internships.filter(start_date__gte=start_date, completion_date__lte=end_date)

    return render(request, "studentinternships.html", {"internship": student_internships})


def odrequest(request):

 
    internship_details=[]
    try:
        for i in OD.objects.all():
            for j in InternshipResponse.objects.all():
                if i.organisation_name==j.organisation_name and i.register_number==j.register_number and i.approved==0:
                    internship_details.append(j)
        return render(request, "odrequest.html",{"internship": internship_details})
    except InternshipResponse.DoesNotExist:
        ...
    print(internship_details)
    return render(request, "odrequest.html",{"internship": internship_details})




def write_sheet(response):
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("intern/credentials.json", scopes=scopes)
    client = gspread.authorize(creds)

    # Open the Google Sheet
    sheet_id = "1F_-74LnjJ5a_EUx6e-cc_Ete6KExInRKiFkaifbswOk"
    workbook = client.open_by_key(sheet_id)
    worksheet = workbook.worksheet("Sheet1") # Assuming the data is in the first sheet
    print(worksheet.get_all_values())
    data=[]
    data.append([
                response.register_number,
                response.email_id,
                response.organisation_name,
                response.start_date.strftime('%Y-%m-%d'),
                response.completion_date.strftime('%Y-%m-%d'),
                "yes"
            ])

        # Insert data into the sheet
    worksheet.append_rows(data, value_input_option="RAW")  # Append the data
def send_mail(mail,message):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # For starttls
    sender_email = 'sanjeevi555pn@gmail.com'
    receiver_email = 'receiver_email@gmail.com'
    password = 'Sanjeevi@05'

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = mail
    msg['Subject'] = 'Test Email'

    # Email body
    body = message
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, password)  # Login to the SMTP server
        
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print('Email sent successfully')
        
    except Exception as e:
        print(f'Error: {e}')
    finally:
        server.quit()  # Close the connection

def summa(orgname,regnum):
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("intern/credentials.json", scopes=scopes)
    client = gspread.authorize(creds)
    # Open the Google Sheet
    sheet_id = "1F_-74LnjJ5a_EUx6e-cc_Ete6KExInRKiFkaifbswOk"
    workbook = client.open_by_key(sheet_id)
    worksheet = workbook.sheet1  # Assuming the data is in the first sheet

    # Read data from the Google Sheet
    data = worksheet.get_all_values()
    updated_data=[["timestamp","ORGANISATION NAME","EMAIL ID",'REGISTER NUMBER','APPROVED']]
    # Skip the header row and create or update Django model instances
    for row in data[1:]:
        if row[1]==orgname and row[3]==regnum:
            row[4]='yes'
        updated_data.append(row)
    worksheet.clear()
    worksheet.append_rows(updated_data,value_input_option="RAW")
def approve(request):
    if request.method == "POST":
        selected_interns = request.POST.get('selected_interns', '')
        selected_intern_ids = selected_interns.split(',') if selected_interns else []
        interns=[]
        for i in selected_intern_ids:
            interns.append(InternshipResponse.objects.get(id=i))
        for j in interns:
            write_sheet(j)
            a=OD.objects.get(id=j.id)
            a.approved=True
            a.save()
            summa(j.organisation_name,j.register_number)
        return redirect(reverse('odrequest'))
    



# myapp/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# myapp/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Announcement, Faculty, Student
from django.contrib.auth.decorators import login_required
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def make_announcement(request):
    if request.method == 'POST':
        announcement_text = request.POST.get('announcement')
        if announcement_text:
            announcement = Announcement.objects.create(
                text=announcement_text,
                user=Faculty.objects.get(faculty_id=faculty_id)
            )
            # Notify other users via WebSocket
            channel_layer = get_channel_layer()
            try:
                async_to_sync(channel_layer.group_send)(
                    "announcement_group", {
                        "type": "announcement_message",
                        "message": announcement_text,
                    }
                )
            except:
                ...
            return redirect(reverse('faculty'))
        else:
            return JsonResponse({'status': 'error', 'message': 'No announcement text provided'})
    return redirect(reverse('faculty'))

def announcements(request):
    return render(request, 'announcements.html')


