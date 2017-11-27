#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pycountry-convert

import sys
import pycountry
from pprintpp import pprint

from pycountry_convert import (
    get_countries,
    convert_country_alpha2_to_country_name,
    convert_country_name_to_country_alpha2,
    convert_country_alpha3_to_country_alpha2,

    convert_country_alpha2_to_continent_code
)


def main():
    for x in pycountry.countries:
        pprint(x)

    pprint(get_countries())

    for key, value in sorted(get_countries().items()):
        pprint({key: value})

    try:
        cn_continent = convert_country_alpha2_to_continent_code('AA')
        pprint(cn_continent)
    except KeyError as kerr:
        print("Key error: {0}".format(kerr))
    except:
        print("Unexpected error:", sys.exc_info()[0])

    try:
        cn_continent = convert_country_alpha2_to_continent_code(None)
        pprint(cn_continent)
    except KeyError as kerr:
        print("Key error: {0}".format(kerr))
    except:
        print("Unexpected error:", sys.exc_info()[0])

    cn_continent = convert_country_alpha2_to_continent_code('US')
    pprint(cn_continent)

    cn_continent = convert_country_alpha2_to_continent_code('AU')
    pprint(cn_continent)
    cn_continent = convert_country_alpha2_to_continent_code('NZ')
    pprint(cn_continent)
    cn_continent = convert_country_alpha2_to_continent_code('JP')
    pprint(cn_continent)

    cn_name = convert_country_alpha2_to_country_name('JP')
    pprint(cn_name)

    cn_a2_code = convert_country_name_to_country_alpha2('USA')
    pprint(cn_a2_code)
    cn_a2_code = convert_country_name_to_country_alpha2('United States')
    pprint(cn_a2_code)
    cn_a2_code = convert_country_name_to_country_alpha2('South Korea')
    pprint(cn_a2_code)
    cn_name = convert_country_alpha2_to_country_name(cn_a2_code)
    pprint(cn_name)

    cn_name = convert_country_alpha2_to_country_name('RU')
    pprint(cn_name)
    cn_a2_code = convert_country_name_to_country_alpha2(cn_name)
    pprint(cn_a2_code)
    cn_a2_code = convert_country_alpha3_to_country_alpha2('RUS')
    pprint(cn_a2_code)

    cn_name = convert_country_alpha2_to_country_name('GB')
    pprint(cn_name)
    cn_name = convert_country_alpha2_to_country_name('US')
    pprint(cn_name)


if __name__ == '__main__':
    sys.exit(main())
