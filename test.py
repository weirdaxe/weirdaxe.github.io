import requests
import json

api_url = 'https://www.page2api.com/api/v1/scrape'
a = []
gm = []
for i in [3,5,7,9,11,13,15,17,19,
          21,23,25,27,29,31,33,35,37,
          39,41,43,45,47,49,51,53,55,
          57,59,61,63,65,67,69,71]:
    payload = {
          "api_key": "2f1d7a26162eed23699d89e37b81cc528014cadd",
          "url": f"www.glassdoor.com/Reviews/General-Motors-(GM)-Reviews-E279_P{i}.htm?filter.iso3Language=eng",
          "real_browser": True,
          "merge_loops": True,
          "premium_proxy": "us",
          "scenario": [
            {
              "loop": [
                { "wait_for": "div.gdReview" },
                { "execute": "parse" },
                { "execute_js": "document.querySelector(\".nextButton\").click()" },
              ],
              "iterations": 2
            }
          ],
          "parse": {
            "reviews": [
              {
                "_parent": "div.gdReview",
                "title": "a.reviewLink >> text",
                "author_info": ".authorInfo >> text",
                "rating": "span.ratingNumber >> text",
                "pros": "span[data-test=pros] >> text",
                "cons": "span[data-test=cons] >> text",
                "helpful": "div.common__EiReviewDetailsStyle__socialHelpfulcontainer >> text"
              }
            ]
          }
        }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post(api_url, data=json.dumps(payload), headers=headers)
    result = json.loads(response.text)
    gm.append(result)

print(result)