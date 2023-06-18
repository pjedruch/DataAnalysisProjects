import numpy as np

# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076, 51.40000153, 50.5, 75.69999695,
    58.40000153, 40.09999847, 61.5, 57.09999847,
    60.90000153, 66.59999847, 60.40000153, 68.09999847,
    66.90000153, 53.40000153, 48.59999847, 56.79999924,
    71.59999847, 58.40000153, 70.40000153, 41.20000076
])

# print some data
print(countries[:10])
print(countries[1:5])
print('{}'.format(employment[:5]))

# dtype

print(countries.dtype)
print(employment.dtype)


# lista po panstwach - Examining country {}....
# 'Country {} has employment {}'

def ex_country(data_coll: np.ndarray):
    """
    Printing data.

    :param data_coll: List of countries
    :type data_coll: np.ndarray
    """

    info = "Examining country {}\n"
    for country in data_coll:
        print(info.format(country))


ex_country(countries)


def country_employment(data_coll: np.ndarray, data_coll_2: np.ndarray):
    """
    Printing Country {} has employment {}.

    :param data_coll: List of countries
    :param data_coll_2: List of employment
    """
    for index in range(len(data_coll)):
        print("Printing Country {} has employment {:.2f}".format(data_coll[index]
                                                             , data_coll_2[index]))


country_employment(countries, employment)
