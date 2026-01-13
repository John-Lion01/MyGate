from storages.backends.s3boto3 import S3Boto3Storage

class SupabaseMediaStorage(S3Boto3Storage):
    location = ""
    file_overwrite = False

    def url(self, name):
        return (
            "https://oagiwwnlcodabgkyswhh.supabase.co"
            "/storage/v1/object/public/media/"
            + name
        )
