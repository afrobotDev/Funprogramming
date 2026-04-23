from enum import Enum

CSVExportStatus = Enum(
    "CSVExportStatus", ["PENDING", "PROCESSING", "SUCCESS", "FAILURE"]
)

def get_csv_status(status, data):
    match (status):
        case CSVExportStatus.PENDING:
                 new_data = list(map(lambda sub: list(map(str, sub)), data))
                 return "Pending...", new_data

        case CSVExportStatus.PROCESSING:
                new_data = '\n'.join(map(lambda sub: ','.join(map(str, sub)), data))
                return "Processing...", new_data

        case CSVExportStatus.SUCCESS:
                return "Success!", data
    

        case CSVExportStatus.FAILURE:
                new_data = '\n'.join(map(lambda sub: ','.join(map(str, sub)), data))
                return "Unknown error, retrying...", new_data

        case _:
                raise ValueError("unknown export status")
