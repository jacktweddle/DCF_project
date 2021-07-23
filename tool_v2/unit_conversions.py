#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


def cel_to_K(x):
    '''Convert Celsius to Kelvin'''
    if type(x) is np.ndarray:
        if x.any() < -273.15:
            raise ValueError('Cannot have temperature lower than -273.15 Celsius!')
    if type(x) in [int, float, np.int64, np.float64] and x < -273.15:
        raise ValueError('Cannot have temperature lower than -273.15 Celsius!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x + 273.15


def K_to_cel(x):
    '''Convert Kelvin to Celsius'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Cannot have temperature lower than 0 Kelvin!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Cannot have temperature lower than 0 Kelvin!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x - 273.15


def rem_to_sv(x):
    '''Convert Rem to Sievert'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative dosage is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative dosage is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x / 100


def sv_to_rem(x):
    '''Convert Sievert to Rem'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative dosage is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative dosage is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x * 100


def rem_to_microsv(x):
    '''Converts rem to microsv'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative dosage is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative dosage is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return micro(rem_to_sv(x))


def microsv_to_rem(x):
    '''Converts microsv to rem'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative dosage is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative dosage is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return mega(sv_to_rem(x))


def psv_cm2_to_microsv_hour(x):
    '''Converts psv cm2 to microsv/hour per n/cm2/s'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative dosage is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative dosage is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return mega(3600 * x)


def microsv_hour_to_psv_cm2(x):
    '''Converts microsv/hour per n/cm2/s to psv cm2'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative dosage is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative dosage is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return micro(x / 3600)


def psv_cm2_to_rem_hour(x):
    '''Converts psv cm2 to rem/hour per n/cm2/s'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative dosage is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative dosage is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return tera(3600 * x) * 100


def rem_hour_to_psv_cm2(x):
    '''Converts rem/hour per n/cm2/s to psv cm2'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative dosage is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative dosage is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return pico(x / 3600) / 100


def curie_to_bq(x):
    '''Convert Curie to Becquerel'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative activity is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative activity is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x * 3.7E10


def bq_to_curie(x):
    '''Convert Becquerel to Curie'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative activity is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative activity is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x / 3.7E10


def seconds_to_minutes(x):
    '''Convert seconds to minutes'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative time is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative time is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x / 60


def seconds_to_hours(x):
    '''Convert seconds to hours'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative time is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative time is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x / (60*60)


def seconds_to_days(x):
    '''Convert seconds to days'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative time is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative time is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x / (24*60*60)


def seconds_to_years(x):
    '''Convert seconds to years'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative time is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative time is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x / (365.25*24*60*60)


def years_to_days(x):
    '''Convert years to days'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative time is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative time is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x * (365.25)


def years_to_hours(x):
    '''Convert years to hours'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative time is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative time is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x * (365.25*24)


def years_to_minutes(x):
    '''Convert years to minutes'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative time is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative time is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x * (365.25*24*60)


def years_to_seconds(x):
    '''Convert years to seconds'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative time is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative time is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x * (365.25*24*60*60)


def ev_to_joule(x):
    '''Convert electron volts to Joules'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative energy is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative energy is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x * 1.602E-19


def joule_to_ev(x):
    '''Convert Joules to electron volts'''
    if type(x) is np.ndarray:
        if x.any() < 0:
            raise ValueError('Negative energy is not physical!')
    if type(x) in [int, float, np.int64, np.float64] and x < 0:
        raise ValueError('Negative energy is not physical!')
    if type(x) not in [int, float, np.ndarray, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x / 1.602E-19


def milli(x):
    '''Convert to milli__'''
    if type(x) not in [int, float, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x / 1E-3


def micro(x):
    '''Convert to micro__'''
    if type(x) not in [int, float, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x / 1E-6


def nano(x):
    '''Convert to nano__'''
    if type(x) not in [int, float, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x / 1E-9


def pico(x):
    '''Convert to pico__'''
    if type(x) not in [int, float, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x / 1E-12


def kilo(x):
    '''Convert to kilo__'''
    if type(x) not in [int, float, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x / 1E3


def mega(x):
    '''Convert to mega__'''
    if type(x) not in [int, float, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x / 1E6


def giga(x):
    '''Convert to giga__'''
    if type(x) not in [int, float, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x / 1E9


def tera(x):
    '''Convert to tera__'''
    if type(x) not in [int, float, np.int64, np.float64]:
        raise TypeError('Only valid integers or floats can be passed.')
    return x / 1E12
