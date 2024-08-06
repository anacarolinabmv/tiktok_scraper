# pylint: disable=C0116, C0114, C0304,C0303
from typing import Dict
import json
from datetime import datetime
import gettext
import requests
from bs4 import BeautifulSoup
import pycountry
from langcodes import *


def get_country_name(alpha_2):
    try:
        if not alpha_2 or not len(alpha_2)==2:
            raise ValueError('Unable to retrieve country information')
        
        country = pycountry.countries.get(alpha_2=f'{alpha_2}')
        print(country)
        
        if not country: 
            raise AttributeError(f'No country name found for the country code: {alpha_2}')
            
        norwegian = gettext.translation('iso3166-1', pycountry.LOCALES_DIR,
        languages=['nb']).install()
        norwegian_name = _(f'{country.name}')
        return norwegian_name
    
    except Exception as err:
        return f"Something went wrong. {err}"


def get_language_name(alpha_2):
        try:
            if not alpha_2 or  not len(alpha_2)==2:
                raise ValueError('Unable to retrieve language information')
            language_norwegian = Language.make(language=f'{alpha_2}').display_name("no")
            return language_norwegian
        except ValueError as err :
            return f"Something went wrong: {err}"


def get_formated_date(timestamp):
    if not timestamp:
        return 'This user has not changed username'
    try:
        utc_time = datetime.fromtimestamp(timestamp) 
        return utc_time.strftime("%d.%m.%Y")
    except Exception as err:
        return f"Something went wrong: {err}"


def get_avatar_url(url):
    if not url:
        return 'This user does not have a profile picture'
    
    clean_url = url.replace('\u002F','/')
    return clean_url
    
def fetch_profile_data(username: str) -> Dict:
    '''
    Scrape user data from TikTok profile
    '''
    try:
        url = f'https://www.tiktok.com/@{username}'
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        script_data = soup.find('script', id='__UNIVERSAL_DATA_FOR_REHYDRATION__')    
        
        data = json.loads(script_data.text)['__DEFAULT_SCOPE__']["webapp.user-detail"]["userInfo"]

        return data

    except KeyError:
        raise ValueError(f'No data found for user: {username}')
    except Exception as e:
        raise ValueError(f'Error fetching data for user {username}: {str(e)}')


def get_user_data(username):    
    try:
        data = fetch_profile_data(username) 
             
        user_data = {
        "Brukernavn": data.get("user", {}).get("uniqueId"),
        "Visningsnavn": data.get("user", {}).get("nickname"),
        "Identifikator": data.get("user", {}).get("id"),
        "Sted": get_country_name(data.get("user", {}).get("region")),
        "Språk": get_language_name(data.get("user", {}).get("language")),
        "Siste brukernavn-endring": get_formated_date(data.get("user", {}).get("nickNameModifyTime")),
        "url": get_avatar_url(data.get("user", {}).get("avatarLarger")),
        }
        
        return user_data
    
    except ValueError as e:
        return str(e)
    except Exception as e:
        raise RuntimeError(f'An error occurred fetching the data: {str(e)}')
    