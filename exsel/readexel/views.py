from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import openpyxl
from .models import Book


class NewLotForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


# Create your views here.
def index(request):
    if request.method == "POST":
        file = request.FILES["file"]  # form = NewLotForm(request.POST, request.FILES)
        # file = NewLotForm(request.POST, request.FILES)
        wookbook = openpyxl.load_workbook(file)
        # Define variable to read the active sheet:
        worksheet = wookbook.active
        print(worksheet.max_row)
        print(worksheet.max_column)
        # Iterate the loop to read the cell values
        for rows in worksheet.iter_rows(2, worksheet.max_row):
            print(rows[0].value)

            book = Book.objects.create(photo_link=rows[0].value, name_of_event=rows[1].value, date_of_event=rows[2].value,
                                       description=rows[3].value, start_time=rows[4].value, end_time=rows[5].value,
                                       location_name=rows[6].value, first_event_category=rows[7].value,
                                       second_category=rows[8].value, free_or_Paid=rows[9].value,
                                       ticket_site_link=rows[10].value,
                                       )
            book.save()
        # for i in range(0, worksheet.max_row):
        #     for col in worksheet.iter_cols(1, worksheet.max_column):
        #         print(col[i].value)
        #         # print(col[i].value, end="\t\t")
        # Date_of_event = models.CharField(max_length=540, blank=True, null=True, default=None)
        # Description = models.CharField(max_length=540, blank=True, null=True, default=None)
        # Start_time = models.CharField(max_length=40, blank=True, null=True, default=None)
        # End_time = models.CharField(max_length=40, blank=True, null=True, default=None)
        # Location_name = models.CharField(max_length=150, blank=True, null=True, default=None)
        # First_event_category = models.CharField(max_length=350, blank=True, null=True, default=None)
        # second_category = models.CharField(max_length=350, blank=True, null=True, default=None)
        # Free_or_Paid = models.CharField(max_length=350, blank=True, null=True, default=None)
        # Ticket_site_link = models.URLField(max_length=3

        return HttpResponse("your model is already in the database go to https://yan3608.pythonanywhere.com/admin (login: yan password: 390871) and make sure. And remove empty values rom the table. there are a thousand empty values")
    else:
        return render(request, "readexel/index.html", {'form': NewLotForm})

# return render(request, "radisna/add_group.html", {'form': CreateFormGroup})
