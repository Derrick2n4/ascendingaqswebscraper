import oopscrape
import logging
import smtplib
import csv
import warnings
from io import BytesIO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
import openpyxl


# Check for excel file if it exists append new data if it doesnt exist update it with new data
warnings.filterwarnings('ignore', category=UserWarning, module="openpyxl")
# start driver
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Setting Browser Driver")
url = "https://vmatrix1.brevardclerk.us/beca/CaseType_Search.cfm"
web_nav = oopscrape.Navigation()
start_driver = web_nav.setup(url)

# Accept terms and cons
# web_nav.accept_usage(xpath='/html/body/form/table/tbody/tr[1]/td/input[1]')
# Submit acceptance
logger.info("accepting terms and conditions on splash page")
web_nav.submit_button()
# Navigate to probate page

# select gen pop court recs
logger.info("clicking general public records buttons")
web_nav.select_gen_pop_court_records()
logger.info("Selecting case type")
web_nav.case_type_menu_option(xpath='/html/body/div[2]/table/tbody/tr[2]/td/div/div/ul/li[4]/a')
# go to probate page

logger.info("Parsing through case types to find probate option")
web_nav.get_probate_page()
logger.info("Click Search Button")
web_nav.search_button()
logger.info("Collecting probate links")
# web_nav.get_probate_links()
# logger.info("Navigate to case info window")
# case_info_url = 'https://vmatrix1.brevardclerk.us/beca/all_results.cfm?x=4BB88F8C738788AC99BFD224CC0A2DDB79DCE7B89F13E70AFE03EBDADFCBC76526FA6ABFEBD34D16D7B733171ED4D4FE'
# web_nav.setup(case_info_url)
# web_nav.get_case_data()

data = web_nav.get_probate_link()
filepath = "C:/Users/P3128232/florida_boyz/test.csv"
data = ["Swag",
          "SwagCase",
          "numberSwag"
          "DeadSwag",
          "ICantSPellPetitionerTosavemylife",
          "AttorneyKnowMySwagNotMyStory"
          ]
case_dict = {"filing_date":[i for i in data if "Swag" in i],
                   "case_number":[i for i in data if "numberSwag" in i],
                   "decedntInfo":[i for i in data if "DeadSwag" in i],
                   "petitionerInfo":[i for i in data if "ICantSPellPetitionerTosavemylife" in i],
                   "attorneyInfo":[i for i in data if "AttorneyKnowMySwagNotMyStory" in i]}

with open(filepath, "a", newline='') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=case_dict.keys())
      if csvfile.tell() == 0:
            writer.writeheader()

            for i in range(len(case_dict[0])):
                  row = {key: case_dict[i] for key in case_dict.keys()}
                  writer.writerow(row)
                  writer.save()




from_email = 'aureliumdevelopment@gmail.com'
password = 'wpwj nmyp sgql yppx'
to_email = 'ascendingacquisitions@gmail.com'

subject = 'Results from Python Script'
body = 'Please find the attached CSV file.'
attachment = open(filepath, 'rb')
part = MIMEBase('application', 'octet-stream')
# part = MIMEapplication(filepath.content, )
# part = MIMEApplication(attachment, _subtype="text/csv")
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f"attachment; filename = {attachment}")
msg = MIMEMultipart('mixed')
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))
msg.attach(part)
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
      smtp.starttls()
      smtp.login(from_email, password)
      smtp.send_message(msg)
      smtp.quit()

