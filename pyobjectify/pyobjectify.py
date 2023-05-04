from csv import DictReader
from enum import auto, Enum, unique
from json import loads
from pandas import DataFrame, json_normalize, read_excel
from requests import get
from xmltodict import parse


@unique
class InputType(Enum):
    """
    An enumeration of the input types supported by pyobjectify.

    The end-user does not have to interface with this, but it is provided for more granular operations.
    """

    JSON = auto()
    CSV = auto()
    TSV = auto()
    XML = auto()
    XLSX = auto()


OUTPUT_TYPES = (list, dict, DataFrame)
"""
A set of the output types supported by pyobjectify.

The end-user does not have to interface with this, but it is provided for more granular operations.
"""

CONVERSIONS = {
    InputType.JSON: [dict, list, DataFrame],
    InputType.CSV: [list],
    InputType.TSV: [list],
    InputType.XML: [dict],
    InputType.XLSX: [dict],
}
"""
A dictionary of allowable conversions,
where the key is a supported input type,
and the value is a list of supported output types.

The end-user does not have to interface with this, but it is provided for more granular operations.
"""


@unique
class Connectivity(Enum):
    """
    An enumeration of the supported file connectivity types:

    - `ONLINE_STATIC` = The URL points to a static file on the Internet.
    - `LOCAL` = The URL is a path to a local file.

    For example, at the moment, a data stream from the Internet is not supported.

    The end-user does not have to interface with this, but it is provided for more granular operations.
    """

    ONLINE_STATIC = auto()
    LOCAL = auto()


class Resource:
    """
    The Resource class stores some metadata about the resource to simplify the code.

    The end-user does not have to interface with this, but it is provided for more granular operations.
    """

    def __init__(self, url, connectivity):
        url = url.replace("file://", "")
        self.url = url
        self.connectivity = connectivity

        if connectivity == Connectivity.ONLINE_STATIC:
            response = get(url)
            self.response = response
            self.plaintext = response.text

        elif connectivity == Connectivity.LOCAL:
            url = url.replace("file://", "")

            file_obj = open(url, "r")
            self.response = file_obj
            try:
                self.plaintext = file_obj.read()
                self.response.seek(0, 0)
            except Exception:  # XLSX data does not like to be read
                self.plaintext = None

    def __eq__(self, other):
        # For Internet resources,
        # Resource.response may have stochastic attributes like time elapsed.
        # URL, connectivity type, plaintext should be enough to determine different Resources.
        return self.url == other.url and self.connectivity == other.connectivity and self.plaintext == other.plaintext


def url_to_connectivity(url):
    """
    Get the connectivity type of the resource.

    The end-user does not have to interface with this, but it is provided for more granular operations.

    Args:
        url (str): The URL to a resource.

    Returns:
        Connectivity: An attribute in the enumeration `Connectivity`. The calculated connectivity of the resource type.
    """
    local_conditions = [url.startswith("file:///"), url.startswith("/"), url.startswith(".")]
    if any(local_conditions):
        return Connectivity.LOCAL
    else:
        return Connectivity.ONLINE_STATIC


def retrieve_resource(url, connectivity):
    """
    Retrieves the resource at the URL using the connectivity type and stores it in a Resource object.

    The end-user does not have to interface with this, but it is provided for more granular operations.

    Args:
        url (str): The URL to a resource.
        connectivity (:obj:`Connectivity`): An attribute in the enumeration Connectivity.
            The calculated connectivity type of the resource.

    Returns:
        Resource: The Resource object for the resource at the URL specified.

    Raises:
        TypeError: The connectivity type is not supported.
    """
    if not isinstance(connectivity, Connectivity):
        raise TypeError(f"The connectivity type {connectivity} is not supported.")

    return Resource(url, connectivity)


