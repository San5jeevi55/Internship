import gspread
from google.oauth2.service_account import Credentials
from models import *
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
 # Skip the header row and create Django model instances
    for row in data[1:]:
        internship_response =   InternshipResponse(
            digital_id=row[0],
            register_number=row[1],
            name=row[2],
            email_id=row[3],
            alternate_email_id=row[4],
            mobile_no=row[5],
            organisation_name=row[6],
            organisation_address_website=row[7],
            nature_of_work=row[8],
            repr_name=row[9],
            repr_designation=row[10],
            repr_email_id=row[11],
            repr_mobile_no=row[12],
            start_date=row[13],
            completion_date=row[14],
            duration=row[15],
            status=row[16],
            mode_of_internship=row[17],
            stipend=row[18],
            stipend_amount=row[19],
            remarks=row[20],
            offer_letter_submitted=row[21],
            completion_certificate_submitted=row[22]
        )
        internship_response.save()
sync_data_with_sheets()
   