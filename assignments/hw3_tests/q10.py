OK_FORMAT = True

test = {   'name': 'q10',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> assert type(ans10(np.array([1, 2, 3]), np.array([4, 5, 6]))) == dict\n'
                                               ">>> assert ans10(np.array([1, 2, 3]), np.array([4, 5, 6]))['1_norm'] == 9.0\n"
                                               ">>> assert ans10(np.array([1, 2, 3]), np.array([4, 5, 6]))['inf_norm'] == 3.0\n"
                                               ">>> assert ans10(np.array([1, 2, 3]), np.array([4, 5, 6]))['2_norm'] > 5.0\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