def get_resource_types(resource):
    """
    Get possible resource types of the resource.

    The end-user does not have to interface with this, but it is provided for more granular operations.

    Args:
        resource (:obj:`Resource`): The Resource object for the resource.

    Returns:
        list: A list of possible resource types of the resource.

    Raises:
        TypeError: The resource is of a type that is not supported.
    """
    possible = list(InputType)

    try:
        _ = loads(resource.plaintext)
    except Exception:
        possible.remove(InputType.JSON)
        pass

    try:
        dicts = DictReader(resource.response)
        if resource.connectivity is Connectivity.LOCAL:
            resource.response.seek(0, 0)

        # Ensure that each row has the same number of fields
        nums_fields = set([len(d.items()) for d in list(dicts)])
        if resource.connectivity is Connectivity.LOCAL:
            resource.response.seek(0, 0)
        assert len(nums_fields) == 1
        # Ensure that the number of fields is greater than 1
        (num_fields,) = nums_fields

        assert num_fields > 1  # Data that have only one column will not be interpreted as CSVs
    except Exception:
        possible.remove(InputType.CSV)

    try:
        dicts = DictReader(resource.response, delimiter="\t")
        if resource.connectivity is Connectivity.LOCAL:
            resource.response.seek(0, 0)

        # Ensure that each row has the same number of fields
        nums_fields = set([len(d.items()) for d in list(dicts)])
        if resource.connectivity is Connectivity.LOCAL:
            resource.response.seek(0, 0)
        assert len(nums_fields) == 1

        # Ensure that the number of fields is greater than 1
        (num_fields,) = nums_fields
        assert num_fields > 1  # Data that have only one column will not be interpreted as TSVs
    except Exception:
        possible.remove(InputType.TSV)

    try:
        _ = parse(resource.plaintext)
        assert resource.plaintext[0] == "<"
    except Exception:
        possible.remove(InputType.XML)

    try:
        df = read_excel(resource.url, sheet_name=None)
        sheets_dict = {}
        for sheet_name, df in df.items():
            sheets_dict[sheet_name] = df.to_dict()
    except Exception:
        possible.remove(InputType.XLSX)

    if len(possible) == 0:
        raise TypeError("The type of the resource is not supported.")

    return possible


def get_conversions(in_types, out_type=None):
    """
    Get possible conversions for the probable resource types.
    If the user specified a preferred output type, filter out any undesirable conversions to consider.

    The end-user does not have to interface with this, but it is provided for more granular operations.

    Args:
        in_types (:obj:`list`): A list of calculated possible resource types.
        out_type (:obj:`class`, optional): The user-specified data type of the output.

    Returns:
        list: A list of (in, out) conversion tuples as described above.
    Raises:
        TypeError: There are no possible conversions.
    """

    # There is guaranteed at least one probable in_type
    # Go through each probable resource data type.
    # Use lists to preserve order.
    conversions = []  # To make a list of possible conversions.
    poss_out_types = []  # To make list of all output types based on probable input types.
    for in_type in in_types:
        for poss_out_type in CONVERSIONS[in_type]:
            if out_type is None:
                if (in_type, poss_out_type) not in conversions:
                    conversions.append((in_type, poss_out_type))
                if poss_out_type not in poss_out_types:
                    poss_out_types.append(poss_out_type)
            elif poss_out_type is out_type:  # (and user specified a preferred output type)
                if (in_type, poss_out_type) not in conversions:
                    conversions.append((in_type, poss_out_type))
                if poss_out_type not in poss_out_types:
                    poss_out_types.append(poss_out_type)
    if out_type is not None and out_type not in poss_out_types:
        raise TypeError(f"The resource cannot be converted into the requested data type {out_type}.")

    return conversions


def json_to_list(resource):
    """
    Helper function to convert JSON data to a list.

    The end-user does not have to interface with this, but it is provided for more granular operations.

    Args:
        resource (:obj:`Resource`): The Resource object for the JSON resource.

    Returns:
        list: A list represenation of the JSON resource.
    """
    json = loads(resource.plaintext)
    if type(json) is dict:
        return [json]
    return json


def json_to_dict(resource):
    """
    Helper function to convert JSON data to a dictionary.

    The end-user does not have to interface with this, but it is provided for more granular operations.

    Args:
        resource (:obj:`Resource`): The Resource object for the JSON resource.

    Returns:
        dict: A dictionary represenation of the JSON resource.
    """
    json = loads(resource.plaintext)
    if type(json) is list:
        return {"data": json}
    return json


