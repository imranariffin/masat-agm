from datetime import datetime, timedelta
from pytz import timezone
import pytz

def est_time():
	eastern = timezone('US/Eastern')
	# fmt = '%Y-%m-%d %H:%M:%S %Z%z'
	fmt = '%Y-%m-%d'
	loc_dt = eastern.localize(datetime.now())
	return str(loc_dt.strftime(fmt))