from ff_espn_api import League

league_id = 939603
year = 2019
swid = '{6AB2CECC-9BA9-484A-8AD1-665122725A9F}'
espn_s2 = 'AEC1KU4z9AZ45%2BTMBhcPxCNUsILOcXsytMiYivHRGn' \
          '%2FEOSExocT8FdCfIrtcoLcrY7j98wxQPSBuGmOa%2BzZVy0ndGisCqPHt' \
          '%2B2lzDRDjuiBQKGStfnd54WYqIiFVSwi%2FIKGT0GwMyeWD9BPkLcee9T' \
          '%2BY5z1wZXjGxQuoNKCIlAPWdQIxBcPw2FkQX2G9NcZMnGLnNjn7PxlcIB' \
          'HVms71uGsFXnNHCCB9LZMgmcbRFEPwSkd9spgoS%2FS6jb5askfDE4SAyF' \
          'DOEfUjJecXYMkWQy3AE%2FwsJd66QK1YsV7uBV5iwA%3D%3D'

league = League(league_id, year, espn_s2, swid)

print(league.teams)