def json_to_dataframe(resource):
    """
    Helper function to convert JSON data to a pandas DataFrame.

    The end-user does not have to interface with this, but it is provided for more granular operations.

    Args:
        resource (:obj:`Resource`): The Resource object for the JSON resource.

    Returns:
        pandas.DataFrame: A pandas DataFrame represenation of the JSON resource.
    """
    json = loads(resource.plaintext)
    df = json_normalize(json)
    return df


def csv_to_list(resource):
    """
    Helper function to convert CSV data to a list.

    The end-user does not have to interface with this, but it is provided for more granular operations.

    Args:
        resource (:obj:`Resource`): The Resource object for the CSV resource.

    Returns:
        list: A list represenation of the CSV resource.
    """
    rows = DictReader(resource.response)
    return list(rows)


def tsv_to_list(resource):
    """
    Helper function to convert TSV data to a list.

    The end-user does not have to interface with this, but it is provided for more granular operations.

    Args:
        resource (:obj:`Resource`): The Resource object for the TSV resource.

    Returns:
        list: A list represenation of the TSV resource.
    """
    rows = DictReader(resource.response, delimiter="\t")
    return list(rows)


def xml_to_dict(resource):
    """
    Helper function to convert XML data to a dictionary.

    The end-user does not have to interface with this, but it is provided for more granular operations.

    Args:
        resource (:obj:`Resource`): The Resource object for the XML resource.

    Returns:
        dict: A dictionary represenation of the XML resource.
    """
    rows = parse(resource.plaintext)
    return rows


def xlsx_to_dict(resource):
    """
    Helper function to convert XLSX data to a dictionary.
    """
    df = read_excel(resource.url, sheet_name=None)
    sheets_dict = {}
    for sheet_name, df in df.items():
        sheets_dict[sheet_name] = df.to_dict()
    return sheets_dict


def convert(resource, conversions):
    """
    Attempts to convert the resource data through possible conversions.

    The end-user does not have to interface with this, but it is provided for more granular operations.

    Args:
        resource (:obj:`Resource`): he Resource object for the resource.
        conversions (list): The list of all possible conversions, filtered if user specified output data type.

    Returns:
        object: The first successful conversion from the probable resource type to an output data type.

    Raises:
        TypeError: None of the possible conversions were successful.
    """
    for conversion in conversions:
        try:
            i_type, o_type = conversion
            # Handle each case. Currently, only JSON has multiple options.
            # Return the first conversion that works.
            if i_type is InputType.JSON:
                if o_type is dict:
                    return json_to_dict(resource)
                elif o_type is list:
                    return json_to_list(resource)
                elif o_type is DataFrame:
                    return json_to_dataframe(resource)
            elif i_type is InputType.CSV:
                return csv_to_list(resource)
            elif i_type is InputType.TSV:
                return tsv_to_list(resource)
            elif i_type is InputType.XML:
                return xml_to_dict(resource)
            elif i_type is InputType.XLSX:
                return xlsx_to_dict(resource)
        except Exception:
            continue  # Try the next conversion

    # Reach here means none of the conversions worked!
    raise TypeError("The type of the resource is not supported.")


def from_url(url, out_type=None):
    """
    This is the main interface that the end-user interacts with.
        Given a URL, converts the resource data to a parsable Python object.

    Args:
        url (str): A URL to a resource.
        out_type (:obj:`class`, optional): The user-specified data type of the output.

    Returns:
        object: A parsable Python object representation of the resource.

    Raises:
        TypeError: The user-specified data type of the output is not supported.
    """

    if out_type is not None and out_type not in OUTPUT_TYPES:
        raise TypeError(f"The specified output type {out_type} is not supported.")

    # (1) Get resource connectivity type
    connectivity = url_to_connectivity(url)

    # (2) Retrieve resource
    resource = retrieve_resource(url, connectivity)

    # (3) Determine input type
    in_types = get_resource_types(resource)

    # (4) Determine possible conversions
    conversions = get_conversions(in_types, out_type)

    # (5) Convert to output type
    output = convert(resource, conversions)

    # (6) Close the file object if open()-ed
    if connectivity is Connectivity.LOCAL:
        resource.response.close()

    return output
