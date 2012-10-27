from django.contrib.gis.feeds import Feed
from models import Incident


class CADGeoRSS(Feed):
    title = "San Luis Obispo County Fire Latest Incidents"
    link = "/"
    description = "Latest 15 incidents"

    def items(self):
        return Incident.objects.order_by('-time')[:15]

    def item_title(self, item):
        return item.event_id

    def item_description(self, item):
        return "%s @ %s(%s)" % (item.details, item.jrsdtn, item.time)

    def item_link(self, item):
        return "/incident/%s" % item.event_id

    def item_geometry(self, item):
        return item.latlng
