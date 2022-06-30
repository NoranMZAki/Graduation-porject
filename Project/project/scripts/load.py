from properties.models import Property
import csv


def run():
    with open('properties/Copy of kc_house - kc_house (4).csv') as file:
        reader = csv.reader(file)

        next(reader)  # Advance past the header
        Property.objects.all().delete()
        for row in reader:
            print(row)

            film = Property(


                bedrooms=row[2],
                bathrooms=row[3],
                SQFT_Living=row[4],
                SQFT_lot=row[5],
                floors=row[6],


                waterfront=row[7],
                view=row[8],
                condition=row[9],
                grade=row[10],
                SQFT_above=row[11],
                SQFT_basement=row[12],
                yr_built=row[13],
                yr_renovated=row[14],
                zip_code=row[15],
                lat=row[16],
                long=row[17],
                SQFT_living15=row[18],

                SQFT_lot15=row[19],



                price=row[20],
                image=row[21],
                title=row[22],
                description=row[23],
            )
            film.save()
