def get_upload_product_path(instance, file):
    return f"shops/shop_{instance.shop.name}/{file}"

def get_upload_logo_path(instance, file):
    return f"logos/shop_{instance.shop.name}/{file}"