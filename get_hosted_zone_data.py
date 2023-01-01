import boto3

MY_ZONE_NAME = "example.com."


def get_zone_id_from_name(zone_name):
    """Returns the Hosted Zone ID that matches the given hosted zone name"""
    zone_list = get_hosted_zone_list()

    for zone in zone_list:
        if zone.get("Name") == zone_name:
            return (zone.get("Id")).split("/")[-1]


def get_hosted_zone_list():
    """Returns a list of Hosted Zones for the authenticated account"""
    client = boto3.client("route53")

    response_object = client.get_hosted_zone_list()
    zone_list = response_object.get("HostedZones")
    return zone_list


my_zone_id = get_zone_id_from_name(MY_ZONE_NAME)
print(my_zone_id)
