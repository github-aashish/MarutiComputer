import os
from django.core.management.base import BaseCommand
from django.conf import settings
from myapp.models import admission  # change to your actual model
import cloudinary
import cloudinary.uploader

class Command(BaseCommand):
    help = 'Re-upload all User images to Cloudinary and update ImageField'

    def add_arguments(self, parser):
        parser.add_argument(
            '--local-media-root',
            type=str,
            help='Path to your Django media root (where images are stored locally)',
            required=True
        )

    def handle(self, *args, **options):
        # Configure Cloudinary from settings
        cloudinary.config(
            cloud_name = settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
            api_key = settings.CLOUDINARY_STORAGE['API_KEY'],
            api_secret = settings.CLOUDINARY_STORAGE['API_SECRET'],
            secure=True
        )

        local_media_root = options['local_media_root']

        users = admission.objects.all()
        total = users.count()
        uploaded = 0

        for user in users:
            if user.image:  # check if image field has a value
                local_path = os.path.join(local_media_root, user.image.name)
                
                if not os.path.isfile(local_path):
                    self.stderr.write(self.style.ERROR(f"File not found: {local_path}"))
                    continue

                # Remove any leading slashes from image.name for public_id
                public_id = user.image.name.replace('\\','/').lstrip('/').rsplit('.', 1)[0]

                try:
                    response = cloudinary.uploader.upload(
                        local_path,
                        public_id=public_id,
                        overwrite=True,
                        unique_filename=False,
                        resource_type='image'
                    )

                    # Update image field with new Cloudinary URL
                    # If you are using ImageField with django-cloudinary-storage, just keep the same name
                    # Or store full URL in a separate field
                    # Example: update ImageField name to match Cloudinary public_id
                    user.image.name = public_id + '.' + local_path.split('.')[-1]  # keep extension
                    user.save()

                    self.stdout.write(self.style.SUCCESS(
                        f"Uploaded {user.image.name} → {response.get('secure_url')}"
                    ))
                    uploaded += 1

                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed {user.image.name}: {e}"))

        self.stdout.write(self.style.SUCCESS(f"Done! Uploaded {uploaded}/{total} images."))
