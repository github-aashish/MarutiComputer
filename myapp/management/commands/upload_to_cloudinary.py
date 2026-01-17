import os
from django.core.management.base import BaseCommand
from django.conf import settings
import cloudinary

class Command(BaseCommand):
    help = 'Upload local images to Cloudinary with filenames matching local names'

    def add_arguments(self, parser):
        parser.add_argument(
            '--local-folder',
            type=str,
            help='Path to the local folder containing images to upload',
            required=True
        )
        parser.add_argument(
            '--cloud-folder',
            type=str,
            help='Cloudinary folder to upload images into (e.g. "photos/")',
            default=''
        )

    def handle(self, *args, **options):
        # Configure Cloudinary from Django settings
        cloudinary.config(
            cloud_name = settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
            api_key = settings.CLOUDINARY_STORAGE['API_KEY'],
            api_secret = settings.CLOUDINARY_STORAGE['API_SECRET'],
            secure=True
        )

        local_folder = options['local_folder']
        cloud_folder = options['cloud_folder']

        if not os.path.isdir(local_folder):
            self.stderr.write(self.style.ERROR(f"Local folder not found: {local_folder}"))
            return

        files_uploaded = 0

        for filename in os.listdir(local_folder):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')):
                file_path = os.path.join(local_folder, filename)

                # Prepare public_id with folder + filename without extension
                public_id = os.path.join(cloud_folder, os.path.splitext(filename)[0]).replace('\\','/')

                try:
                    response = cloudinary.uploader.upload(
                        file_path,
                        public_id=public_id,
                        overwrite=True,
                        resource_type='image'
                    )
                    self.stdout.write(self.style.SUCCESS(
                        f"Uploaded '{filename}' to Cloudinary public_id='{public_id}', URL: {response.get('secure_url')}"
                    ))
                    files_uploaded += 1
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed to upload '{filename}': {e}"))

        self.stdout.write(self.style.SUCCESS(f"Done! Total files uploaded: {files_uploaded}"))
