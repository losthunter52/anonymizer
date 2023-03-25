from .utils import data_tools
from .lib import masking
from .lib import number_variation


def prepare(data, fields):
    fields = data_tools.prepare_fields(fields)
    prepared_database = data_tools.prepare_database_fields(data, fields)
    return prepared_database

def mask(
    data,
    fields,
    method="full",
    length=0,
    masked=False,
    initial_rage=0,
    final_range=0,
    mask_result_lenght=False
):
    database = masking.mask_data(
        data,
        fields,
        method,
        length,
        masked,
        initial_rage,
        final_range,
        mask_result_lenght
    )

    return database

def num_variation(
    data,
    fields
):
  database = number_variation.var_num_random_data(
        data,
        fields,
        10,
        6
    )
  return database