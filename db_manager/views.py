from django.shortcuts import render
from django.shortcuts import redirect
from core.models import PropertyTypeModel,BallincolligPropertyModel
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import pandas as pd



@login_required
def db_manager(request):
    return render(request, "db-manager.html", )


@login_required
def property_upload(request):
    """View for uploading data to database """
    if request.method == "POST":
        csv_file=request.FILES["csv_file"]
        dataset = pd.read_csv(csv_file, encoding="utf-8-sig")

        for property in dataset.itertuples():

            # Query DB for Foreign Key Model using string from 'property_type' column in CSV dataset
            property_type_model = get_object_or_404(PropertyTypeModel, property_type=property.property_type)

            BallincolligPropertyModel.objects.get_or_create(
               area=property.area,
               full_address=property.full_address,
               price=property.price,
               property_type=property_type_model,
               sold_date=property.date,
               longitude=property.long,
               latitude=property.lat
            )

        return redirect("/")

    return render(request, "property-upload.html", )


