from enum import Enum
from datetime import datetime
from geopy.distance import vincenty

def format_datetime(since):
	datetime_from=datetime.fromtimestamp(float(since)).strftime('%Y-%m-%d %H:%M:%S.%f')
	datetime_to=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
	return [datetime_from, datetime_to]


def get_filters_from_query_string(params):
	filters = {}
	status = params.get('status', None)
	category = params.get('category', None)
	since = params.get('since', None)

	if status:
		filters['status'] = status
	if category:
		filters['category'] = category
	if since:
		filters['opened__range'] = format_datetime(since)
	return filters

def get_cases_within_radius(params, cases):

	location = params.get('near', None)
	if not location:
		return cases

	latitude=location.split(',')[0]	
	longitude = location.split(',')[1]

	nearby_cases=[]
	for case in cases:
		center = (float(latitude), float(longitude))
		if case.point:
			case_location = (float(case.point.latitude), float(case.point.longitude))
			if vincenty(center, case_location).miles <= 5:
				nearby_cases.append(case)
	return nearby_cases		



	
