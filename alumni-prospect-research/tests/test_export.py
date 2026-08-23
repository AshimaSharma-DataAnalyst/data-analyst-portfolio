import pandas as pd

from app.services.export_service import ExportService

exporter = ExportService()

data = [

    {

        "Name": "Satya Nadella",

        "Company": "Microsoft",

        "Designation": "CEO"

    },

    {

        "Name": "Sundar Pichai",

        "Company": "Google",

        "Designation": "CEO"

    },

    {

        "Name": "Andy Jassy",

        "Company": "Amazon",

        "Designation": "CEO"

    }

]

df = pd.DataFrame(data)

exporter.export_csv(

    df,

    "exports/alumni.csv"

)

exporter.export_excel(

    df,

    "exports/alumni.xlsx"

)

exporter.export_json(

    df,

    "exports/alumni.json"
)
