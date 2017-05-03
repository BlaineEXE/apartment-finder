from craigslist import CraigslistHousing
from functions import in_box
from functions import posted_recently
import settings
import sender

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
                #apartments.append(result)
                sender.post_to_slack(result, box[0])
                break

print('Scrape done')

#for apartment in apartments:
#    sender.post_to_slack(apartment)
