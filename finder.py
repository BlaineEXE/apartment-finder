from craigslist import CraigslistHousing
from functions import in_box
from functions import posted_recently
import settings
import sender
from database import Database

database = Database()

print('Starting scrape...')
houses = CraigslistHousing(site=settings.CRAIGSLIST_SITE, category='apa',
    filters={'max_price': settings.MAX_PRICE, 'min_price': settings.MIN_PRICE,
        'bedrooms': [3,5]})

results = houses.get_results(sort_by='newest', geotagged=True, limit=1000)
apartments = []

for result in results:
    geotag = result["geotag"]
    # if geotag is not None and posted_recently(result):
    if geotag is not None:
        for box in settings.BOXES.items():
            if in_box(geotag, box[1]):
                if not database.contains(result['id']):
                    print('adding: ' + str(result['id']))
                    database.add(result)
                    sender.post_to_slack(result, box[0])
                else:
                    print('already exists: ' + str(result['id']))
                break

print('Scrape done')
