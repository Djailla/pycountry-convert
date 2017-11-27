#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)
#  @namespace logging_mv_integrations

import pytest

from pycountry_convert import (
    convert_country_alpha2_to_country_name,
    convert_country_alpha2_to_continent_code,
    convert_country_name_to_country_alpha2,
    convert_country_alpha3_to_country_alpha2,
)

class TestCountryConvert():

    def test_country_alpha2_to_continent(self):
        cn_continent = convert_country_alpha2_to_continent_code('US')
        assert(cn_continent)
        assert(cn_continent == 'NA')

        cn_continent = convert_country_alpha2_to_continent_code('AU')
        assert(cn_continent)
        assert(cn_continent == 'OC')

        cn_continent = convert_country_alpha2_to_continent_code('NZ')
        assert(cn_continent)
        assert(cn_continent == 'OC')

        cn_continent = convert_country_alpha2_to_continent_code('JP')
        assert(cn_continent)
        assert(cn_continent == 'AS')

    def test_country_alpha2_to_country_name(self):
        cn_name = convert_country_alpha2_to_country_name('JP')
        assert(cn_name)
        assert(cn_name == 'Japan')

        cn_name = convert_country_alpha2_to_country_name('KR')
        assert(cn_name)
        assert(cn_name == 'Korea, Republic of')

        cn_name = convert_country_alpha2_to_country_name('RU')
        assert(cn_name)
        assert(cn_name == 'Russian Federation')

    def test_country_name_to_country_alpha2(self):
        cn_a2_code = convert_country_name_to_country_alpha2('USA')
        assert(cn_a2_code)
        assert(cn_a2_code == 'US')

        cn_a2_code = convert_country_name_to_country_alpha2('United States')
        assert(cn_a2_code)
        assert(cn_a2_code == 'US')

        cn_a2_code = convert_country_name_to_country_alpha2('South Korea')
        assert(cn_a2_code)
        assert(cn_a2_code == 'KR')

    def test_country_alpha3_to_country_alpha2(self):
        cn_a2_code = convert_country_alpha3_to_country_alpha2('USA')
        assert(cn_a2_code)
        assert(cn_a2_code == 'US')

        cn_a2_code = convert_country_alpha3_to_country_alpha2('RUS')
        assert(cn_a2_code)
        assert(cn_a2_code == 'RU')

    def test_invalid_country_alpha2(self):
        with pytest.raises(KeyError) as e_key:
            convert_country_alpha2_to_continent_code('AA')
        assert "Invalid Country Alpha-2 code: 'AA'" in str(e_key)