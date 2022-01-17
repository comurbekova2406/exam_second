def country_data(name, **country_data):
    print(f' {name}')
    for info in country_data:
        print(country_data)


country_data(name='USA', population='330 million', is_democratic=True)


country_data(name='Kyrgyzstan', area='200 km2',
             have_borders_with=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China'])
