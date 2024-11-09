def increase_version(version, breaking_change, new_features):
    major, minor, patch = version
    if breaking_change:
        major += 1
        minor = 0
        patch = 0
    elif new_features:
        minor += 1
        patch = 0
    else:
        patch += 1
    return (major,minor,patch)

# print(increase_version((0,0,0),breaking_chance=False,new_features=True))

def is_more_recent(v1, v2):
    return v1 > v2

# print(is_more_recent((0,0,1),(0,1,0)))

def is_older(v1, v2):
    return v1 < v2