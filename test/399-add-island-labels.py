# Natural Earth 110m 
assert_has_feature(
    1, 0, 0, 'earth',
    { 'kind': 'earth', 'source': 'naturalearthdata.com' })

# Natural Earth 50m 
assert_has_feature(
    2, 0, 1, 'earth',
    { 'kind': 'earth', 'source': 'naturalearthdata.com' })

# Natural Earth 10m 
assert_has_feature(
    8, 40, 98, 'earth',
    { 'kind': 'earth', 'source': 'naturalearthdata.com' })

# OSM derived data from openstreetmapdata.com
assert_has_feature(
    9, 81, 197, 'earth',
    { 'kind': 'earth', 'source': 'openstreetmapdata.com' })



# NODE continent labels (from places)
assert_has_feature(
    1, 0, 0, 'earth',
    { 'kind': 'continent', 'name': 'North America', 'label_placement': 'yes' })



# NODE archipelago labels (from place nodes)
# http://www.openstreetmap.org/node/3178316462
assert_has_feature(
    15, 10776, 14921, 'earth',
    { 'kind': 'archipelago', 'label_placement': 'yes', 'min_zoom': 15 })

# NODE archipelago labels (from place nodes)
# http://www.openstreetmap.org/node/358955020
assert_has_feature(
    15, 9367, 12534, 'earth',
    { 'kind': 'archipelago', 'label_placement': 'yes', 'min_zoom': 15 })

# LARGE archipelago labels (from place polygons)
# There aren't any today
# Really these should be lines, but will initially be points

# MEDIUM archipelago labels (from place polygons)
# There aren't any today
# Really these should be lines, but will initially be points

# SMALL archipelago labels (from place polygons)
# Really these should be lines, but will initially be points
# http://www.openstreetmap.org/way/39890363
# In North America, but no name, so not exported by default
assert_has_feature(
    13, 2466, 3599, 'earth',
    { 'kind': 'archipelago', 'label_placement': 'yes' })

# SMALL archipelago labels (from place polygons)
# Really these should be lines, but will initially be points
# http://www.openstreetmap.org/way/39890363
# In Europe, with a name, is exported
assert_has_feature(
    14, 9328, 4743, 'earth',
    { 'kind': 'archipelago', 'label_placement': 'yes' })



# NODE island labels (from place nodes)
# http://www.openstreetmap.org/node/358796350
# Yerba Buena Island, near SF
assert_has_feature(
    15, 5245, 12661, 'earth',
    { 'kind': 'island', 'label_placement': 'yes' })

# NODE island labels (from place nodes)
# http://www.openstreetmap.org/node/358761955
# Bird Island, north of SF
assert_has_feature(
    15, 5230, 12659, 'earth',
    { 'kind': 'island', 'label_placement': 'yes' })

# NODE island labels (from place nodes)
# http://www.openstreetmap.org/node/358768646
# Kent Island, north of SF
assert_has_feature(
    15, 5217, 12649, 'earth',
    { 'kind': 'island', 'label_placement': 'yes' })

# LARGE island labels (from place polygons)
# http://www.openstreetmap.org/relation/4227580
# Manitoulin Island, Canada
assert_has_feature(
    7, 34, 45, 'earth',
    { 'kind': 'island', 'label_placement': 'yes' })
    
# LARGE island labels (from place polygons)
# http://www.openstreetmap.org/relation/5176042
# Trinidad, the island of the nation
assert_has_feature(
    7, 42, 60, 'earth',
    { 'kind': 'island', 'label_placement': 'yes' })

# MEDIUM island labels (from place polygons)
# http://www.openstreetmap.org/way/124916662
# Cockburn Island, Canada
assert_has_feature(
    9, 137, 182, 'earth',
    { 'kind': 'island', 'label_placement': 'yes' })

# MEDIUM island labels (from place polygons)
# http://www.openstreetmap.org/way/40500912
# San Miguel Island, California
assert_has_feature(
    10, 169, 408, 'earth',
    { 'kind': 'island', 'label_placement': 'yes' })

# MEDIUM island labels (from place polygons)
# http://www.openstreetmap.org/way/40500922
# West Anacapa Island, California
assert_has_feature(
    12, 689, 1636, 'earth',
    { 'kind': 'island', 'label_placement': 'yes' })

# MEDIUM island labels (from place polygons)
# http://www.openstreetmap.org/way/157429145
# Angel Island, near SF
# 12, 654, 1581
assert_has_feature(
    12, 655, 1581, 'earth',
    { 'kind': 'island', 'label_placement': 'yes' })

# SMALL island labels (from place polygons)
# http://www.openstreetmap.org/way/24433344
# Alcatraz Island, near SF
assert_has_feature(
    15, 5240, 12659, 'earth',
    { 'kind': 'island', 'label_placement': 'yes' })

# SMALL island labels (from place polygons)
# http://www.openstreetmap.org/way/22693068
# Great Gull Island, NY state
assert_has_feature(
    15, 5240, 12659, 'earth',
    { 'kind': 'island', 'label_placement': 'yes' })

# SMALL island labels (from place polygons)
# http://www.openstreetmap.org/way/308262375
# Goose Island, NY state
assert_has_feature(
    16, 19659, 24507, 'earth',
    { 'kind': 'island', 'label_placement': 'yes' })

# SMALL island labels (from place polygons)
# http://www.openstreetmap.org/way/37248735
# Rincon Island, California
assert_has_feature(
    16, 11023, 26103, 'earth',
    { 'kind': 'island', 'label_placement': 'yes' })



# NODE islet labels (from place nodes)
# http://www.openstreetmap.org/node/358795646
# Pyramid Rock, SF
assert_has_feature(
    16, 10466, 25327, 'earth',
    { 'kind': 'island', 'label_placement': 'yes' })

# LARGE islet labels (from place polygons)
# http://www.openstreetmap.org/way/40500803
# Sugarloaf Island, west of SF
# 15, 5188, 12673
assert_has_feature(
    15, 5187, 12673, 'earth',
    { 'kind': 'island', 'label_placement': 'yes' })

# MEDIUM islet labels (from place polygons)
# http://www.openstreetmap.org/way/157449982
# Bird Island, west of SF
assert_has_feature(
    16, 10493, 25303, 'earth',
    { 'kind': 'island', 'label_placement': 'yes' })

# SMALL islet labels (from place polygons)
# http://www.openstreetmap.org/way/306344403
# Sail Rock, near SF
assert_has_feature(
    17, 20934, 50791, 'earth',
    { 'kind': 'islet', 'label_placement': 'yes' })

# SMALL islet labels (from place polygons)
# http://www.openstreetmap.org/way/32289183
# Little Mile Rock, SF
assert_has_feature(
    17, 20931, 50653, 'earth',
    { 'kind': 'islet', 'label_placement': 'yes' })