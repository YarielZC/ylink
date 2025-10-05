from bson import ObjectId

def link_schema(link):
    return {
        'id': str(link['_id']),
        'user_id': str(link['user_id']),
        'small_url': str(link['small_url']),
        'redirect_url': str(link['redirect_url']),
        'touch_counts': int(link['touch_counts']),
        'create_at': str(link['create_at']),
    }