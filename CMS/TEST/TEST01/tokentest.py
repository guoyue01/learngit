l={
    'resultCode': '0',
    'resultDesc': 'success',
    'resultData':
        {
            'couponsList':
             [
                 {
                     'couponName': 'cmstest1534231590.625395',
                     'limitType': 'allspu',
                     'couponId': '236147664700325888',
                     'couponType': 'fullcut',
                     'fullAmount': 10000,
                     'cutAmount': 1000,
                     'couponStatus': True
                 }
             ]
        }
}
assert l['resultData']['couponsList'][0]['couponStatus']==True , 'error'