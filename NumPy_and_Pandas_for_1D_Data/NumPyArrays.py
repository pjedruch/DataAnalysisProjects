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

# Change False to True for each block of code to see what it does

# Accessing elements
if True:
    print(countries[0])
    print(countries[3])
    print(employment[5])
    print(countries[10])

# Slicing
if False:
    print(countries[0:3])
    print(countries[:3])
    print(countries[17:])
    print(countries[:])
    print(employment[5:9])
    print(employment[:8])
    print(employment[15:])
    print(employment[:])

# Element types
if False:
    print(countries.dtype)
    print(employment.dtype)
    print(np.array([0, 1, 2, 3]).dtype)
    print(np.array([1.0, 1.5, 2.0, 2.5]).dtype)
    print(np.array([True, False, True]).dtype)
    print(np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype)
    print(np.array(['qwe', 2.5]).dtype)

    matrix = np.array([
        1, 0, 1, 0, 1, 1, 0
    ])

    print(matrix[:2])
    print(matrix.dtype)
# Looping
# lista po panstwach - Examining country {}....
# 'Country {} has employment {}'
if False:
    for country in countries:
        print('Examining country {}'.format(country))

    for index in range(len(countries)):
        print('Country {} has employment {:.2f}'.format(countries[index], employment[index]))

# Numpy functions
if False:
    print(employment.mean())
    print(employment.std())
    print(employment.max())
    print(employment.sum())


def max_employment(countries: np.ndarray, employment: np.ndarray) -> tuple:
    """
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.

    Parameters:
        (np.ndarray) countries - list of countries
        (np.ndarray) employment - list of employment in countries
    Returns:
       tuple - Returns tupla with max value of employment and name of country
    """

    max_value = employment.max()

    max_country = countries[np.argmax(employment)]

    return max_country, '%.2f' % max_value


print(max_employment.__doc__)
print(max_employment(countries, employment))
