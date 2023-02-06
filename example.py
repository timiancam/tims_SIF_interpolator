import tims_SIF_interpolator

inputs = [[0.8, 0.8, 0.8], [0.5, 0.5, 0.5]]
geometry_defects = ['LDSE']
#geometry_defects = ['LDSE', 'CDSI']

interpolated_results = tims_SIF_interpolator.interpolate(inputs, geometry_defects)

print(interpolated_results)
print('\n')

print(interpolated_results[0])
print('\n')

print(interpolated_results[0]['LDSE'])
#print(interpolated_results[0]['CDSI'])
print('\n')

print(interpolated_results[0]['LDSE']['i2_depth'])
#print(interpolated_results[0]['CDSI']['i3_surface'])